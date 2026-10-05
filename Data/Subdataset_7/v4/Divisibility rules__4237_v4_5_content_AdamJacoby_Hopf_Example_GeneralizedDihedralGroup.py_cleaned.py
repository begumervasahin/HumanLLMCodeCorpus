from ExampleGroup_Functions import *
from HopfClass import HopfAlgebra
import numpy as np
import scipy.sparse as sps
from itertools import product
def fonk1(a1, a2, a3):
    b1 = a1 * a2
    b2 = np.zeros((b1, b1**2), dtype=complex)
    for i, j in product(range(a2), range(a1)):
        for k, l in product(range(a2), range(a1)):
            b2[a1 * ((i + a3 * k) % a2) + (k + l) % a1, b1 * (i * a1 + j) + a1 * k + l] = 1
    b2 = sps.csr_matrix(b2.tolist(), dtype=complex)
    return b2
def fonk2(a1, a2, a3):
    b1 = a1 * a2
    b3 = np.zeros((b1, b1), dtype=complex)
    for i, j in product(range(a2), range(a1)):
        b4 = (((a3**j) % a2)**(a2 - 2)) % a2
        b3[((-i * b4) % a2) * a1 + ((-j) % a1), i * a1 + j] = 1
    b3 = sps.csr_matrix(b3.tolist(), dtype=complex)
    return b3
def fonk3(a1, a2, ele_name_g, ele_name_x):
    b5 = []
    for i in range(a2):
        for j in range(a1):
            b5.append(ele_name_g + '^' + str(i) + ele_name_x + '^' + str(j))
    return b5
def fonk4(a1, a2, a3, b12, b13):
    b1 = a1 * a2
    b2 = fonk1(a1, a2, a3)
    b6 = Group_Comult_Matrix(b1)
    b7 = Group_Counit(b1)
    b8 = Group_Integral(b1)
    b3 = fonk2(a1, a2, a3)
    b9 = 'B_' + str(a1) + ',' + str(a2) + ',' + str(a3)
    b10 = fonk3(a1, a2, b12, b13)
    b11 = HopfAlgebra(b9, b10, b2, b6, b7, b3)
    b11.Input_Integral(b8)
    return b11
a1 = 3
a2 = 2
a3 = 1
b12 = 'g'
b13 = 'x'
b11 = fonk4(a1, a2, a3, b12, b13)