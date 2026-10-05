from HopfClass import HopfAlgebra
import numpy as np
import scipy.sparse as sps
from itertools import product
def taft_element_names(n, g, x):
    elements = []
    for i in range(n):
        for j in range(n):
            elements.append(f"{g}^{j}{x}^{i}")
    return elements
def taft_mult_matrix(n):
    poly = [0] * (n + 1)
    poly[0] = 1
    poly[n] = -1
    omega = np.roots(poly)
    mult_matrix = np.zeros((n ** 2, n ** 4), dtype=complex)
    for i, j, k in product(range(n), repeat=3):
        for l in range(n - j):
            mult_matrix[((i + k) % n) + n * (j + l), i + n * j + (k + n * l) * n ** 2] = omega[(n - 1) - (-j * k) % n]
    return sps.csr_matrix(mult_matrix)
def taft_comult_matrix(n, mult):
    dim = n ** 2
    comult_matrix = np.zeros((dim ** 2, dim), dtype=complex)
    x_plus_g = np.zeros(dim)
    x_plus_g[1] = 1
    x_plus_g[n] = 1
    temp = np.zeros(dim)
    temp[0] = 1
    products = [temp]
    for i in range(1, n):
        temp2 = np.kron(temp, x_plus_g)
        temp = mult.dot(temp2)
        products.append(temp)
    for i, j in product(range(1, n), repeat=2):
        for l in range(j + 1):
            comult_matrix[((i + l) % n) + (j - l) * n + (i + n * l) * dim, i + j * n] = products[j][l + (j - l) * n]
    return comult_matrix
def taft_counit_vector(n):
    return np.ones(n, dtype=complex)
def taft_antipode_matrix(n):
    dim = n ** 2
    poly = [0] * (n + 1)
    poly[0] = 1
    poly[n] = -1
    omega = np.roots(poly)
    antipode_matrix = np.zeros((dim, dim), dtype=complex)
    for i, j in product(range(n), repeat=2):
        antipode_matrix[((-i) % n) + j * n, i + j * n] = (-1) ** j * omega[(i * j) % n]
    return sps.csr_matrix(antipode_matrix)
n = 3
g = 'g'
x = 'x'
element_names = taft_element_names(n, g, x)
mult_matrix = taft_mult_matrix(n)
comult_matrix = taft_comult_matrix(n, mult_matrix)
counit_vector = taft_counit_vector(n)
antipode_matrix = taft_antipode_matrix(n)
taft_algebra = HopfAlgebra("TaftAlgebra", element_names, mult_matrix, comult_matrix, counit_vector, antipode_matrix)