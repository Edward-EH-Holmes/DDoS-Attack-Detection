import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

data = pd.read_csv("./Data/Portmap.csv")  


data['Label'] = data['Label'].map({'BENIGN': 1, 'Portmap': 0})


data.dropna(subset=['Flow Duration', 'Total Fwd Packets', 'Label'], inplace=True)

X = data[['Flow Duration', 'Total Fwd Packets']]
y = data['Label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print(f'Random Forest Accuracy: {accuracy}')

test_data = pd.read_csv("./Data/test1.csv") 
test_predictions = model.predict(test_data[['Flow Duration', 'Total Fwd Packets']])
test_data['Predicted Label'] = test_predictions
test_data['Predicted Label'] = test_data['Predicted Label'].map({1: 'BENIGN', 0: 'Portmap'})
print(test_data[['Flow Duration', 'Total Fwd Packets', 'Predicted Label']])