import pandas as pd
import pickle
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
url = ""
column_names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
base_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_path, 'results.txt')
df = pd.read_csv(file_path, sep=" ", header=None)
df.columns = ['worst_case_prob', 'scout_report', 'actual_value']
test_size = 0.2
X, Y = df.iloc[:, :2], df.iloc[:, 2]
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=test_size)
model = LogisticRegression()
model.fit(X_train, Y_train)
print(list(model.predict_proba(X_test)))
accuracy = model.score(X_test, Y_test)
print("Model accuracy:", accuracy)
filename = 'finalized_model.sav'
with open(filename, 'wb') as file:
    pickle.dump(model, file)
with open(filename, 'rb') as file:
    loaded_model = pickle.load(file)
loaded_model_accuracy = loaded_model.score(X_test, Y_test)
print("Loaded model accuracy:", loaded_model_accuracy)