import numpy as np
def fonk1(X):
    if len(X) == 0:
        return np.array([])
    b1 = np.empty((0, X[0].size), dtype=X[0].dtype)
    for row in X:
        b1 = np.vstack((b1, np.asarray(row).reshape(1, -1)))
    return b1
def fonk2(X):
    if len(X) == 0:
        return np.array([])
    b1 = np.empty((X[0].size, 0), dtype=X[0].dtype)
    for col in X:
        b1 = np.hstack((b1, np.asarray(col).reshape(-1, 1)))
    return b1
def fonk3(X, b2 = 0):
    n, b3 = X.shape
    if b2 <= 0 or b2 > n:
        b2 = n
    b4 = X.mean(axis=0)
    b5 = X - b4
    if n > b3:
        b6 = np.dot(b5.T, b5)
        b9, b7 = np.linalg.eigh(b6)
    else:
        b6 = np.dot(b5, b5.T)
        b9, b7 = np.linalg.eigh(b6)
        b7 = np.dot(b5.T, b7)
    b7 = np.apply_along_axis(lambda v: v / np.linalg.norm(v), 0, b7)
    b8 = np.argsort(-b9)
    b9 = b9[b8]
    b7 = b7[:, b8]
    b9 = b9[:b2].copy()
    b7 = b7[:, :b2].copy()
    return b9, b7, b4
def fonk4(W, X, b4 = None):
    if b4 is None:
        return np.dot(X, W)
    return np.dot(X - b4, W)
def fonk5(W, Y, b4 = None):
    if b4 is None:
        return np.dot(Y, W.T)
    return np.dot(Y, W.T) + b4