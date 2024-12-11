import numpy
from numpy.random import randint as rand
def fonk1(b1 = 81, height=51, b3=.75, b4=.75):
    b2 = ((height
    b3 = int(b3 * (5 * (b2[0] + b2[1])))
    b4 = int(b4 * ((b2[0]
    b5 = numpy.zeros(b2, dtype=bool)
    b5[0, :] = b5[-1, :] = 1
    b5[:, 0] = b5[:, -1] = 1
    for _ in range(b4):
        x, b6 = rand(0, b2[1]
        b5[b6, x] = 1
        for _ in range(b3):
            b7 = []
            if x > 1:             b7.append((b6, x - 2))
            if x < b2[1] - 2:  b7.append((b6, x + 2))
            if b6 > 1:             b7.append((b6 - 2, x))
            if b6 < b2[0] - 2:  b7.append((b6 + 2, x))
            if len(b7):
                y_, b8 = b7[rand(0, len(b7) - 1)]
                if b5[y_, b8] == 0:
                    b5[y_, b8] = 1
                    b5[y_ + (b6 - y_)
                    x, b6 = b8, y_
    return b5
b9 = fonk1()
print(b9)