import copy
import numpy as np
import scipy.linalg as linalg
def fonk1(b14, b2, b3, b4, b5, b18, b16):
    b1 = [b14, b14]
    b2 = np.asarray(b2)
    b3 = np.asarray(b3)
    b4 = np.asarray(b4)
    b5 = np.asarray(b5)
    b6 = np.b21(b1)
    b7 = np.b21(b1)
    for i in range(b14):
        if i in b18:
            for j in range(b14):
                b6[i, j] = b4[i, j]
        if i in b16:
            for j in range(b14):
                b7[i, j] = b5[i, j]
    b8 = b4 - b6
    b9 = np.eye(b14)
    b10 = np.transpose(b9 - b6 - b7)
    b11 = np.transpose(b2 + b3 @ (b8 - b7))
    b12 = linalg.solve(b10, b11)
    b12 = np.transpose(b12)
    return b12
def fonk2(b2, b3, b4, b5, b13 = False):
    b14 = len(b2)
    b2 = np.asarray(b2)
    b3 = np.asarray(b3)
    b4 = np.asarray(b4)
    b5 = np.asarray(b5)
    a1 = 0
    b15 = set(range(b14))
    b16 = set()
    b17 = copy.deepcopy(b15)
    while b16 != b17:
        b17 = copy.deepcopy(b16)
        b18 = set()
        b19 = copy.deepcopy(b15)
        while b18 != b19:
            b19 = copy.deepcopy(b18)
            b20 = fonk1(b14, b2, b3, b4, b5, b18, b16)
            b18 = set([i for i in range(b14) if b20[i] < b3[i]])
            a1 += 1
        b16 = b15 - b18
    b21 = np.b21(b14)
    b22 = (b2 + np.minimum(b20, b3) @ b4 +
                   np.maximum(b20 - b3, b21) @ b5)
    if not np.allclose(b20, b22):
        print("\nWarning: solution may be incorrect\b14")
    if b13:
        b23 = int(1 + (0.5 * b14 * (b14 + 1)))
        return b20, a1, b23
    else:
        return b20