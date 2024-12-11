from ExampleGroup_Functions import *
from HopfClass import HopfAlgebra
import numpy as np
import scipy.sparse as sps
from itertools import product
def fonk1(a1, a2, a3):
    b1 = a1 * a2
    b2 = np.zeros((b1, b1**2), b5=complex)
    for i, j in product(range(a2), range(a1)):
        for k, l in product(range(a2), range(a1)):
            b3 = a1 * ((i + a3 * k) % a2) + (k + l) % a1
            b4 = b1 * (i * a1 + j) + a1 * k + l
            b2[b3, b4] = 1
    return sps.csr_matrix(b2, b5 = complex)
def fonk2(a1, a2, a3):
    b1 = a1 * a2
    b6 = np.zeros((b1, b1), b5=complex)
    for i, j in product(range(a2), range(a1)):
        b7 = (((a3**j) % a2)**(a2 - 2)) % a2
        b3 = ((-i * b7) % a2) * a1 + ((-j) % a1)
        b4 = i * a1 + j
        b6[b3, b4] = 1
    return sps.csr_matrix(b6, b5 = complex)
def fonk3(a1, a2, ele_name_g, ele_name_x):
    b8 = [f"{ele_name_g}^{i}{ele_name_x}^{j}" for i in range(a2) for j in range(a1)]
    return b8
def fonk4(a1, a2, a3, b14, b15):
    b1 = a1 * a2
    b2 = fonk1(a1, a2, a3)
    b9 = Group_Comult_Matrix(b1)
    b10 = Group_Counit(b1)
    b11 = Group_Integral(b1)
    b6 = fonk2(a1, a2, a3)
    b12 = f'B_{a1},{a2},{a3}'
    b8 = fonk3(a1, a2, b14, b15)
    b13 = HopfAlgebra(b12, b8, b2, b9, b10, b6)
    b13.Input_Integral(b11)
    return b13
a1 = 3
a2 = 2
a3 = 1
b14 = 'g'
b15 = 'x'
b13 = fonk4(a1, a2, a3, b14, b15)