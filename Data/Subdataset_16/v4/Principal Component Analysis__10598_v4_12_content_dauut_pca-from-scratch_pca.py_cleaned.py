import numpy as np
from numpy.linalg import eig
def fonk1(X, b1 = True, scaling=True):
    b2 = X.astype(float)
    rows, b3 = b2.shape
    if b1:
        b4 = X.mean(axis=0)
        b2 -= b4
    if scaling:
        b5 = np.std(b2, axis=0)
        b2 /= b5
    return b2
def fonk2(b2):
    return b2.T.dot(b2) / (b2.shape[0] - 1)
def fonk3(COV):
    b8, b6 = eig(COV)
    b7 = b8.argsort()[::-1]
    b8 = b8[b7]
    b6 = b6[:, b7]
    return b8, b6
def fonk4(b2, PCS, L, b9 = 0, var=0.0):
    if b9 != 0:
        b10 = PCS[:, :b9]
    else:
        a1 = 0
        a2 = 0
        while a1 < var and a2 < len(L):
            a1 += L[a2] / np.sum(L)
            a2 += 1
        b10 = PCS[:, :a2]
    b11 = b2.dot(b10)
    return b11