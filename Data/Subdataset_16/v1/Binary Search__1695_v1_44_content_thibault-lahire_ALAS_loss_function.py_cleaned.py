import numpy as np
def fonk1(w):
    return 1 / (1 + np.exp(-w))
def fonk2(w):
    b1 = np.exp(-w)
    if b1 < 10**16:
        if b1 > 10**-16:
            return b1 / ((1 + b1) ** 2)
        else:
            return b1
    else:
        return np.exp(w)
def fonk3(w):
    b1 = np.exp(-w)
    if b1 < 10**16:
        if b1 > 10**-16:
            b2 = np.exp(w)
            return -b2 * (b2 - 1) / ((1 + b2) ** 3)
        else:
            return -b1
    else:
        return np.exp(w)
def fonk4(x, S, A, y, b3 = 1, penalization=False):
    b4 = A.shape[1]
    b5 = len(S)
    a1 = 0
    if b3 >= 2:
        b6 = np.zeros(b4)
    if b3 = = 3:
        b7 = np.zeros((b4, b4))
    for i in range(b5):
        b8 = y[S[i]]
        b9 = A[S[i]]
        b10 = np.dot(x, b9)
        a1 += (b8 - fonk1(b10)) ** 2
        if b3 >= 2:
            b6 += 2 * b9 * fonk2(b10) * (fonk1(b10) - b8)
        if b3 = = 3:
            b7 += 2 * ((fonk1(b10) - b8) * fonk3(b10) +
                      fonk2(b10) ** 2) * np.outer(b9, b9)
    if penalization:
        a1 += 0.5 * np.linalg.norm(x) ** 2
    a1 /= b5
    if b3 = = 3:
        b7 = 0.5 * (b7 + b7.T)
        if penalization:
            b6 += x
            b7 += np.eye(b4)
        b6 /= b5
        b7 /= b5
        return a1, b6, b7
    elif b3 = = 2:
        if penalization:
            b6 += x
        b6 /= b5
        return a1, b6
    else:
        return a1
