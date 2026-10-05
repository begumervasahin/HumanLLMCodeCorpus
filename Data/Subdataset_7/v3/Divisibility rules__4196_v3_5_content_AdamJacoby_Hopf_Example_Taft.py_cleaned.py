from HopfClass import HopfAlgebra
import numpy as np
import scipy.sparse as sps
from itertools import product
def fonk1(a1, b14, b15):
    b1 = [f"{b14}^{j}{b15}^{i}" for i, j in product(range(a1), b5=2)]
    return b1
def fonk2(a1):
    b2 = [0] * (a1 + 1)
    b2[0] = 1
    b2[a1] = -1
    b3 = np.roots(b2)
    b4 = np.zeros((a1**2, a1**4), b12=complex)
    for i, j, k in product(range(a1), b5 = 3):
        for l in range(a1 - j):
            b4[((i + k) % a1) + a1 * (j + l), i + a1 * j + (k + a1 * l) * a1**2] = b3[(a1 - 1) - (-j * k) % a1]
    return sps.csr_matrix(b4)
def fonk3(a1, b4):
    b6 = a1 ** 2
    b7 = np.zeros((b6**2, b6), b12=complex)
    b8 = np.zeros(b6)
    b8[1] = 1
    b8[a1] = 1
    b9 = np.zeros(b6)
    b9[0] = 1
    b10 = [b9]
    for i in range(1, a1):
        b11 = np.kron(b9, b8)
        b9 = b4.dot(b11)
        b10.append(b9)
    for i, j in product(range(1, a1), b5 = 2):
        for l in range(j + 1):
            b7[((i + l) % a1) + (j - l) * a1 + (i + a1 * l) * b6, i + j * a1] = b10[j][l + (j - l) * a1]
    return b7
def fonk4(a1):
    return np.ones(a1, b12 = complex)
def fonk5(a1):
    b6 = a1 ** 2
    b13 = np.zeros((b6, b6), b12=complex)
    b2 = [0] * (a1 + 1)
    b2[0] = 1
    b2[a1] = -1
    b3 = np.roots(b2)
    for i, j in product(range(a1), b5 = 2):
        b13[((-i) % a1) + j * a1, i + j * a1] = (-1) ** j * b3[(i * j) % a1]
    return sps.csr_matrix(b13)
a1 = 3
b14 = 'b14'
b15 = 'b15'
b1 = fonk1(a1, b14, b15)
b4 = fonk2(a1)
b7 = fonk3(a1, b4)
b16 = fonk4(a1)
b13 = fonk5(a1)
b17 = HopfAlgebra("TaftAlgebra", b1, b4, b7, b16, b13)