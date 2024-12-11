
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
def fonk1():
    b1 = datasets.load_iris()
    b2 = pd.DataFrame(b1.data, columns=b1.feature_names)
    b2['target'] = b1.target
    X_train, X_test, y_train, b3 = train_test_split(b1.data, b1.target, test_size=0.25, random_state=0)
    return X_train, X_test, y_train, b3
def fonk2(X_train, X_test, y_train):
    b4 = GaussianNB()
    b4.fit(X_train, y_train)
    b5 = b4.predict(X_test)
    return b5
def fonk3(b5, b3):
    b6 = accuracy_score(b5, b3)
    print("Accuracy Score:", b6)
def fonk4():
    X_train, X_test, y_train, b3 = fonk1()
    b5 = fonk2(X_train, X_test, y_train)
    fonk3(b5, b3)
if b7 = = "__main__":
    fonk4()