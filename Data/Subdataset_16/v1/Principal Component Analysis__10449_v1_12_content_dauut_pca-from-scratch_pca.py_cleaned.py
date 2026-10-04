import numpy as np
from numpy import linalg as LA
def fonk1(b17, b1 = True, scaling=True):
    b2 = b17.astype(float)
    b3 = b2.shape[0]
    b4 = b2.shape[1]
    if b1:
        b5 = b17.mean(0)
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
def fonk3(b18):
    b9, b7 = LA.eig(b18)
    b8 = b9.argsort()[::-1]
    b9 = b9[b8]
    b7 = b7[:, b8]
    return b9, b7
def fonk4(b2, PCS, L, b10 = 0, var=0):
    b11 = [(np.abs(L[i]), PCS[:, i]) for i in range(len(L))]
    b11.sort(b12 = lambda x: x[0], reverse=True)
    b13 = np.copy(PCS)
    if b10 != 0:
        b13 = np.delete(b13, range(b10, b13.shape[1]), axis=1)
        b14 = b2.dot(b13)
    else:
        a1 = 0
        a2 = 0
        while a1 < var:
            a1 = a1 + L[a2] / np.sum(L)
            a2 = a2 + 1
        b15 = a2
        b13 = np.delete(b13, range(b15, b13.shape[1]), axis=1)
        b14 = b2.dot(b13)
    return b14
if b16 = = "__main__":
    b17 = np.array([[2.5, 2.4],
                  [0.5, 0.7],
                  [2.2, 2.9],
                  [1.9, 2.2],
                  [3.1, 3.0],
                  [2.3, 2.7],
                  [2.0, 1.6],
                  [1.0, 1.1],
                  [1.5, 1.6],
                  [1.1, 0.9]])
    b2 = fonk1(b17, b1=True, scaling=True)
    b18 = fonk2(b2)
    b9, b7 = fonk3(b18)
    b14 = fonk4(b2, b7, b9, b10=1)
    print("Projected data:\n", b14)