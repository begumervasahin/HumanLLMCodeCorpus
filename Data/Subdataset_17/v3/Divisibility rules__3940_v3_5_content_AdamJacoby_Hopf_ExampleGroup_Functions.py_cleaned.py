import numpy as np
from scipy.sparse import csr_matrix
from itertools import product
from HopfClass import HopfAlgebra
import sympy.combinatorics as comb
def create_group_integral(dim):
    return np.ones(dim, dtype=complex)
def create_group_counit(dim):
    return np.ones(dim, dtype=complex)
def create_comultiplication_matrix(dim):
    matrix = np.zeros((dim**2, dim), dtype=complex)
    for i in range(dim):
        matrix[i + dim * i, i] = 1
    return csr_matrix(matrix, dtype=complex)
def create_hopf_algebra(name, element_names, multiplication_matrix, antipode_matrix):
    dim = len(element_names)
    hopf_algebra = HopfAlgebra(
        name,
        element_names,
        multiplication_matrix,
        create_comultiplication_matrix(dim),
        create_group_counit(dim),
        antipode_matrix
    )
    hopf_algebra.input_integral(create_group_integral(dim))
    return hopf_algebra
def extract_permutation_group_info(permutation_group):
    elements = list(permutation_group.elements)
    dim = len(elements)
    permutation_size = max(max(e) for e in elements)
    identity = comb.Permutation(permutation_size)
    if identity in elements:
        elements.remove(identity)
        elements.insert(0, identity)
    element_names = [str(list(e)).replace(" ", "") for e in elements]
    multiplication_matrix = np.zeros((dim, dim**2), dtype=int)
    for i, j in product(range(dim), repeat=2):
        product_index = elements.index(elements[i] * elements[j])
        multiplication_matrix[product_index, i * dim + j] = 1
    multiplication_matrix = csr_matrix(multiplication_matrix, dtype=int)
    antipode_matrix = np.zeros((dim, dim), dtype=int)
    for i in range(dim):
        inverse = elements[i]**-1
        if inverse in elements:
            inverse_index = elements.index(inverse)
            antipode_matrix[inverse_index, i] = 1
    antipode_matrix = csr_matrix(antipode_matrix, dtype=int)
    return {
        'element_names': element_names,
        'mult': multiplication_matrix,
        'antipode': antipode_matrix
    }
if __name__ == '__main__':
    permutation_group = comb.PermutationGroup([
        comb.Permutation([0, 1]),
        comb.Permutation([1, 0])
    ])
    group_info = extract_permutation_group_info(permutation_group)
    hopf_algebra = create_hopf_algebra(
        name='ExampleHopf',
        element_names=group_info['element_names'],
        multiplication_matrix=group_info['mult'],
        antipode_matrix=group_info['antipode']
    )
    print("Hopf Algebra created:", hopf_algebra)