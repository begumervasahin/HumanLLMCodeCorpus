import numpy as np
from numpy import linalg as LA
def fonk1(X, b1 = True, scaling=True):
    b2 = X.astype(float)
    b3 = b2.shape[0]
    b4 = b2.shape[1]
    if b1:
        b5 = X.mean(0)
        for i in range(b3):
            for j in range(b4):
                b2[i, j] = b2[i, j] - b5[j]
    if scaling:
        b6 = np.b6(b2, axis=0)
        for i in range(b4):
            for j in range(b3):
                b2[j][i] = b2[j][i] / b6[i]
    return b2
def fonk2(b2):
    return b2.T.dot(b2)
def fonk3(COV):
    b9, b7 = LA.eig(COV)
    b8 = b9.argsort()[::-1]
    b9 = b9[b8]
    b7 = b7[:, b8]
    return b9, b7
def fonk4(b2, PCS, L, k, var):
    b10 = [(np.abs(L[i]), PCS[:, i]) for i in range(len(L))]
    b10.sort(b11 = lambda x: x[0], reverse=True)
    b12 = np.copy(PCS)
    if k != 0:
        b12 = np.delete(b12, range(k, b12.shape[1]), axis=1)
        b13 = b2.dot(b12)
    else:
        print()
        a1 = 0
        a2 = 0
        while a1 < var:
            a1 = a1 + L[a2] / np.sum(L)
            a2 = a2 + 1
        b14 = a2
        b12 = np.delete(b12, range(b14, b12.shape[1]), axis=1)
        b13 = b2.dot(b12)
    return b13