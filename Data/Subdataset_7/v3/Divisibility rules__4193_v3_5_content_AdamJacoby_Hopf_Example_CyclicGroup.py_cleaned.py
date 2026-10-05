from ExampleGroup_Functions import *
from HopfClass import HopfAlgebra
import numpy as np
import scipy.sparse as sps
from itertools import product
def fonk1(a1):
    b1 = np.zeros((a1, a1**2), dtype=complex)
    for i, j in product(range(a1), b2 = 2):
        b1[(i + j) % a1, i * a1 + j] = 1
    b1 = sps.csr_matrix(b1, dtype=complex)
    return b1
def fonk2(a1):
    b3 = np.zeros((a1, a1), dtype=complex)
    for i in range(a1):
        b3[i, (-i) % a1] = 1
    b3 = sps.csr_matrix(b3, dtype=complex)
    return b3
def fonk3(a1, b10):
    return [f"{b10}^{i}" for i in range(a1)]
def fonk4(a1, b10):
    b1 = fonk1(a1)
    b4 = Group_Comult_Matrix(a1)
    b5 = Group_Counit(a1)
    b6 = Group_Integral(a1)
    b3 = fonk2(a1)
    b7 = f"C_{a1}"
    b8 = fonk3(a1, b10)
    b9 = HopfAlgebra(b7, b8, b1, b4, b5, b3)
    b9.Input_Integral(b6)
    return b9
a1 = 4
b10 = 'a'
b9 = fonk4(a1, b10)
print(b9)