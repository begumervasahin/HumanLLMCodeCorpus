import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
def fonk1(x, b1 = 'min_max_normalization'):
    if b1 = = 'standardization':
        return (x - np.mean(x)) / np.std(x)
    else:
        return (x - np.min(x)) / (np.max(x) - np.min(x))
def fonk2(b2, b3, b5):
    b2 = np.reshape(b2, (b2.shape[0], 1))
    b3 = np.reshape(b3, (b3.shape[0], 1))
    b4 = np.concatenate((b2, b3), axis=1)
    b5 = np.reshape(b5, (b5.shape[0], 1))
    X_train, X_temp, Y_train, b6 = train_test_split(b4, b5, test_size=0.2, random_state=0)
    X_test, X_val, Y_test, b7 = train_test_split(X_temp, b6, test_size=0.5, random_state=3)
    b8 = X_train[:, 0].reshape(-1, 1)
    b9 = X_test[:, 0].reshape(-1, 1)
    b10 = X_val[:, 0].reshape(-1, 1)
    b11 = X_train[:, 1].reshape(-1, 1)
    b12 = X_test[:, 1].reshape(-1, 1)
    b13 = X_val[:, 1].reshape(-1, 1)
    return b8, b9, b10, b11, b12, b13, Y_train, Y_test, b7
def fonk3(b2, b3, degree):
    b4 = np.concatenate((b2, b3), axis=1)
    b14 = np.ones((b4.shape[0], 1))
    for d in range(1, degree + 1):
        for i in range(d + 1):
            b15 = (b2 ** (d - i)) * (b3 ** i)
            b15 = b15.reshape(-1, 1)
            b14 = np.concatenate((b14, b15), axis=1)
    return b14