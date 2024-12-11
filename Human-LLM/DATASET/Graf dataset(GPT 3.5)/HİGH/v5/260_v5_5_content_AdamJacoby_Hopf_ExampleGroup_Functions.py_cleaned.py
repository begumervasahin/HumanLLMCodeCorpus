import numpy as np
from scipy.sparse import csr_matrix
from HopfClass import HopfAlgebra
import sympy.combinatorics as comb
def fonk1(b3):
    return np.ones(b3, b1 = complex)
def fonk2(b3):
    return np.ones(b3, b1 = complex)
def fonk3(b3):
    b2 = np.zeros((b3**2, b3), b1=complex)
    for i in range(b3):
        b2[i + b3 * i, i] = 1
    return csr_matrix(b2.tolist(), b1 = complex)
def fonk4(name, b9, b10, b12):
    b3 = len(b9)
    b4 = fonk3(b3)
    b5 = HopfAlgebra(name, b9, b10, b4, fonk2(b3), b12)
    b5.input_integral(fonk1(b3))
    return b5
def fonk5(P):
    b6 = list(P.elements)
    b3 = len(b6)
    b7 = max(list(b6[0]))
    b8 = comb.Permutation(b7)
    b6.remove(b8)
    b6.insert(0, b8)
    b9 = [str(list(Element)).replace(" ", "") for Element in b6]
    b10 = np.zeros((b3, b3**2))
    for i, b14 in product(range(b3), range(b3)):
        b11 = b6.index(b6[i] * b6[b14])
        b10[b11, i * b3 + b14] = 1
    b10 = csr_matrix(b10.tolist(), b1=np.int8)
    b12 = np.zeros((b3, b3))
    for i in range(b3):
        b13 = b6[i] ** -1
        b14 = b6.index(b13)
        b12[b14, i] = 1
    b12 = csr_matrix(b12.tolist(), b1=np.int8)
    return {'element_names': b9, 'b10': b10, 'b12': b12}