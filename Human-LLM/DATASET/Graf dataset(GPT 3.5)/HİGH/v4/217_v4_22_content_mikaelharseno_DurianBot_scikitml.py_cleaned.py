import pandas as pd
import pickle
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
b1 = ""
b2 = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
b3 = os.path.dirname(os.path.abspath(__file__))
b4 = os.path.join(b3, 'results.txt')
b5 = pd.read_csv(b4, sep=" ", header=None)
b5.b6 = ['worst_case_prob', 'scout_report', 'actual_value']
a1 = 0.2
X, b7 = b5.iloc[:, :2], b5.iloc[:, 2]
X_train, X_test, Y_train, b8 = train_test_split(X, b7, a1=a1)
b9 = LogisticRegression()
b9.fit(X_train, Y_train)
print(list(b9.predict_proba(X_test)))
b10 = b9.score(X_test, b8)
print("Model b10:", b10)
b11 = 'finalized_model.sav'
with open(b11, 'wb') as file:
    pickle.dump(b9, file)
with open(b11, 'rb') as file:
    b12 = pickle.load(file)
b13 = b12.score(X_test, b8)
print("Loaded b9 b10:", b13)