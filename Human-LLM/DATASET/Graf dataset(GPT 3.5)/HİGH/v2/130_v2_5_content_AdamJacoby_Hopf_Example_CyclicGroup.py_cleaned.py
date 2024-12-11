from ExampleGroup_Functions import *
from HopfClass import HopfAlgebra
import numpy as np
import scipy.sparse as sps
from itertools import product
def fonk1(a1):
    b1 = np.zeros((a1, a1**2), dtype=complex)
    for i, j in product(range(a1), range(a1)):
        b1[(i+j) % a1, i*a1+j] = 1
    b1 = sps.csr_matrix(b1.tolist(), dtype=complex)
    return b1
def fonk2(a1):
    b2 = np.zeros((a1, a1), dtype=complex)
    for i in range(a1):
        b2[i, (-i) % a1] = 1
    b2 = sps.csr_matrix(b2.tolist(), dtype=complex)
    return b2
def fonk3(a1, ele_name):
    return [f"{ele_name}^{i}" for i in range(a1)]
def fonk4(a1, b9):
    b1 = fonk1(a1)
    b3 = Group_Comult_Matrix(a1)
    b4 = Group_Counit(a1)
    b5 = Group_Integral(a1)
    b2 = fonk2(a1)
    b6 = f"C_{a1}"
    b7 = fonk3(a1, b9)
    b8 = HopfAlgebra(b6, b7, b1, b3, b4, b2)
    b8.Input_Integral(b5)
    return b8
a1 = 4
b9 = 'a'
b10 = fonk4(a1, b9)
print(b10)