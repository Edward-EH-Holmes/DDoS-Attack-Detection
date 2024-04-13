import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
import pickle
import time

def train_GNB(train, test):
    data = pd.read_csv(train)
    data['Label'] = data['Label'].map({'BENIGN': 1, 'Portmap': 0})
    data.dropna(subset=['Flow Duration', 'Total Fwd Packets', 'Label'], inplace=True)
    
    X = data[['Flow Duration', 'Total Fwd Packets']]
    y = data['Label']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = GaussianNB()
    model.fit(X_train, y_train)
    
    with open('GNB.dat', 'wb') as f:
        pickle.dump(model, f)
    
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    
    return accuracy

def test_GNB(test):
    with open('GNB.dat', 'rb') as f:
        model = pickle.load(f)
    
    test_data = pd.read_csv(test)
    test_predictions = model.predict(test_data[['Flow Duration', 'Total Fwd Packets']])
    test_data['Predicted Label'] = test_predictions
    test_data['Predicted Label'] = test_data['Predicted Label'].map({1: 'BENIGN', 0: 'Portmap'})
    
    return test_data

def GNB(train_file, test_file):
    startGNB = time.time()
    
    if not os.path.exists('GNB.dat'):
        print("Training Gaussian Naive Bayes model...")
        accuracy = train_GNB(train_file, test_file)
    else:
        print("Loading pre-trained model...")
        accuracy = test_GNB(test_file)
    
    print("Accuracy:", accuracy)
    
    endGNB = time.time()
    timeGNB = endGNB - startGNB

    return accuracy, timeGNB
