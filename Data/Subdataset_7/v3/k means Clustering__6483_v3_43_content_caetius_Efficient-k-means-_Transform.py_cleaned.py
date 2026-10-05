import numpy as np
from itertools import combinations
from math import acos, sqrt, pi, cos, sin
def fonk1(b17):
    b1 = np.matmul(b17.transpose(), b17)
    return b1.flatten()
def fonk2(b19, b4):
    b2 = np.outer(b19, b19)
    b2 = fonk8(b2)
    b3 = -b2[:, b4 - 1]
    return b3
def fonk3(b3):
    b1 = np.outer(b3, b3)
    return b1.flatten()
def fonk4(b3):
    b4 = len(b3)
    b5 = np.zeros((b4 - 1))
    b6 = pow(b3[-1], 2) + pow(b3[-2], 2)
    b7 = acos(b3[-2] / sqrt(b6))
    b5[-1] = b7 if b3[-1] >= 0 else 2 * pi - b7
    for k in range(b4 - 3, -1, -1):
        b6 += pow(b3[k], 2)
        b5[k] = acos(b3[k] / sqrt(b6))
    return b5
def fonk5(b5):
    b8 = len(b5)
    b3 = np.zeros(b8 + 1)
    a1 = 1
    for i in range(b8):
        b3[i] = a1 * cos(b5[i])
        a1 *= sin(b5[i])
    b3[-1] = a1
    return b3
def fonk6(b17, j):
    b4 = len(b17[0])
    b9 = np.array([])
    b10 = np.multiply(b17, b17).reshape(1, -1)
    b9 = np.append(b9, b10)
    b11 = range(b4 + 1)
    b12 = list(combinations(b11, 2))
    for i in range(b4 - j):
        b13 = 2 * np.multiply(b17[i, [b3[0] for b3 in b12]], b17[i, [b3[1] for b3 in b12]])
        b9 = np.append(b9, b13)
    return b9
def fonk7(b19, b4, j):
    b14 = np.sqrt(np.abs(b19[:b4]))
    b15 = b19[b4 * (b4 - j):b4 * (b4 - j) + b4 - 1]
    b3 = np.zeros(b4)
    b3[0] = np.absolute(b14[0])
    for i in range(1, len(b14)):
        b3[i] = -np.absolute(b14[i]) if b15[i - 1] < 0 else np.absolute(b14[i])
    return b3
def fonk8(b17):
    return (b17 + b17.T) / 2
if b16 = = "__main__":
    b17 = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])
    b18 = fonk1(b17)
    print("Projection result:")
    print(b18)
    b19 = np.array([1, 2, 3])
    a2 = 3
    b20 = fonk2(b19, a2)
    print("\nDecomposition result:")
    print(b20)
    b21 = fonk3(b20)
    print("\nComposition result:")
    print(b21)
    b3 = np.array([1, 2, 3])
    b22 = fonk4(b3)
    print("\nSpherical coordinates:")
    print(b22)
    b23 = fonk5(b22)
    print("\nCartesian coordinates:")
    print(b23)
    b24 = fonk6(b17, 1)
    print("\nAlternative projection result:")
    print(b24)
    b25 = fonk7(b21, a2, 1)
    print("\nAlternative decomposition result:")
    print(b25)