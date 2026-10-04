import numpy as np
from itertools import combinations
from math import acos, sqrt, pi, cos, sin
class class1:
    @staticmethod
    def fonk1(mat):
        return (mat + mat.T) / 2
def fonk2(b16):
    b1 = np.matmul(b16.T, b16)
    return np.reshape(b1, -1)
def fonk3(b17, b4):
    b2 = class1.fonk1(np.reshape(b17, (b4, b4)))
    b3 = -b2[b4 - 1]
    return b3
def fonk4(b3):
    b1 = np.outer(b3, b3)
    return np.reshape(b1, -1)
def fonk5(b3):
    b4 = len(b3)
    b5 = np.zeros(b4 - 1)
    b6 = b3[-1]**2 + b3[-2]**2
    b7 = acos(b3[-2] / sqrt(b6))
    b5[-1] = b7 if b3[-1] >= 0 else 2 * pi - b7
    for k in range(b4 - 3, -1, -1):
        b6 += b3[k]**2
        b5[k] = acos(b3[k] / sqrt(b6))
    return b5
def fonk6(b5):
    b8 = len(b5)
    b3 = np.zeros(b8 + 1)
    a1 = 1
    for i in range(b8):
        b3[i] = a1 * cos(b5[i])
        a1 *= sin(b5[i])
    b3[b8] = a1
    return b3
def fonk7(b16, j):
    b4 = b16.shape[1]
    b9 = np.array([])
    b10 = np.reshape(b16 * b16, (1, b16.size))
    b9 = np.append(b9, b10)
    b11 = range(b4 + 1)
    b12 = list(combinations(b11, 2))
    for i in range(b4 - j):
        b13 = 2 * b16[i, [b3[0] for b3 in b12]] * b16[i, [b3[1] for b3 in b12]]
        b9 = np.append(b9, b13)
    return b9
def fonk8(b17, b4, j):
    b14 = np.sqrt(np.abs(b17[:b4]))
    b15 = b17[b4 * (b4 - j):b4 * (b4 - j) + b4 - 1]
    b3 = np.zeros(b4)
    b3[0] = np.abs(b14[0])
    for i in range(1, len(b14)):
        b3[i] = -np.abs(b14[i]) if b15[i - 1] < 0 else np.abs(b14[i])
    return b3
def fonk9():
    b16 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    b9 = fonk2(b16)
    print("pComp:", b9)
    b17 = b9
    b4 = 3
    b3 = fonk3(b17, b4)
    print("qDecomp:", b3)
    b18 = np.array([1, 2, 3])
    b5 = fonk5(b18)
    print("cartesianToSpherical:", b5)
    b19 = fonk6(b5)
    print("sphericalToCartesian:", b19)
    b20 = fonk7(b16, 1)
    print("pCompAlt:", b20)
    b21 = fonk8(b20, b4, 1)
    print("qDecompAlt:", b21)
if b22 = = "__main__":
    fonk9()