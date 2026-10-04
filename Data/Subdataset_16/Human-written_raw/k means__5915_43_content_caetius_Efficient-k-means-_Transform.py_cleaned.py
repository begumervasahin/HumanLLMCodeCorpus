import numpy as np
from itertools import combinations
from math import acos, sqrt, pow, pi, cos, sin
import Matrix
'''Projections along dimensions: (b4+1)->(b4+1)^2 and back'''
def fonk1(A):
    b1 = np.matmul(A.transpose(),A)
    return np.reshape(b1,-1)
def fonk2(q, b4):
    b2 = Matrix.getClosestSymMatrix(np.reshape(q, (b4, b4)))
    b3 = -b2[b4 - 1]
    return b3
def fonk3(b3):
    b1 = np.outer(b3,b3)
    return np.reshape(b1, -1)
'''Cartesian -> Spherical '''
def fonk4(b3):
    b4 = len(b3)
    b5 = np.zeros((b4-1))
    b6 = len(b5)
    b7 = pow(b3[b6],2) + pow(b3[b6-1],2)
    b8 = acos(b3[b6-1]/(sqrt(b7)))
    if b3[b6] >= 0:
        b5[b6-1] = b8
    else:
        b5[b6-1] = 2*pi-b8
    for k in range(b6-2,-1,-1):
        b7 = b7 + pow(b3[k],2)
        b5[k] = acos(b3[k]/sqrt(b7))
    return b5
'''Spherical -> Cartesian '''
def fonk5(b5):
    b9 = len(b5)
    b3 = np.zeros(b9+1)
    a1 = 1
    for i in range(0,b9):
        b3[i] = a1*cos(b5[i])
        a1 *= sin(b5[i])
    b3[b9] = a1
    return b3
'''Alternative Code: Appendix method'''
'''P-Q: Appendix Version'''
def fonk6(A,j):
    b4 = len(A[0,:])
    b10 = np.array([])
    b11 = np.reshape(np.multiply(A, A), (1, A.shape[0] * A.shape[1]))
    b10 = np.append(b10, b11)
    b12 = range(b4 + 1)
    b13 = list(combinations(b12, 2))
    for i in range(b4 - j):
        b14 = 2 * np.multiply(A[i, [b3[0] for b3 in b13]], A[i, [b3[1] for b3 in b13]])
        b10 = np.append(b10, b14)
    return b10
def fonk7(q, b4, j):
    b15 = np.sqrt(np.abs(q[0:b4]))
    b16 = q[b4 * (b4 - j):b4 * (b4 - j) + b4 - 1]
    b3 = np.zeros(b4)
    b3[0] = np.absolute(b15[0])
    for i in range(1, len(b15)):
        if (b16[i - 1] < 0):
            b3[i] = -np.absolute(b15[i])
        else:
            b3[i] = np.absolute(b15[i])
    return b3