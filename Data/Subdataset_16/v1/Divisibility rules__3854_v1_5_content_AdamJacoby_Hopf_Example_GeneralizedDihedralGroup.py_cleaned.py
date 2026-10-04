
import numpy as np
import scipy.sparse as sps
from itertools import product
from ExampleGroup_Functions import Group_Comult_Matrix, Group_Counit, Group_Integral
from HopfClass import HopfAlgebra
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
        b7 = (((a3 ** j) % a2) ** (a2 - 2)) % a2
        b3 = ((-i * b7) % a2) * a1 + ((-j) % a1)
        b4 = i * a1 + j
        b6[b3, b4] = 1
    return sps.csr_matrix(b6, b5 = complex)
def fonk3(a1, a2, b17, b18):
    return [f"{b17}^{i}{b18}^{j}" for i in range(a2) for j in range(a1)]
def fonk4(a1, a2, a3, b17, b18):
    b1 = a1 * a2
    b8 = fonk1(a1, a2, a3)
    b9 = Group_Comult_Matrix(b1)
    b10 = Group_Counit(b1)
    b11 = Group_Integral(b1)
    b12 = fonk2(a1, a2, a3)
    b13 = f"B_{a1},{a2},{a3}"
    b14 = fonk3(a1, a2, b17, b18)
    b15 = HopfAlgebra(b13, b14, b8, b9, b10, b12)
    b15.Input_Integral(b11)
    return b15
if b16 = = "__main__":
    a1 = 3
    a2 = 4
    a3 = 2
    b17 = "g"
    b18 = "x"
    b19 = fonk4(a1, a2, a3, b17, b18)
    print(b19)