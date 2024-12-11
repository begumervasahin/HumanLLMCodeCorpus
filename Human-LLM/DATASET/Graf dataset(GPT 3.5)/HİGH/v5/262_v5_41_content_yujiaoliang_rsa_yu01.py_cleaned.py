import numpy as np
import itertools
def fonk1(b11):
    if 0 in b11:
        b1 = [list(group) for value, group in itertools.groupby(b11) if value == 0]
        b2 = max(len(group) for group in b1)
        b3 = b11.count(0)
        b4 = 1 - b2 / b3
    else:
        b4 = 0
    return b4
def fonk2(b11):
    b5 = [(i, i + 1) for i in range(len(b11) - 1) if b11[i] + b11[i + 1] == 0]
    return np.array(b5)
def fonk3(b11, b5):
    b6 = []
    for pair in b5:
        b7 = b11.copy()
        b7[pair[0]], b7[pair[1]] = 1, 1
        b4 = fonk1(b7)
        b6.append(b4)
        b7[pair[0]], b7[pair[1]] = 0, 0
    if len(b6) == 0:
        a1 = 9
        b8 = np.array([9, 9])
    else:
        a1 = min(b6)
        b9 = b6.index(a1)
        b8 = b5[b9]
    return b8, a1
if b10 = = '__main__':
    b11 = [0, 1, 0, 0, 0, 0]
    b5 = fonk2(b11)
    print(fonk3(b11, b5)))