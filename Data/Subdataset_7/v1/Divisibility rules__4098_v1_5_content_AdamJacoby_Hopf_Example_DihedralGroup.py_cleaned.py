from ExampleGroup_Functions import *
from HopfClass import HopfAlgebra
import numpy as np
import scipy.sparse as sps
from itertools import product
def fonk1(a1):
    b1 = 2 * a1
    b2 = np.zeros((b1, b1**2), dtype=complex)
    b3 = range(a1)
    for i, j, k, l in product(b3, [0, 1], b4 = 2):
        b2[2 * ((i + ((-1) ** j) * k) % a1) + (j + l) % 2, b1 * (i * 2 + j) + 2 * k + l] = 1
    b5 = sps.csr_matrix(b2, dtype=complex)
    return b5
def fonk2(a1):
    b1 = 2 * a1
    b6 = np.zeros((b1, b1), dtype=complex)
    for i, j in product(range(a1), [0, 1]):
        b6[2 * (((-1) ** (j + 1) * i) % a1) + j, i * 2 + j] = 1
    b7 = sps.csr_matrix(b6, dtype=complex)
    return b7
def fonk3(a1, ele_name_g, ele_name_x):
    b8 = []
    for i in range(a1):
        for j in [0, 1]:
            b8.append(f"{ele_name_g}^{i}{ele_name_x}^{j}")
    return b8
def fonk4(a1, b14, b15):
    b1 = 2 * a1
    b2 = fonk1(a1)
    b9 = Group_Comult_Matrix(b1)
    b10 = Group_Counit(b1)
    b11 = Group_Integral(b1)
    b6 = fonk2(a1)
    b12 = f"D_{a1}"
    b8 = fonk3(a1, b14, b15)
    b13 = HopfAlgebra(b12, b8, b2, b9, b10, b6)
    b13.Input_Integral(b11)
    return b13
a1 = 3
b14 = 'g'
b15 = 'x'
b13 = fonk4(a1, b14, b15)
print(b13)