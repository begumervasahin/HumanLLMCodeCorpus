from skimage import io
import math
import numpy as np
import os
def fonk1(path):
    b1 = os.listdir(path)
    b2 = []
    b3 = []
    a1 = 0
    a2 = 0
    a3 = 0
    for i in range(len(b1)):
        b4 = os.path.join(path, b1[i])
        b5 = io.imread(b4, as_grey=True)
        b6 = len(b5)
        b7 = len(b5[0])
        a4 = 0
        a5 = 0
        for c in range(b6):
            for n in range(b7):
                a4 += b5[c][n]
        b8 = a4 / (b6 * b7)
        b2.append(b8)
        for a in range(b6):
            for b in range(b7):
                a5 += (b5[a][b] - b8) ** 2
        b9 = math.sqrt(a5 / (b6 * b7))
        b3.append(b9)
    for k in range(len(b1)):
        a1 += b2[k]
        a2 += b3[k]
    b10 = a1 / len(b1)
    b11 = a2 / len(b1)
    b12 = np.array([b10, b11])
    for p in range(len(b1)):
        b13 = math.sqrt((b2[p] - b10) ** 2 + (b3[p] - b11) ** 2)
        a3 += b13
    b14 = a3 / len(b1)
    return b12, b14