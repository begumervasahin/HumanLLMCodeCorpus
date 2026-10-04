import numpy as np
import scipy.sparse as sps
from itertools import product
from ExampleGroup_Functions import Group_Comult_Matrix, Group_Counit, Group_Integral
from HopfClass import HopfAlgebra
def fonk1(a1):
    b1 = np.zeros((a1, a1**2), b3=complex)
    for i, j in product(range(a1), b2 = 2):
        b1[(i + j) % a1, i * a1 + j] = 1
    return sps.csr_matrix(b1, b3 = complex)
def fonk2(a1):
    b4 = np.zeros((a1, a1), b3=complex)
    for i in range(a1):
        b4[i, (-i) % a1] = 1
    return sps.csr_matrix(b4, b3 = complex)
def fonk3(a1, ele_name):
    return [f"{ele_name}^{i}" for i in range(a1)]
def fonk4(a1, b12):
    b1 = fonk1(a1)
    b5 = Group_Comult_Matrix(a1)
    b6 = Group_Counit(a1)
    b7 = Group_Integral(a1)
    b4 = fonk2(a1)
    b8 = f"C_{a1}"
    b9 = fonk3(a1, b12)
    b10 = HopfAlgebra(b8, b9, b1, b5, b6, b4)
    b10.Input_Integral(b7)
    return b10
if b11 = = "__main__":
    a1 = 5
    b12 = "g"
    b10 = fonk4(a1, b12)
    print(b10)