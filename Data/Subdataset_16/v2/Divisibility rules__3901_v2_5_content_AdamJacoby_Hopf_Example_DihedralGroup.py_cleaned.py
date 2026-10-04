import numpy as np
import scipy.sparse as sps
from itertools import product
from ExampleGroup_Functions import Group_Comult_Matrix, Group_Counit, Group_Integral
from HopfClass import HopfAlgebra
def fonk1(a1):
    b1 = 2 * a1
    b2 = np.zeros((b1, b1**2), b3=complex)
    for i, j in product(range(a1), [0, 1]):
        for k, l in product(range(a1), [0, 1]):
            b2[2 * ((i + ((-1) ** j) * k) % a1) + (j + l) % 2, b1 * (i * 2 + j) + 2 * k + l] = 1
    return sps.csr_matrix(b2, b3 = complex)
def fonk2(a1):
    b1 = 2 * a1
    b4 = np.zeros((b1, b1), b3=complex)
    for i, j in product(range(a1), [0, 1]):
        b4[2 * (((-1) ** (j + 1) * i) % a1) + j, i * 2 + j] = 1
    return sps.csr_matrix(b4, b3 = complex)
def fonk3(a1, b14, b15):
    return [f"{b14}^{i}{b15}^{j}" for i in range(a1) for j in [0, 1]]
def fonk4(a1, b14, b15):
    b5 = fonk1(a1)
    b6 = Group_Comult_Matrix(2 * a1)
    b7 = Group_Counit(2 * a1)
    b8 = Group_Integral(2 * a1)
    b9 = fonk2(a1)
    b10 = f"D_{a1}"
    b11 = fonk3(a1, b14, b15)
    b12 = HopfAlgebra(b10, b11, b5, b6, b7, b9)
    b12.Input_Integral(b8)
    return b12
if b13 = = "__main__":
    a1 = 5
    b14 = "g"
    b15 = "x"
    b16 = fonk4(a1, b14, b15)
    print(b16)