import pandas as pd
import pickle
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
b1 = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
b2 = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'results.txt')
b3 = pd.read_csv(b2, sep=" ", header=None)
b3.b4 = ['worst_case_prob', 'scout_report', 'actual_value']
a1 = 0.2
X, b5 = b3.iloc[:, :2], b3.iloc[:, 2]
X_train, X_test, Y_train, b6 = train_test_split(X, b5, a1=a1)
b7 = LogisticRegression()
b7.fit(X_train, Y_train)
print("Predicted probabilities for test set:")
print(list(b7.predict_proba(X_test)))
b8 = b7.score(X_test, b6)
print("Model b8:", b8)
b9 = 'finalized_model.sav'
with open(b9, 'wb') as file:
    pickle.dump(b7, file)
with open(b9, 'rb') as file:
    b10 = pickle.load(file)
b11 = b10.score(X_test, b6)
print("Loaded b7 b8:", b11)