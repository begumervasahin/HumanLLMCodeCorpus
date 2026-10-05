from HopfClass import *
import numpy as np
from itertools import product
import scipy.sparse as sps
def fonk1(a1, b11, b12):
    b1 = []
    for i in range(a1):
        for j in range(a1):
            b1.append(f"{b11}^{j}{b12}^{i}")
    return b1
def fonk2(a1):
    b2 = [0] * (a1 + 1)
    b2[0] = 1
    b2[a1] = -1
    b3 = np.roots(b2)
    b1 = np.zeros((a1**2, a1**4), b5=complex)
    b4 = range(a1)
    for i, j, k in product(b4, b4, b4):
        for l in range(a1 - j):
            b1[((i + k) % a1) + a1 * (j + l), i + a1 * j + (k + a1 * l) * a1**2] = b3[(a1 - 1) - (-j * k) % a1]
    return sps.csr_matrix(b1, b5 = complex)
def fonk3(a1, mult):
    b6 = a1 ** 2
    b1 = np.zeros((b6**2, b6), b5=complex)
    b7 = np.zeros(b6)
    b7[1] = 1
    b7[a1] = 1
    b8 = np.zeros(b6)
    b8[0] = 1
    b9 = [b8]
    b4 = range(1, a1)
    for i in b4:
        b10 = np.kron(b8, b7)
        b8 = mult.dot(b10)
        b9.append(b8)
    for i, j in product(b4, b4):
        for l in range(j + 1):
            b1[((i + l) % a1) + (j - l) * a1 + (i + a1 * l) * b6, i + j * a1] = b9[j][l + (j - l) * a1]
    return b1
def fonk4(a1):
    return np.ones(a1, b5 = complex)
def fonk5(a1):
    b6 = a1 ** 2
    b2 = [0] * (a1 + 1)
    b2[0] = 1
    b2[a1] = -1
    b3 = np.roots(b2)
    b1 = np.zeros((b6, b6), b5=complex)
    b4 = range(a1)
    for i, j in product(b4, b4):
        b1[((-i) % a1) + j * a1, i + j * a1] = (-1) ** j * b3[(i * j) % a1]
    return sps.csr_matrix(b1, b5 = complex)
a1 = 3
b11 = 'b11'
b12 = 'b12'
b13 = fonk1(a1, b11, b12)
b14 = fonk2(a1)
b15 = fonk3(a1, b14)
b16 = fonk4(a1)
b17 = fonk5(a1)
b18 = HopfAlgebra("TaftAlgebra", b13, b14, b15, b16, b17)