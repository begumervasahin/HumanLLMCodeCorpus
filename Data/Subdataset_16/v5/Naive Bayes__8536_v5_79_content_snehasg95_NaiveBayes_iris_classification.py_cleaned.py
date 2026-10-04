
import pandas as pd
from sklearn import datasets
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
def fonk1():
    b1 = datasets.load_iris()
    X_train, X_test, y_train, b2 = train_test_split(b1.data, b1.target, test_size=0.25, random_state=0)
    return X_train, X_test, y_train, b2
def fonk2(X_train, X_test, y_train, b2):
    b3 = GaussianNB()
    b3.fit(X_train, y_train)
    b4 = b3.predict(X_test)
    return accuracy_score(b2, b4)
def fonk3():
    X_train, X_test, y_train, b2 = fonk1()
    b5 = fonk2(X_train, X_test, y_train, b2)
    print(f"Accuracy b5: {b5:.2f}")
if b6 = = "__main__":
    fonk3()