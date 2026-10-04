import numpy as np
from sklearn.model_selection import train_test_split
def fonk1(x, b1 = 'min_max_normalization'):
    if b1 = = 'standardization':
        return (x - np.mean(x)) / np.std(x)
    return (x - np.min(x)) / (np.max(x) - np.min(x))
def fonk2(b2, b3, b5):
    b2 = b2.reshape(-1, 1)
    b3 = b3.reshape(-1, 1)
    b4 = np.hstack((b2, b3))
    b5 = b5.reshape(-1, 1)
    X_train, X_temp, Y_train, b6 = train_test_split(b4, b5, test_size=0.2, random_state=0)
    X_test, X_val, Y_test, b7 = train_test_split(X_temp, b6, test_size=0.5, random_state=3)
    x1_train, b8 = X_train[:, 0], X_train[:, 1]
    x1_test, b9 = X_test[:, 0], X_test[:, 1]
    x1_val, b10 = X_val[:, 0], X_val[:, 1]
    return x1_train, x1_test, x1_val, b8, b9, b10, Y_train, Y_test, b7
def fonk3(b2, b3, a1):
    b2 = b2.reshape(-1, 1)
    b3 = b3.reshape(-1, 1)
    b11 = np.ones((b2.shape[0], 1))
    for d in range(1, a1 + 1):
        for i in range(d + 1):
            b12 = (b2 ** (d - i)) * (b3 ** i)
            b11 = np.hstack((b11, b12.reshape(-1, 1)))
    return b11
if b13 = = "__main__":
    b2 = np.array([1, 2, 3, 4, 5])
    b3 = np.array([2, 3, 4, 5, 6])
    b5 = np.array([3, 4, 5, 6, 7])
    b14 = fonk1(b2, b1='min_max_normalization')
    print("Normalized b2:", b14)
    x1_train, x1_test, x1_val, b8, b9, b10, Y_train, Y_test, b7 = fonk2(b2, b3, b5)
    print("x1_train:", x1_train)
    print("x1_test:", x1_test)
    print("x1_val:", x1_val)
    print("b8:", b8)
    print("b9:", b9)
    print("b10:", b10)
    print("Y_train:", Y_train)
    print("Y_test:", Y_test)
    print("b7:", b7)
    a1 = 2
    b11 = fonk3(b2, b3, a1)
    print("Feature Matrix:\n", b11)