import numpy as np
def fonk1(w):
    return 1 / (1 + np.exp(-w))
def fonk2(w):
    b1 = np.exp(-w)
    if b1 < 1e16:
        if b1 > 1e-16:
            return b1 / ((1 + b1) ** 2)
        else:
            return b1
    else:
        return np.exp(w)
def fonk3(w):
    b1 = np.exp(-w)
    if b1 < 1e16:
        if b1 > 1e-16:
            return -np.exp(w) * (np.exp(w) - 1) / ((1 + np.exp(w)) ** 3)
        else:
            return -b1
    else:
        return np.exp(w)
def fonk4(x, S, A, y, b2 = 1, penalization=False):
    b3 = A.shape[1]
    b4 = len(S)
    a1 = 0
    b5 = np.zeros(b3) if b2 >= 2 else None
    b6 = np.zeros((b3, b3)) if b2 == 3 else None
    for i in range(b4):
        b7 = y[S[i]]
        b8 = A[S[i]]
        b9 = np.dot(x, b8)
        b10 = fonk1(b9)
        a1 += (b7 - b10) ** 2
        if b2 >= 2:
            b11 = fonk2(b9)
            b5 += 2 * b8 * b11 * (b10 - b7)
        if b2 = = 3:
            b12 = fonk3(b9)
            b6 += 2 * ((b10 - b7) * b12 + \
                            b11 ** 2) * np.outer(b8, b8)
    if penalization:
        a1 += 0.5 * np.linalg.norm(x) ** 2
    a1 /= b4
    if b2 >= 2:
        if penalization:
            b5 += x
        b5 /= b4
    if b2 = = 3:
        b6 = (b6 + b6.T) / (2 * b4)
        if penalization:
            b6 += np.eye(b3) / b4
    if b2 = = 3:
        return a1, b5, b6
    elif b2 = = 2:
        return a1, b5
    else:
        return a1