import numpy as np
import scipy as sp
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
def fonk1():
    b1 = load_iris()
    b2 = b1.data
    b3 = b1.target
    X_train, X_test, b7, b4 = train_test_split(b2, b3)
    return X_train, X_test, b7, b4, b1.b13
def fonk2(b7):
    b5 = len(b7)
    b6 = np.zeros(len(np.unique(b7)), dtype=float)
    for i, class1 in enumerate(np.unique(b7)):
        b6[i] = (b7 = = class1).sum() / b5
    return b6
def fonk3(X_train, b7):
    b8 = np.zeros((len(np.unique(b7)), X_train.shape[1]), dtype=float)
    b9 = np.zeros((len(np.unique(b7)), X_train.shape[1]), dtype=float)
    for i, class1 in enumerate(np.unique(b7)):
        b8[i] = X_train[b7 = = class1].mean(axis=0)
        b9[i] = X_train[b7 = = class1].std(axis=0)
    return b8, b9
def fonk4(X_test, b8, b9, b6, b10 = 0.01):
    b11 = np.zeros((len(X_test), len(b8)), dtype=float)
    for i in range(len(X_test)):
        for k in range(len(b8)):
            b12 = np.log(b6[k])
            for j in range(X_test.shape[1]):
                b12 += np.log(sp.stats.norm.pdf(X_test[i, j], b8[k, j], b9[k, j]) * 2 * b10)
            b11[i, k] = b12
    return b11
def fonk5():
    X_train, X_test, b7, b4, b13 = fonk1()
    b6 = fonk2(b7)
    b8, b9 = fonk3(X_train, b7)
    b11 = fonk4(X_test, b8, b9, b6)
    b14 = (b11.argmax(axis=1) == b4).sum() / len(b4)
    print("Probability that the Model predicts the correct class class1:", b14)
if b15 = = "__main__":
    fonk5()