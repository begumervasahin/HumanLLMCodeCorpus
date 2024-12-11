import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from scipy.stats import norm
def fonk1():
    b1 = load_iris()
    b2 = b1.data
    b3 = b1.target
    X_train, X_test, y_train, b4 = train_test_split(b2, b3)
    return X_train, X_test, y_train, b4, b1.b12
def fonk2(X_train, y_train):
    b5 = len(np.unique(y_train))
    b6 = X_train.shape[1]
    b7 = np.array([X_train[y_train == i].mean(axis=0) for i in range(b5)])
    b8 = np.array([X_train[y_train == i].std(axis=0) for i in range(b5)])
    return b7, b8
def fonk3(y_train):
    b9 = np.array([(y_train == i).sum() / len(y_train) for i in range(len(np.unique(y_train)))])
    return b9
def fonk4(X_test, b7, b8, b9):
    a1 = 0.01
    b5 = len(b9)
    num_test_samples, b6 = X_test.shape
    b10 = np.zeros((num_test_samples, b5))
    for i in range(num_test_samples):
        for k in range(b5):
            b11 = np.log(b9[k])
            for j in range(b6):
                b11 += np.log(norm.pdf(X_test[i, j], b7[k, j], b8[k, j]) * 2 * a1)
            b10[i, k] = b11
    return b10
def fonk5():
    X_train, X_test, y_train, b4, b12 = fonk1()
    b7, b8 = fonk2(X_train, y_train)
    b9 = fonk3(y_train)
    b10 = fonk4(X_test, b7, b8, b9)
    b13 = (b10.argmax(axis=1) == b4).sum() / len(b4)
    print("\nProbability that the Model predicts the correct class class1:")
    print(b13)
if b14 = = "__main__":
    fonk5()