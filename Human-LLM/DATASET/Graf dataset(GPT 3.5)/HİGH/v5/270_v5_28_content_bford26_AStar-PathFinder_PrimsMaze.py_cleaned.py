import numpy as np
from numpy.random import randint
def fonk1(b5, b6):
    b1 = (b6, b5)
    b2 = np.zeros(b1, dtype=bool)
    b2[0, :] = b2[-1, :] = 1
    b2[:, 0] = b2[:, -1] = 1
    return b2
def fonk2(b2, start_x, start_y):
    b2[start_y, start_x] = 1
def fonk3(x, b9, b5, b6):
    b3 = []
    if x > 1:
        b3.append((b9, x - 2))
    if x < b5 - 2:
        b3.append((b9, x + 2))
    if b9 > 1:
        b3.append((b9 - 2, x))
    if b9 < b6 - 2:
        b3.append((b9 + 2, x))
    return b3
def fonk4(b2, x, b9, b3):
    y_, b4 = b3[randint(0, len(b3) - 1)]
    if b2[y_, b4] == 0:
        b2[y_, b4] = 1
        b2[y_ + (b9 - y_)
        return b4, y_
    return x, b9
def fonk5(b5 = 81, b6=51, b7=.75, b8=.75):
    b5 = (b5
    b6 = (b6
    b2 = fonk1(b5, b6)
    b7 = int(b7 * (5 * (b5 + b6)))
    b8 = int(b8 * ((b5
    for _ in range(b8):
        x, b9 = randint(0, b5
        fonk2(b2, x, b9)
        for _ in range(b7):
            b3 = fonk3(x, b9, b5, b6)
            if b3:
                x, b9 = fonk4(b2, x, b9, b3)
    return b2
b2 = fonk5()
print(b2)