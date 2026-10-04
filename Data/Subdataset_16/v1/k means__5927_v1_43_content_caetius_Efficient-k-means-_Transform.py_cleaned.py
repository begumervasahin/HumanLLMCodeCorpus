import numpy as np
from itertools import combinations
from math import acos, sqrt, pow, pi, cos, sin
class class1:
    @staticmethod
    def fonk1(mat):
        return (mat + mat.T) / 2
def fonk2(b17):
    b1 = np.matmul(b17.transpose(), b17)
    return np.reshape(b1, -1)
def fonk3(b18, b4):
    b2 = class1.fonk1(np.reshape(b18, (b4, b4)))
    b3 = -b2[b4 - 1]
    return b3
def fonk4(b3):
    b1 = np.outer(b3, b3)
    return np.reshape(b1, -1)
def fonk5(b3):
    b4 = len(b3)
    b5 = np.zeros(b4-1)
    b6 = len(b5)
    b7 = pow(b3[b6], 2) + pow(b3[b6-1], 2)
    b8 = acos(b3[b6-1] / sqrt(b7))
    if b3[b6] >= 0:
        b5[b6-1] = b8
    else:
        b5[b6-1] = 2 * pi - b8
    for k in range(b6-2, -1, -1):
        b7 = b7 + pow(b3[k], 2)
        b5[k] = acos(b3[k] / sqrt(b7))
    return b5
def fonk6(b5):
    b9 = len(b5)
    b3 = np.zeros(b9 + 1)
    a1 = 1
    for i in range(b9):
        b3[i] = a1 * cos(b5[i])
        a1 *= sin(b5[i])
    b3[b9] = a1
    return b3
def fonk7(b17, j):
    b4 = len(b17[0, :])
    b10 = np.array([])
    b11 = np.reshape(np.multiply(b17, b17), (1, b17.shape[0] * b17.shape[1]))
    b10 = np.append(b10, b11)
    b12 = range(b4 + 1)
    b13 = list(combinations(b12, 2))
    for i in range(b4 - j):
        b14 = 2 * np.multiply(b17[i, [b3[0] for b3 in b13]], b17[i, [b3[1] for b3 in b13]])
        b10 = np.append(b10, b14)
    return b10
def fonk8(b18, b4, j):
    b15 = np.sqrt(np.abs(b18[0:b4]))
    b16 = b18[b4 * (b4 - j):b4 * (b4 - j) + b4 - 1]
    b3 = np.zeros(b4)
    b3[0] = np.absolute(b15[0])
    for i in range(1, len(b15)):
        if b16[i - 1] < 0:
            b3[i] = -np.absolute(b15[i])
        else:
            b3[i] = np.absolute(b15[i])
    return b3
b17 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b10 = fonk2(b17)
print("pComp:", b10)
b18 = b10
b4 = 3
b3 = fonk3(b18, b4)
print("qDecomp:", b3)
b19 = np.array([1, 2, 3])
b5 = fonk5(b19)
print("cartesianToSpherical:", b5)
b20 = fonk6(b5)
print("sphericalToCartesian:", b20)
b21 = fonk7(b17, 1)
print("pCompAlt:", b21)
b22 = fonk8(b21, b4, 1)
print("qDecompAlt:", b22)