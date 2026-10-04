import numpy as np
from itertools import combinations
from math import acos, sqrt, pow, pi, cos, sin
import Matrix
def fonk1(A):
    b1 = np.matmul(A.transpose(), A)
    return np.reshape(b1, -1)
def fonk2(q, b4):
    b2 = Matrix.getClosestSymMatrix(np.reshape(q, (b4, b4)))
    b3 = -b2[b4 - 1]
    return b3
def fonk3(b3):
    b1 = np.outer(b3, b3)
    return np.reshape(b1, -1)
def fonk4(b3):
    b4 = len(b3)
    b5 = np.zeros(b4 - 1)
    b6 = pow(b3[b4 - 1], 2) + pow(b3[b4 - 2], 2)
    b7 = acos(b3[b4 - 2] / sqrt(b6))
    if b3[b4 - 1] >= 0:
        b5[b4 - 2] = b7
    else:
        b5[b4 - 2] = 2 * pi - b7
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
    b3[b8] = a1
    return b3
def fonk6(A, j):
    b4 = len(A[0, :])
    b9 = np.array([])
    b10 = np.reshape(np.multiply(A, A), (1, A.shape[0] * A.shape[1]))
    b9 = np.append(b9, b10)
    b11 = range(b4 + 1)
    b12 = list(combinations(b11, 2))
    for i in range(b4 - j):
        b13 = 2 * np.multiply(A[i, [b3[0] for b3 in b12]], A[i, [b3[1] for b3 in b12]])
        b9 = np.append(b9, b13)
    return b9
def fonk7(q, b4, j):
    b14 = np.sqrt(np.abs(q[:b4]))
    b15 = q[b4 * (b4 - j):b4 * (b4 - j) + b4 - 1]
    b3 = np.zeros(b4)
    b3[0] = np.abs(b14[0])
    for i in range(1, len(b14)):
        b3[i] = -np.abs(b14[i]) if b15[i - 1] < 0 else np.abs(b14[i])
    return b3