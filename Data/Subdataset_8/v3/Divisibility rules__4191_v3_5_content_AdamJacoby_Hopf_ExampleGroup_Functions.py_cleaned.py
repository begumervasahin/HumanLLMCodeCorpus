import numpy as np
from scipy.sparse import csr_matrix
from itertools import product
from HopfClass import HopfAlgebra
import sympy.combinatorics as comb
def generate_group_integral(dim):
    return np.ones(dim, dtype=complex)
def generate_group_counit(dim):
    return np.ones(dim, dtype=complex)
def generate_group_comult_matrix(dim):
    comult_matrix = np.zeros((dim**2, dim), dtype=complex)
    for i in range(dim):
        comult_matrix[i + dim * i, i] = 1
    return csr_matrix(comult_matrix.tolist(), dtype=complex)
def create_group_algebra(name, element_names, multiplication_matrix, antipode_matrix):
    dim = len(element_names)
    group_algebra = HopfAlgebra(name, element_names, multiplication_matrix,
                                generate_group_comult_matrix(dim),
                                generate_group_counit(dim),
                                antipode_matrix)
    group_algebra.input_integral(generate_group_integral(dim))
    return group_algebra
def get_permutation_group_info(permutation_group):
    elements = list(permutation_group.elements)
    dim = len(elements)
    max_permutation_size = max(list(elements[0]))
    identity_permutation = comb.Permutation(max_permutation_size)
    elements.remove(identity_permutation)
    elements.insert(0, identity_permutation)
    element_names = [str(list(element)).replace(" ", "") for element in elements]
    multiplication_matrix = np.zeros((dim, dim**2))
    for i, j in product(range(dim), range(dim)):
        k = elements.index(elements[i] * elements[j])
        multiplication_matrix[k, i * dim + j] = 1
    multiplication_matrix = csr_matrix(multiplication_matrix.tolist(), dtype=np.int8)
    antipode_matrix = np.zeros((dim, dim))
    for i in range(dim):
        inverse = elements[i] ** -1
        j = elements.index(inverse)
        antipode_matrix[j, i] = 1
    antipode_matrix = csr_matrix(antipode_matrix.tolist(), dtype=np.int8)
    return {'element_names': element_names, 'multiplication_matrix': multiplication_matrix, 'antipode_matrix': antipode_matrix}
permutation_group = comb.PermutationGroup(range(1, 5))
group_info = get_permutation_group_info(permutation_group)
group_algebra = create_group_algebra("PermutationGroup", group_info['element_names'],
                                     group_info['multiplication_matrix'], group_info['antipode_matrix'])