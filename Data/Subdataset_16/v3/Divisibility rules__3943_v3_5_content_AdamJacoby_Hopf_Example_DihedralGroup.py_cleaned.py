import numpy as np
import scipy.sparse as sps
from itertools import product
from ExampleGroup_Functions import Group_Comult_Matrix, Group_Counit, Group_Integral
from HopfClass import HopfAlgebra
def fonk1(a1):
    b1 = 2 * a1
    b2 = np.zeros((b1, b1**2), b5=complex)
    for i, j in product(range(a1), [0, 1]):
        for k, l in product(range(a1), [0, 1]):
            b3 = 2 * ((i + ((-1) ** j) * k) % a1) + (j + l) % 2
            b4 = b1 * (i * 2 + j) + 2 * k + l
            b2[b3, b4] = 1
    return sps.csr_matrix(b2, b5 = complex)
def fonk2(a1):
    b1 = 2 * a1
    b6 = np.zeros((b1, b1), b5=complex)
    for i, j in product(range(a1), [0, 1]):
        b3 = 2 * (((-1) ** (j + 1) * i) % a1) + j
        b4 = i * 2 + j
        b6[b3, b4] = 1
    return sps.csr_matrix(b6, b5 = complex)
def fonk3(a1, b16, b17):
    return [f"{b16}^{i}{b17}^{j}" for i in range(a1) for j in [0, 1]]
def fonk4(a1, b16, b17):
    b7 = fonk1(a1)
    b8 = Group_Comult_Matrix(2 * a1)
    b9 = Group_Counit(2 * a1)
    b10 = Group_Integral(2 * a1)
    b11 = fonk2(a1)
    b12 = f"D_{a1}"
    b13 = fonk3(a1, b16, b17)
    b14 = HopfAlgebra(b12, b13, b7, b8, b9, b11)
    b14.Input_Integral(b10)
    return b14
if b15 = = "__main__":
    a1 = 5
    b16 = "g"
    b17 = "x"
    b18 = fonk4(a1, b16, b17)
    print(b18)