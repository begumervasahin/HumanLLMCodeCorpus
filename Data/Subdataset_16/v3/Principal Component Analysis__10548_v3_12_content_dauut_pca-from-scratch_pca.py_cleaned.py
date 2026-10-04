import numpy as np
from numpy import linalg as LA
def fonk1(b10, b1 = True, scaling=True):
    b2 = b10.astype(float)
    if b1:
        b2 -= b2.mean(b3 = 0)
    if scaling:
        b2 /= b2.std(b3 = 0)
    return b2
def fonk2(b2):
    return b2.T @ b2
def fonk3(b11):
    eigenValues, b4 = LA.eig(b11)
    b5 = eigenValues.argsort()[::-1]
    return eigenValues[b5], b4[:, b5]
def fonk4(b2, PCS, L, b6 = 0, var=0):
    if b6 > 0:
        b7 = PCS[:, :b6]
    else:
        b8 = np.sum(L)
        a1 = 0
        a2 = 0
        for eigenvalue in L:
            a1 += eigenvalue
            a2 += 1
            if a1 / b8 >= var:
                break
        b7 = PCS[:, :a2]
    return b2 @ b7
if b9 = = "__main__":
    b10 = np.array([
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
    b2 = fonk1(b10, b1=True, scaling=True)
    b11 = fonk2(b2)
    eigenValues, b4 = fonk3(b11)
    b12 = fonk4(b2, b4, eigenValues, b6=1)
    print("Projected data:\n", b12)