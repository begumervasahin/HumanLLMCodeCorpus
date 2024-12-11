import itertools
import numpy as np
def fonk1(x):
    if 0 in x:
        b1 = [list(group) for key, group in itertools.groupby(x) if key == 0]
        b2 = max(len(group) for group in b1)
        b3 = x.count(0)
        b4 = 1 - b2 / b3
    else:
        b4 = 0
    return b4
def fonk2(lyst):
    b5 = len(lyst) - 1
    b6 = []
    for i in range(b5):
        if lyst[i] + lyst[i + 1] == 0:
            b6.extend([i, i + 1])
    b7 = np.array(b6).reshape(-1, 2)
    b8 = []
    for pair in b7:
        b9 = lyst[:]
        b9[pair[0]], b9[pair[1]] = 1, 1
        b4 = fonk1(b9)
        b8.append(b4)
        b9[pair[0]], b9[pair[1]] = 0, 0
    if len(b8) == 0:
        b10 = np.array([9, 9])
        a1 = 9
    else:
        a1 = min(b8)
        b11 = b8.index(min(b8))
        b10 = b7[b11]
    return b10, a1
if b12 = = '__main__':
    b13 = [0, 1, 0, 0, 0, 0]
    print(fonk2(b13))