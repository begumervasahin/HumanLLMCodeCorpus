import numpy as np
from numpy import linalg as LA
def fonk1(b14, b1 = True, scaling=True):
    b2 = b14.astype(float)
    rows, b3 = b2.shape
    if b1:
        b4 = b14.mean(axis=0)
        b2 -= b4
    if scaling:
        b5 = np.b5(b2, axis=0)
        b2 /= b5
    return b2
def fonk2(b2):
    return b2.T @ b2
def fonk3(b15):
    b8, b6 = LA.eig(b15)
    b7 = b8.argsort()[::-1]
    b8 = b8[b7]
    b6 = b6[:, b7]
    return b8, b6
def fonk4(b2, PCS, L, b9 = 0, var=0):
    if b9 != 0:
        b10 = PCS[:, :b9]
    else:
        b11 = np.sum(L)
        a1 = 0
        a2 = 0
        for eigenvalue in L:
            a1 += eigenvalue
            a2 += 1
            if a1 / b11 >= var:
                break
        b10 = PCS[:, :a2]
    b12 = b2 @ b10
    return b12
if b13 = = "__main__":
    b14 = np.array([
        [2.5, 2.4],
        [0.5, 0.7],
        [2.2, 2.9],
        [1.9, 2.2],
        [3.1, 3.0],
        [2.3, 2.7],
        [2.0, 1.6],
        [1.0, 1.1],
        [1.5, 1.6],
        [1.1, 0.9]
    ])
    b2 = fonk1(b14, b1=True, scaling=True)
    b15 = fonk2(b2)
    b8, b6 = fonk3(b15)
    b12 = fonk4(b2, b6, b8, b9=1)
    print("Projected data:\n", b12)