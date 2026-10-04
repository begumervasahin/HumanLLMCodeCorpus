import numpy as np
import scipy.sparse as sps
from itertools import product
from HopfClass import HopfAlgebra
def generate_taft_element_names(n, g, x):
    return [f"{g}^{j}{x}^{i}" for i in range(n) for j in range(n)]
def generate_taft_mult_matrix(n):
    poly = [0] * (n + 1)
    poly[0] = 1
    poly[n] = -1
    omega = np.roots(poly)
    out = np.zeros((n**2, n**4), dtype=complex)
    for i, j, k in product(range(n), repeat=3):
        for l in range(n - j):
            out[((i + k) % n) + n * (j + l), i + n * j + (k + n * l) * n**2] = omega[(n - 1) - (-j * k) % n]
    return sps.csr_matrix(out, dtype=complex)
def generate_taft_comult_matrix(n, mult_matrix):
    dim = n**2
    out = np.zeros((dim**2, dim), dtype=complex)
    x_plus_g = np.zeros(dim)
    x_plus_g[1] = 1
    x_plus_g[n] = 1
    temp = np.zeros(dim)
    temp[0] = 1
    prods = [temp]
    for i in range(1, n):
        temp2 = np.kron(temp, x_plus_g)
        temp = mult_matrix.dot(temp2)
        prods.append(temp)
    for i, j in product(range(n), repeat=2):
        for l in range(j + 1):
            out[((i + l) % n) + (j - l) * n + (i + n * l) * dim, i + j * n] = prods[j][l + (j - l) * n]
    return out
def generate_taft_counit(n):
    return np.ones(n, dtype=complex)
def generate_taft_antipode_matrix(n):
    dim = n**2
    poly = [0] * (n + 1)
    poly[0] = 1
    poly[n] = -1
    omega = np.roots(poly)
    out = np.zeros((dim, dim), dtype=complex)
    for i, j in product(range(n), repeat=2):
        out[((-i) % n) + j * n, i * n + j] = (-1)**j * omega[(i * j) % n]
    return sps.csr_matrix(out, dtype=complex)
def create_taft_algebra(n, g, x):
    element_names = generate_taft_element_names(n, g, x)
    mult_matrix = generate_taft_mult_matrix(n)
    comult_matrix = generate_taft_comult_matrix(n, mult_matrix)
    counit_vector = generate_taft_counit(n)
    antipode_matrix = generate_taft_antipode_matrix(n)
    taft_algebra = HopfAlgebra(f'Taft_{n}', element_names, mult_matrix, comult_matrix, counit_vector, antipode_matrix)
    return taft_algebra
if __name__ == "__main__":
    n = 3
    g = "g"
    x = "x"
    taft_algebra_instance = create_taft_algebra(n, g, x)
    print(taft_algebra_instance)