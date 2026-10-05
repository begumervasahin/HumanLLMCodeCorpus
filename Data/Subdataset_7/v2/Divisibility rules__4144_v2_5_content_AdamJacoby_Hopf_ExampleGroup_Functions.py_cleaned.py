import numpy as np
from scipy.sparse import csr_matrix
from itertools import product
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
def fonk4(name, b8, b9, b11):
    b3 = len(b8)
    b4 = HopfAlgebra(name, b8, b9, fonk3(b3), fonk2(b3), b11)
    b4.input_integral(fonk1(b3))
    return b4
def fonk5(b14):
    b5 = list(b14.elements)
    b3 = len(b5)
    b6 = max(list(b5[0]))
    b7 = comb.Permutation(b6)
    b5.remove(b7)
    b5.insert(0, b7)
    b8 = [str(list(Element)).replace(" ", "") for Element in b5]
    b9 = np.zeros((b3, b3**2))
    for i, b13 in product(range(b3), range(b3)):
        b10 = b5.index(b5[i] * b5[b13])
        b9[b10, i * b3 + b13] = 1
    b9 = csr_matrix(b9.tolist(), b1=np.int8)
    b11 = np.zeros((b3, b3))
    for i in range(b3):
        b12 = b5[i] ** -1
        b13 = b5.index(b12)
        b11[b13, i] = 1
    b11 = csr_matrix(b11.tolist(), b1=np.int8)
    return {'element_names': b8, 'b9': b9, 'b11': b11}
b14 = comb.PermutationGroup(range(1, 5))
b15 = fonk5(b14)
b16 = fonk4("PermutationGroup", b15['element_names'], b15['b9'], b15['b11'])