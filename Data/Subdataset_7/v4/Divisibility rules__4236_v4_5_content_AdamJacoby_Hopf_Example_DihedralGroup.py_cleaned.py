from ExampleGroup_Functions import *
from HopfClass import HopfAlgebra
import numpy as np
import scipy.sparse as sps
from itertools import product
def fonk1(n):
    b1 = 2 * n
    b2 = np.zeros((b1, b1**2), dtype=complex)
    for i, j, k, l in product(range(n), [0, 1], b3 = 2):
        b4 = 2 * ((i + ((-1) ** j) * k) % n) + (j + l) % 2
        b5 = b1 * (i * 2 + j) + 2 * k + l
        b2[b4, b5] = 1
    return sps.csr_matrix(b2)
def fonk2(n):
    b1 = 2 * n
    b6 = np.zeros((b1, b1), dtype=complex)
    for i, j in product(range(n), [0, 1]):
        b4 = 2 * (((-1) ** (j + 1) * i) % n) + j
        b5 = i * 2 + j
        b6[b4, b5] = 1
    return sps.csr_matrix(b6)
def fonk3(n, ele_name_g, ele_name_x):
    b7 = [f"{ele_name_g}^{i}{ele_name_x}^{j}" for i in range(n) for j in [0, 1]]
    return b7
def fonk4(n, element_name_g, element_name_x):
    b1 = 2 * n
    b2 = fonk1(n)
    b8 = Group_Comult_Matrix(b1)
    b9 = Group_Counit(b1)
    b10 = Group_Integral(b1)
    b6 = fonk2(n)
    b11 = f"D_{n}"
    b7 = fonk3(n, element_name_g, element_name_x)
    b12 = HopfAlgebra(b11, b7, b2, b8, b9, b6)
    b12.Input_Integral(b10)
    return b12