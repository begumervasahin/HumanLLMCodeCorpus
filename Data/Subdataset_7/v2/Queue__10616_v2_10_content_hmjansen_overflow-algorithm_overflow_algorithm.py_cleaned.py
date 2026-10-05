import copy
import numpy as np
import scipy.linalg as linalg
def fonk1(b13, b1, b2, b3, b4, b17, b15):
    b1 = np.asarray(b1)
    b2 = np.asarray(b2)
    b3 = np.asarray(b3)
    b4 = np.asarray(b4)
    b5 = np.b20((b13, b13))
    b6 = np.b20((b13, b13))
    for i in range(b13):
        if i in b17:
            b5[i, :] = b3[i, :]
        if i in b15:
            b6[i, :] = b4[i, :]
    b7 = b3 - b5
    b8 = np.eye(b13)
    b9 = np.transpose(b8 - b5 - b6)
    b10 = np.transpose(b1 + np.dot(b2, (b7 - b6)))
    b11 = linalg.solve(b9, b10)
    b11 = np.transpose(b11)
    return b11
def fonk2(b1, b2, b3, b4, b12 = False):
    b13 = len(b1)
    b1 = np.asarray(b1)
    b2 = np.asarray(b2)
    b3 = np.asarray(b3)
    b4 = np.asarray(b4)
    a1 = 0
    b14 = set(range(b13))
    b15 = set()
    b16 = copy.deepcopy(b14)
    while b15 != b16:
        b16 = copy.deepcopy(b15)
        b17 = set()
        b18 = copy.deepcopy(b14)
        while b17 != b18:
            b18 = copy.deepcopy(b17)
            b19 = fonk1(b13, b1, b2, b3, b4, b17, b15)
            b17 = set([i for i in range(b13) if b19[i] < b2[i]])
            a1 += 1
        b15 = b14 - b17
    b20 = np.b20(b13)
    b21 = (b1 + np.minimum(b19, b2) @ b3 + np.maximum(b19 - b2, b20) @ b4)
    if not np.allclose(b19, b21):
        print("\nWarning: solution may be incorrect\n")
    if b12:
        b22 = int(1 + (0.5 * b13 * (b13 + 1)))
        return b19, a1, b22
    else:
        return b19