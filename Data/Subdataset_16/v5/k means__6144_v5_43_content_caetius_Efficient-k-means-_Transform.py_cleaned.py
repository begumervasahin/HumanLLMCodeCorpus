import numpy as np
from itertools import combinations
from math import acos, sqrt, pow, pi, cos, sin
import Matrix
def fonk1(A):
    b1 = np.matmul(A.transpose(), A)
    return np.reshape(b1, -1)
def fonk2(q, b5):
    b2 = np.reshape(q, (b5, b5))
    b3 = Matrix.getClosestSymMatrix(b2)
    b4 = -b3[b5 - 1]
    return b4
def fonk3(b4):
    b1 = np.outer(b4, b4)
    return np.reshape(b1, -1)
def fonk4(b4):
    b5 = len(b4)
    b6 = np.zeros(b5 - 1)
    b7 = pow(b4[b5 - 1], 2) + pow(b4[b5 - 2], 2)
    b8 = acos(b4[b5 - 2] / sqrt(b7))
    if b4[b5 - 1] >= 0:
        b6[b5 - 2] = b8
    else:
        b6[b5 - 2] = 2 * pi - b8
    for k in range(b5 - 3, -1, -1):
        b7 += pow(b4[k], 2)
        b6[k] = acos(b4[k] / sqrt(b7))
    return b6
def fonk5(b6):
    b9 = len(b6)
    b4 = np.zeros(b9 + 1)
    a1 = 1
    for i in range(b9):
        b4[i] = a1 * cos(b6[i])
        a1 *= sin(b6[i])
    b4[b9] = a1
    return b4
def fonk6(A, j):
    b5 = len(A[0, :])
    b10 = np.array([])
    b11 = np.reshape(np.multiply(A, A), (1, A.shape[0] * A.shape[1]))
    b10 = np.append(b10, b11)
    b12 = range(b5 + 1)
    b13 = list(combinations(b12, 2))
    for i in range(b5 - j):
        b14 = 2 * np.multiply(A[i, [b4[0] for b4 in b13]], A[i, [b4[1] for b4 in b13]])
        b10 = np.append(b10, b14)
    return b10
def fonk7(q, b5, j):
    b15 = np.sqrt(np.abs(q[:b5]))
    b16 = q[b5 * (b5 - j):b5 * (b5 - j) + b5 - 1]
    b4 = np.zeros(b5)
    b4[0] = np.abs(b15[0])
    for i in range(1, len(b15)):
        b4[i] = -np.abs(b15[i]) if b16[i - 1] < 0 else np.abs(b15[i])
    return b4