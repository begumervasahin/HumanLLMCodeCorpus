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
    return csr_matrix(b2, b1 = complex)
def fonk4(b5, b6, b7, b16):
    b3 = len(b6)
    b4 = HopfAlgebra(
        b5 = b5,
        b6 = b6,
        b7 = b7,
        b8 = fonk3(b3),
        b9 = fonk2(b3),
        b10 = b16
    )
    b4.input_integral(fonk1(b3))
    return b4
def fonk5(b20):
    b11 = list(b20.b11)
    b3 = len(b11)
    b12 = max(max(e) for e in b11)
    b13 = comb.Permutation(b12)
    if b13 in b11:
        b11.remove(b13)
        b11.insert(0, b13)
    b6 = [str(list(e)).replace(" ", "") for e in b11]
    b7 = np.zeros((b3, b3**2), b1=int)
    for i, j in product(range(b3), b14 = 2):
        b15 = b11.index(b11[i] * b11[j])
        b7[b15, i * b3 + j] = 1
    b7 = csr_matrix(b7, b1=int)
    b16 = np.zeros((b3, b3), b1=int)
    for i in range(b3):
        b17 = b11[i]**-1
        if b17 in b11:
            b18 = b11.index(b17)
            b16[b18, i] = 1
    b16 = csr_matrix(b16, b1=int)
    return {
        'b6': b6,
        'mult': b7,
        'b10': b16
    }
if b19 = = '__main__':
    b20 = comb.PermutationGroup([
        comb.Permutation([0, 1]),
        comb.Permutation([1, 0])
    ])
    b21 = fonk5(b20)
    b4 = fonk4(
        b5 = 'ExampleHopf',
        b6 = b21['b6'],
        b7 = b21['mult'],
        b16 = b21['b10']
    )
    print("Hopf Algebra created:", b4)