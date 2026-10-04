import numpy as np
def fonk1(w):
    return 1 / (1 + np.exp(-w))
def fonk2(w):
    b1 = np.exp(-w)
    if b1 < 1e16:
        if b1 > 1e-16:
            return b1 / (1 + b1) ** 2
        else:
            return b1
    else:
        return np.exp(w)
def fonk3(w):
    b1 = np.exp(-w)
    if b1 < 1e16:
        if b1 > 1e-16:
            b2 = np.exp(w)
            return -b2 * (b2 - 1) / (1 + b2) ** 3
        else:
            return -b1
    else:
        return np.exp(w)
def fonk4(x, S, A, y, b3 = 1, penalize=False):
    b4 = A.shape[1]
    b5 = len(S)
    a1 = 0
    b6 = np.zeros(b4) if b3 >= 2 else None
    b7 = np.zeros((b4, b4)) if b3 == 3 else None
    for i in S:
        b8 = y[i]
        b9 = A[i]
        b10 = np.dot(x, b9)
        b11 = fonk1(b10)
        a1 += (b8 - b11) ** 2
        if b3 >= 2:
            b12 = fonk2(b10)
            b6 += 2 * b9 * b12 * (b11 - b8)
        if b3 = = 3:
            b13 = fonk3(b10)
            b7 += 2 * (
                (b11 - b8) * b13 +
                b12 ** 2
            ) * np.outer(b9, b9)
    if penalize:
        a1 += 0.5 * np.linalg.norm(x) ** 2
    a1 /= b5
    if b3 = = 3:
        b7 = 0.5 * (b7 + b7.T)
        if penalize:
            b6 += x
            b7 += np.eye(b4)
        b6 /= b5
        b7 /= b5
        return a1, b6, b7
    elif b3 = = 2:
        if penalize:
            b6 += x
        b6 /= b5
        return a1, b6
    else:
        return a1
