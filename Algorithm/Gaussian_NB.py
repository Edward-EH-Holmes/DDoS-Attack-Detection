import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix
import numpy as np

import time

def GNB(train, test):
    startGNB = time.time()

    data = pd.read_csv(train)
    
    data['Label'] = data['Label'].map({'BENIGN': 1, 'Portmap': 0})
    
    data.dropna(subset=['Flow Duration', 'Total Fwd Packets', 'Label'], inplace=True)
    
    X = data[['Flow Duration', 'Total Fwd Packets']]
    y = data['Label']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = GaussianNB()
    model.fit(X_train, y_train)

    correlation_matrix = np.corrcoef(X_train.T)

    print("Correlation matrix between parameters:")
    print(correlation_matrix)

    correlations = []
    for column in X_train.columns:
        correlation = np.corrcoef(X_train[column], y_train)[0, 1]
        correlations.append((column, correlation))
    print("Correlation between each parameter and the labels:")
    for column, correlation in correlations:
        print(f"{column}: {correlation}")
    
    predictions = model.predict(X_test)

    # Predictions on Test Data
    test_data = pd.read_csv(test)
    test_predictions = model.predict(test_data[['Flow Duration', 'Total Fwd Packets']])
    test_data['Predicted Label'] = test_predictions
    test_data['Predicted Label'] = test_data['Predicted Label'].map({1: 'BENIGN', 0: 'Portmap'})
    #print(test_data[['Flow Duration', 'Total Fwd Packets', 'Predicted Label']])

    endGNB = time.time()
    timeGNB = endGNB - startGNB
   
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
        'Time Taken (s)': timeGNB
    }
    return accuracy, timeGNB, precision_rate, false_alarm_rate