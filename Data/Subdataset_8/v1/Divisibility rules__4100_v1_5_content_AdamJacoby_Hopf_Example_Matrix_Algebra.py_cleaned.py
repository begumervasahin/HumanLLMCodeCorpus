import numpy as np
from scipy.sparse import csr_matrix
from itertools import product
from HopfClass import Algebra
def matrix_algebra_element_names(n):
    element_names = [f"T_{i},{j}" for i, j in product(range(n), repeat=2)]
    return element_names
def matrix_algebra_mult_matrix(n):
    dim = n ** 2
    mult = np.zeros((dim, dim ** 2))
    for i, j, k in product(range(n), repeat=3):
        mult[i * n + k, dim * (i * n + j) + n * j + k] = 1
    return csr_matrix(mult)
def matrix_algebra_casimir(n):
    dim = n ** 2
    casimir = np.zeros((dim ** 2))
    for i, j in product(range(n), repeat=2):
        casimir[dim * (n * i + j) + n * j + i] = n
    return casimir
def matrix_algebra(n):
    element_names = matrix_algebra_element_names(n)
    mult_matrix = matrix_algebra_mult_matrix(n)
    M = Algebra(f"M_{n}", element_names, mult_matrix)
    M.Input_Casimir(matrix_algebra_casimir(n))
    return M