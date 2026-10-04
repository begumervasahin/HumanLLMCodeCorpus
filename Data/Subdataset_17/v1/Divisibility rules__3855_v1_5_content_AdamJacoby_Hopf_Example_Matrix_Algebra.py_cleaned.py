import numpy as np
from scipy.sparse import csr_matrix
from itertools import product
from HopfClass import Algebra
def generate_matrix_algebra_element_names(n):
    return [f'T_{i},{j}' for i in range(n) for j in range(n)]
def generate_matrix_algebra_mult_matrix(n):
    dim = n**2
    mult = np.zeros((dim, dim**2))
    for i, j, k in product(range(n), repeat=3):
        mult[i * n + k, dim * (i * n + j) + n * j + k] = 1
    return csr_matrix(mult.tolist())
def generate_matrix_algebra_casimir(n):
    dim = n**2
    casimir = np.zeros((dim**2))
    for i, j in product(range(n), repeat=2):
        casimir[dim * (n * i + j) + n * j + i] = n
    return casimir
def create_matrix_algebra(n):
    name = f'M_{n}'
    element_names = generate_matrix_algebra_element_names(n)
    mult_matrix = generate_matrix_algebra_mult_matrix(n)
    casimir = generate_matrix_algebra_casimir(n)
    matrix_algebra = Algebra(name, element_names, mult_matrix)
    matrix_algebra.Input_Casimir(casimir)
    return matrix_algebra
if __name__ == "__main__":
    n = 3
    matrix_algebra_instance = create_matrix_algebra(n)
    print(matrix_algebra_instance)