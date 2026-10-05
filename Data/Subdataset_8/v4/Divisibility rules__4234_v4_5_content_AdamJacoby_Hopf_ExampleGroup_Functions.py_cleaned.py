import numpy as np
from scipy.sparse import csr_matrix
from HopfClass import HopfAlgebra
import sympy.combinatorics as comb
def group_integral(dim):
    return np.ones(dim, dtype=complex)
def group_counit(dim):
    return np.ones(dim, dtype=complex)
def group_comult_matrix(dim):
    temp = np.zeros((dim**2, dim), dtype=complex)
    for i in range(dim):
        temp[i + dim * i, i] = 1
    return csr_matrix(temp.tolist(), dtype=complex)
def make_group_algebra(name, ele_names, mult, antipode):
    dim = len(ele_names)
    G = HopfAlgebra(name, ele_names, mult, group_comult_matrix(dim), group_counit(dim), antipode)
    G.input_integral(group_integral(dim))
    return G
def permutation_group_info(P):
    Elements = list(P.elements)
    dim = len(Elements)
    permutation_size = max(list(Elements[0]))
    identity = comb.Permutation(permutation_size)
    Elements.remove(identity)
    Elements.insert(0, identity)
    ele_names = [str(list(Element)).replace(" ", "") for Element in Elements]
    mult = np.zeros((dim, dim**2))
    for i, j in product(range(dim), range(dim)):
        k = Elements.index(Elements[i] * Elements[j])
        mult[k, i * dim + j] = 1
    mult = csr_matrix(mult.tolist(), dtype=np.int8)
    antipode = np.zeros((dim, dim))
    for i in range(dim):
        inverse = Elements[i] ** -1
        j = Elements.index(inverse)
        antipode[j, i] = 1
    antipode = csr_matrix(antipode.tolist(), dtype=np.int8)
    return {'element_names': ele_names, 'mult': mult, 'antipode': antipode}