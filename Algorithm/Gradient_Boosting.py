import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

import time

def GB(train, test):
    startGB = time.time()

    data = pd.read_csv(train)  
        
    data['Label'] = data['Label'].map({'BENIGN': 1, 'Portmap': 0})

    data.dropna(subset=['Flow Duration', 'Total Fwd Packets', 'Label'], inplace=True)

    X = data[['Flow Duration', 'Total Fwd Packets']]
    y = data['Label']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = GradientBoostingClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    test_data = pd.read_csv(test)
    test_predictions = model.predict(test_data[['Flow Duration', 'Total Fwd Packets']])
    test_data['Predicted Label'] = test_predictions
    test_data['Predicted Label'] = test_data['Predicted Label'].map({1: 'BENIGN', 0: 'Portmap'})
    #print(test_data[['Flow Duration', 'Total Fwd Packets', 'Predicted Label']])

    endGB = time.time()
    timeGB = endGB - startGB

    # Calculate Accuracy
    accuracy = accuracy_score(y_test, predictions)

    # Calculate Confusion Matrix
    tn, fp, fn, tp = confusion_matrix(y_test, predictions).ravel()
    
    # Calculate Precision
    precision_rate = tp / (tp + fp) if (tp + fp) > 0 else 0

    # Calculate False Alarm Rate
    false_alarm_rate = fp / (fp + tp) if (fp + tp) > 0 else 0

    # Output Metrics
    metrics = {
        'Accuracy': accuracy,
        'True Positives': tp,
        'False Positives': fp,
        'True Negatives': tn,
        'False Negatives': fn,
        'Precision': precision_rate,
        'False Alarm Rate': false_alarm_rate,
        'Time Taken (s)': timeGB
    }

    return accuracy, timeGB, precision_rate, false_alarm_rate