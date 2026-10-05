from ExampleGroup_Functions import *
from HopfClass import HopfAlgebra
import numpy as np
import scipy.sparse as sps
from itertools import product
def fonk1(a1):
    b1 = 2 * a1
    b2 = np.zeros((b1, b1**2), dtype=complex)
    for i, j, k, l in product(range(a1), [0, 1], b3 = 2):
        b4 = 2 * ((i + ((-1) ** j) * k) % a1) + (j + l) % 2
        b5 = b1 * (i * 2 + j) + 2 * k + l
        b2[b4, b5] = 1
    return sps.csr_matrix(b2)
def fonk2(a1):
    b1 = 2 * a1
    b6 = np.zeros((b1, b1), dtype=complex)
    for i, j in product(range(a1), [0, 1]):
        b4 = 2 * (((-1) ** (j + 1) * i) % a1) + j
        b5 = i * 2 + j
        b6[b4, b5] = 1
    return sps.csr_matrix(b6)
def fonk3(a1, ele_name_g, ele_name_x):
    return [f"{ele_name_g}^{i}{ele_name_x}^{j}" for i in range(a1) for j in [0, 1]]
def fonk4(a1, b13, b14):
    b1 = 2 * a1
    b2 = fonk1(a1)
    b7 = Group_Comult_Matrix(b1)
    b8 = Group_Counit(b1)
    b9 = Group_Integral(b1)
    b6 = fonk2(a1)
    b10 = f"D_{a1}"
    b11 = fonk3(a1, b13, b14)
    b12 = HopfAlgebra(b10, b11, b2, b7, b8, b6)
    b12.Input_Integral(b9)
    return b12
a1 = 3
b13 = 'g'
b14 = 'x'
b12 = fonk4(a1, b13, b14)
print(b12)