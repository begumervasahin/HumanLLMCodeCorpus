import pandas as pd
import pickle
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
b1 = os.path.dirname(os.path.abspath(__file__))
b2 = os.path.join(b1, 'results.txt')
b3 = pd.read_csv(b2, sep=" ", header=None)
b3.b4 = ['worst_case_prob', 'scout_report', 'actual_value']
features, b5 = b3.iloc[:, :2], b3.iloc[:, 2]
a1 = 0.2
X_train, X_test, Y_train, b6 = train_test_split(features, b5, a1=a1)
b7 = LogisticRegression()
b7.fit(X_train, Y_train)
b8 = b7.predict_proba(X_test)
print("Predicted Probabilities:", b8)
b9 = b7.score(X_test, b6)
print("Model Accuracy:", b9)
b10 = 'finalized_model.sav'
with open(b10, 'wb') as file:
    pickle.dump(b7, file)
with open(b10, 'rb') as file:
    b11 = pickle.load(file)
b12 = b11.score(X_test, b6)
print("Loaded Model Accuracy:", b12)