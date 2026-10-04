import numpy as np
from scipy.sparse import csr_matrix
from itertools import product
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
    return csr_matrix(temp, dtype=complex)
def make_group_algebra(name, ele_names, mult, antipode):
    dim = len(ele_names)
    G = HopfAlgebra(name, ele_names, mult, group_comult_matrix(dim), group_counit(dim), antipode)
    G.input_integral(group_integral(dim))
    return G
def permutation_group_info(P):
    elements = list(P.elements)
    dim = len(elements)
    permutation_size = max(max(e) for e in elements)
    identity = comb.Permutation(permutation_size)
    elements.remove(identity)
    elements.insert(0, identity)
    ele_names = [str(list(e)).replace(" ", "") for e in elements]
    mult = np.zeros((dim, dim**2), dtype=int)
    for i, j in product(range(dim), repeat=2):
        k = elements.index(elements[i] * elements[j])
        mult[k, i * dim + j] = 1
    mult = csr_matrix(mult, dtype=int)
    antipode = np.zeros((dim, dim), dtype=int)
    for i in range(dim):
        inverse = elements[i]**-1
        j = elements.index(inverse)
        antipode[j, i] = 1
    antipode = csr_matrix(antipode, dtype=int)
    return {
        'element_names': ele_names,
        'mult': mult,
        'antipode': antipode
    }
if __name__ == '__main__':
    perm_group = comb.PermutationGroup([comb.Permutation([0, 1]), comb.Permutation([1, 0])])
    group_info = permutation_group_info(perm_group)
    hopf_algebra = make_group_algebra(
        name='ExampleHopf',
        ele_names=group_info['element_names'],
        mult=group_info['mult'],
        antipode=group_info['antipode']
    )
    print("Hopf Algebra created:", hopf_algebra)