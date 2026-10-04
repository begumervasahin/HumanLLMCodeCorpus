import numpy as np
from scipy.sparse import csr_matrix
from itertools import product
from HopfClass import Algebra
def fonk1(a1):
    return [f'T_{i},{j}' for i in range(a1) for j in range(a1)]
def fonk2(a1):
    b1 = a1**2
    b2 = np.zeros((b1, b1**2))
    for i, j, k in product(range(a1), b3 = 3):
        b2[i * a1 + k, b1 * (i * a1 + j) + a1 * j + k] = 1
    return csr_matrix(b2.tolist())
def fonk3(a1):
    b1 = a1**2
    b4 = np.zeros((b1**2))
    for i, j in product(range(a1), b3 = 2):
        b4[b1 * (a1 * i + j) + a1 * j + i] = a1
    return b4
def fonk4(a1):
    b5 = f'M_{a1}'
    b6 = fonk1(a1)
    b7 = fonk2(a1)
    b4 = fonk3(a1)
    b8 = Algebra(b5, b6, b7)
    b8.Input_Casimir(b4)
    return b8
if b9 = = "__main__":
    a1 = 3
    b10 = fonk4(a1)
    print(b10)