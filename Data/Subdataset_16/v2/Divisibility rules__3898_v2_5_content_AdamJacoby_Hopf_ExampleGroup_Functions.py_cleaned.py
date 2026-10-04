import numpy as np
from scipy.sparse import csr_matrix
from itertools import product
from HopfClass import HopfAlgebra
import sympy.combinatorics as comb
def fonk1(dim):
    return np.ones(dim, b1 = complex)
def fonk2(dim):
    return np.ones(dim, b1 = complex)
def fonk3(dim):
    b2 = np.zeros((dim**2, dim), b1=complex)
    for i in range(dim):
        b2[i + dim * i, i] = 1
    return csr_matrix(b2, b1 = complex)
def fonk4(b18, b8, b9, b12):
    b3 = len(b8)
    b4 = HopfAlgebra(
        b18,
        b8,
        b9,
        fonk3(b3),
        fonk2(b3),
        b12
    )
    b4.input_integral(fonk1(b3))
    return b4
def fonk5(b16):
    b5 = list(b16.b5)
    b3 = len(b5)
    b6 = max(max(e) for e in b5)
    b7 = comb.Permutation(b6)
    b5.remove(b7)
    b5.insert(0, b7)
    b8 = [str(list(e)).replace(" ", "") for e in b5]
    b9 = np.zeros((b3, b3**2), b1=int)
    for i, j in product(range(b3), b10 = 2):
        b11 = b5.index(b5[i] * b5[j])
        b9[b11, i * b3 + j] = 1
    b9 = csr_matrix(b9, b1=int)
    b12 = np.zeros((b3, b3), b1=int)
    for i in range(b3):
        b13 = b5[i]**-1
        b14 = b5.index(b13)
        b12[b14, i] = 1
    b12 = csr_matrix(b12, b1=int)
    return {
        'b8': b8,
        'mult': b9,
        'antipode': b12
    }
if b15 = = '__main__':
    b16 = comb.PermutationGroup([comb.Permutation([0, 1]), comb.Permutation([1, 0])])
    b17 = fonk5(b16)
    b4 = fonk4(
        b18 = 'ExampleHopf',
        b8 = b17['b8'],
        b9 = b17['mult'],
        b12 = b17['antipode']
    )
    print("Hopf Algebra created:", b4)