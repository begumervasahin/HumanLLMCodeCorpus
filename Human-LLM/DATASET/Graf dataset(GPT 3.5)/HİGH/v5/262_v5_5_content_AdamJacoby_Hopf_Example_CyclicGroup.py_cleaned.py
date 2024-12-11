from ExampleGroup_Functions import *
from HopfClass import HopfAlgebra
import numpy as np
import scipy.sparse as sps
from itertools import product
def fonk1(a1):
    b1 = np.zeros((a1, a1**2), dtype=complex)
    for i, j in product(range(a1), b2 = 2):
        b1[(i + j) % a1, i * a1 + j] = 1
    b3 = sps.csr_matrix(b1, dtype=complex)
    return b3
def fonk2(a1):
    b4 = np.zeros((a1, a1), dtype=complex)
    for i in range(a1):
        b4[i, (-i) % a1] = 1
    b5 = sps.csr_matrix(b4, dtype=complex)
    return b5
def fonk3(a1, b12):
    b6 = [f"{b12}^{i}" for i in range(a1)]
    return b6
def fonk4(a1, b12):
    b1 = fonk1(a1)
    b7 = Group_Comult_Matrix(a1)
    b8 = Group_Counit(a1)
    b9 = Group_Integral(a1)
    b4 = fonk2(a1)
    b10 = f"C_{a1}"
    b6 = fonk3(a1, b12)
    b11 = HopfAlgebra(b10, b6, b1, b7, b8, b4)
    b11.Input_Integral(b9)
    return b11
a1 = 4
b12 = 'a'
b11 = fonk4(a1, b12)
print(b11)