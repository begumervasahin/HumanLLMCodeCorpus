import numpy as np
import scipy.sparse as sps
from itertools import product
from HopfClass import HopfAlgebra
def fonk1(a1, b18, b19):
    return [f"{b18}^{j}{b19}^{i}" for i in range(a1) for j in range(a1)]
def fonk2(a1):
    b1 = [0] * (a1 + 1)
    b1[0] = 1
    b1[a1] = -1
    b2 = np.roots(b1)
    b3 = np.zeros((a1**2, a1**4), b5=complex)
    for i, j, k in product(range(a1), b4 = 3):
        for l in range(a1 - j):
            b3[((i + k) % a1) + a1 * (j + l), i + a1 * j + (k + a1 * l) * a1**2] = b2[(a1 - 1) - (-j * k) % a1]
    return sps.csr_matrix(b3, b5 = complex)
def fonk3(a1, b12):
    b6 = a1**2
    b3 = np.zeros((b6**2, b6), b5=complex)
    b7 = np.zeros(b6)
    b7[1] = 1
    b7[a1] = 1
    b8 = np.zeros(b6)
    b8[0] = 1
    b9 = [b8]
    for i in range(1, a1):
        b10 = np.kron(b8, b7)
        b8 = b12.dot(b10)
        b9.append(b8)
    for i, j in product(range(a1), b4 = 2):
        for l in range(j + 1):
            b3[((i + l) % a1) + (j - l) * a1 + (i + a1 * l) * b6, i + j * a1] = b9[j][l + (j - l) * a1]
    return b3
def fonk4(a1):
    return np.ones(a1, b5 = complex)
def fonk5(a1):
    b6 = a1**2
    b1 = [0] * (a1 + 1)
    b1[0] = 1
    b1[a1] = -1
    b2 = np.roots(b1)
    b3 = np.zeros((b6, b6), b5=complex)
    for i, j in product(range(a1), b4 = 2):
        b3[((-i) % a1) + j * a1, i * a1 + j] = (-1)**j * b2[(i * j) % a1]
    return sps.csr_matrix(b3, b5 = complex)
def fonk6(a1, b18, b19):
    b11 = fonk1(a1, b18, b19)
    b12 = fonk2(a1)
    b13 = fonk3(a1, b12)
    b14 = fonk4(a1)
    b15 = fonk5(a1)
    b16 = HopfAlgebra(f'Taft_{a1}', b11, b12, b13, b14, b15)
    return b16
if b17 = = "__main__":
    a1 = 3
    b18 = "b18"
    b19 = "b19"
    b20 = fonk6(a1, b18, b19)
    print(b20)