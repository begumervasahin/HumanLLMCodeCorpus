import numpy as np
from scipy.sparse import csr_matrix
from itertools import product
from HopfClass import Algebra
def fonk1(n):
    return [f"T_{i},{j}" for i, j in product(range(n), b1 = 2)]
def fonk2(n):
    b2 = n ** 2
    b3 = np.zeros((b2, b2 ** 2))
    for i, j, k in product(range(n), b1 = 3):
        b3[i * n + k, b2 * (i * n + j) + n * j + k] = 1
    return csr_matrix(b3)
def fonk3(n):
    b2 = n ** 2
    b4 = np.zeros((b2 ** 2))
    for i, j in product(range(n), b1 = 2):
        b4[b2 * (n * i + j) + n * j + i] = n
    return b4
def fonk4(n):
    b5 = fonk1(n)
    b6 = fonk2(n)
    b7 = Algebra(f"M_{n}", b5, b6)
    b7.Input_Casimir(fonk3(n))
    return b7