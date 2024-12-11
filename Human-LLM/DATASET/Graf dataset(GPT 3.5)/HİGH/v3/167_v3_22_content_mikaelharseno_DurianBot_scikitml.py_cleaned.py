import pandas as pd
import pickle
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
def fonk1(b7):
    b1 = pd.read_csv(b7, sep=" ", header=None)
    b1.b2 = ['worst_case_prob', 'scout_report', 'actual_value']
    return b1
def fonk2(X_train, Y_train):
    b3 = LogisticRegression()
    b3.fit(X_train, Y_train)
    return b3
def fonk3(b3, filename):
    with open(filename, 'wb') as file:
        pickle.dump(b3, file)
def fonk4(filename):
    with open(filename, 'rb') as file:
        b4 = pickle.load(file)
    return b4
def fonk5(b3, X_test, b9):
    b5 = b3.score(X_test, b9)
    return b5
def fonk6():
    b6 = os.path.dirname(os.path.abspath(__file__))
    b7 = os.path.join(b6, 'results.txt')
    b1 = fonk1(b7)
    features, b8 = b1.iloc[:, :2], b1.iloc[:, 2]
    a1 = 0.2
    X_train, X_test, Y_train, b9 = train_test_split(features, b8, a1=a1)
    b3 = fonk2(X_train, Y_train)
    b10 = b3.predict_proba(X_test)
    print("Predicted Probabilities:", b10)
    b5 = fonk5(b3, X_test, b9)
    print("Model Accuracy:", b5)
    b11 = 'finalized_model.sav'
    fonk3(b3, b11)
    b4 = fonk4(b11)
    b12 = fonk5(b4, X_test, b9)
    print("Loaded Model Accuracy:", b12)
if b13 = = "__main__":
    fonk6()