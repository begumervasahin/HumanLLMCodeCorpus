import numpy as np
from itertools import combinations
from math import acos, sqrt, pow, pi, cos, sin
def fonk1(b17):
    b1 = np.matmul(b17.transpose(), b17)
    return np.reshape(b1, -1)
def fonk2(b19, b4):
    b2 = np.outer(b19, b19)
    b2 = fonk8(b2)
    b3 = -b2[:, b4 - 1]
    return b3
def fonk3(b3):
    b1 = np.outer(b3, b3)
    return np.reshape(b1, -1)
def fonk4(b3):
    b4 = len(b3)
    b5 = np.zeros((b4-1))
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
def fonk5(b5):
    b9 = len(b5)
    b3 = np.zeros(b9 + 1)
    a1 = 1
    for i in range(0, b9):
        b3[i] = a1 * cos(b5[i])
        a1 *= sin(b5[i])
    b3[b9] = a1
    return b3
def fonk6(b17, j):
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
def fonk7(b19, b4, j):
    b15 = np.sqrt(np.abs(b19[0:b4]))
    b16 = b19[b4 * (b4 - j):b4 * (b4 - j) + b4 - 1]
    b3 = np.zeros(b4)
    b3[0] = np.absolute(b15[0])
    for i in range(1, len(b15)):
        if b16[i - 1] < 0:
            b3[i] = -np.absolute(b15[i])
        else:
            b3[i] = np.absolute(b15[i])
    return b3
def fonk8(b17):
    return (b17 + b17.T) / 2
b17 = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
b18 = fonk1(b17)
print("pComp result:")
print(b18)
b19 = np.array([1, 2, 3])
a2 = 3
b20 = fonk2(b19, a2)
print("\nqDecomp result:")
print(b20)
b21 = fonk3(b20)
print("\nqComp result:")
print(b21)
b3 = np.array([1, 2, 3])
b22 = fonk4(b3)
print("\nSpherical coordinates:")
print(b22)
b23 = fonk5(b22)
print("\nCartesian coordinates:")
print(b23)
b24 = fonk6(b17, 1)
print("\npCompAlt result:")
print(b24)
b25 = fonk7(b21, a2, 1)
print("\nqDecompAlt result:")
print(b25)