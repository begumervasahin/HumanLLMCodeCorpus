import numpy as np
def fonk1(b5):
    if len(b5) == 0:
        return np.array([])
    b1 = np.empty((0, b5[0].size), dtype=b5[0].dtype)
    for row in b5:
        b1 = np.vstack((b1, np.asarray(row).reshape(1, -1)))
    return b1
def fonk2(b5):
    if len(b5) == 0:
        return np.array([])
    b1 = np.empty((b5[0].size, 0), dtype=b5[0].dtype)
    for col in b5:
        b1 = np.hstack((b1, np.asarray(col).reshape(-1, 1)))
    return b1
def fonk3(b5, b2 = 0):
    n, b3 = b5.shape
    if b2 <= 0 or b2 > n:
        b2 = n
    b4 = b5.mean(axis=0)
    b5 = b5 - b4
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
def fonk4(W, b5, b4 = None):
    if b4 is None:
        return np.dot(b5, W)
    return np.dot(b5 - b4, W)
def fonk5(W, Y, b4 = None):
    if b4 is None:
        return np.dot(Y, W.T)
    return np.dot(Y, W.T) + b4