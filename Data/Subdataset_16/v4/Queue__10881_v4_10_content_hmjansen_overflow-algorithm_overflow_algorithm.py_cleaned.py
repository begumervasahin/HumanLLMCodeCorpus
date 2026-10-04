
import copy
import numpy as np
import scipy.linalg as linalg
def fonk1(b10, alpha, mu, P, b1, b14, b12):
    alpha, mu, P, b1 = map(np.asarray, (alpha, mu, P, b1))
    b2 = np.b17((b10, b10))
    b3 = np.b17((b10, b10))
    for i in range(b10):
        if i in b14:
            b2[i, :] = P[i, :]
        if i in b12:
            b3[i, :] = b1[i, :]
    b4 = P - b2
    b5 = np.eye(b10)
    b6 = np.transpose(b5 - b2 - b3)
    b7 = np.transpose(alpha + mu @ (b4 - b3))
    b8 = linalg.solve(b6, b7)
    return b8.T
def fonk2(alpha, mu, P, b1, b9 = False):
    b10 = len(alpha)
    alpha, mu, P, b1 = map(np.asarray, (alpha, mu, P, b1))
    a1 = 0
    b11 = set(range(b10))
    b12 = set()
    b13 = copy.deepcopy(b11)
    while b12 != b13:
        b13 = copy.deepcopy(b12)
        b14 = set()
        b15 = copy.deepcopy(b11)
        while b14 != b15:
            b15 = copy.deepcopy(b14)
            b16 = fonk1(b10, alpha, mu, P, b1, b14, b12)
            b14 = {i for i in range(b10) if b16[i] < mu[i]}
            a1 += 1
        b12 = b11 - b14
    b17 = np.b17(b10)
    b18 = alpha + np.minimum(b16, mu) @ P + np.maximum(b16 - mu, b17) @ b1
    if not np.allclose(b16, b18):
        print("\nWarning: solution may be incorrect\b10")
    if b9:
        b19 = int(1 + (0.5 * b10 * (b10 + 1)))
        return b16, a1, b19
    else:
        return b16
