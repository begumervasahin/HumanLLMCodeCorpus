import scipy.io as sio
import numpy as np
import itertools
def fonk1(b12):
    if 0 in b12:
        b1 = max([len(list(group)) for value, group in itertools.groupby(b12) if value == 0])
        b2 = b12.count(0)
        b3 = 1 - b1 / b2
    else:
        b3 = 0
    return b3
def fonk2(b12):
    b4 = len(b12) - 1
    b5 = []
    for i in range(b4):
        if b12[i] + b12[i + 1] == 0:
            b5.append(i)
            b5.append(i + 1)
    b6 = np.array(b5).reshape(-1, 2)
    return b6
def fonk3(b12, b5):
    b7 = []
    for pair in b5:
        b8 = b12.copy()
        b8[pair[0]], b8[pair[1]] = 1, 1
        b3 = fonk1(b8)
        b7.append(b3)
        b8[pair[0]], b8[pair[1]] = 0, 0
    if len(b7) == 0:
        a1 = 9
        b9 = np.array([9, 9])
    else:
        a1 = min(b7)
        b10 = b7.index(a1)
        b9 = b5[b10]
    return b9, a1
if b11 = = '__main__':
    b12 = [0, 1, 0, 0, 0, 0]
    b5 = fonk2(b12)
    print(fonk3(b12, b5))