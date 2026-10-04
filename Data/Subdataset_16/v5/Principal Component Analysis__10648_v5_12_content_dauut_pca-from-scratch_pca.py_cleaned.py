import numpy as np
from numpy.linalg import eig
def fonk1(X, b1 = True, scaling=True):
    b2 = X.astype(float)
    if b1:
        b3 = b2.mean(axis=0)
        b2 -= b3
    if scaling:
        b4 = b2.std(axis=0, ddof=1)
        b2 /= b4
    return b2
def fonk2(b2):
    return np.cov(b2, b5 = False)
def fonk3(COV):
    b8, b6 = eig(COV)
    b7 = b8.argsort()[::-1]
    b8 = b8[b7]
    b6 = b6[:, b7]
    return b8, b6
def fonk4(b2, PCS, L, b9 = 0, var=0.0):
    if b9 > 0:
        b10 = PCS[:, :b9]
    else:
        a1 = 0
        a2 = 0
        for eigenvalue in L:
            a1 += eigenvalue / L.sum()
            a2 += 1
            if a1 >= var:
                break
        b10 = PCS[:, :a2]
    b11 = b2.dot(b10)
    return b11