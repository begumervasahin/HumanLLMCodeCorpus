from ExampleGroup_Functions import *
from HopfClass import HopfAlgebra
import numpy as np
import scipy.sparse as sps
from itertools import product
def generate_generalized_dihedral_mult_matrix(p, q, r):
    dim = p * q
    mult = np.zeros((dim, dim**2), dtype=complex)
    for i, j in product(range(q), range(p)):
        for k, l in product(range(q), range(p)):
            row = p * ((i + r * k) % q) + (k + l) % p
            col = dim * (i * p + j) + p * k + l
            mult[row, col] = 1
    return sps.csr_matrix(mult, dtype=complex)
def generate_generalized_dihedral_antipode(p, q, r):
    dim = p * q
    antipode = np.zeros((dim, dim), dtype=complex)
    for i, j in product(range(q), range(p)):
        inv = (((r**j) % q)**(q - 2)) % q
        row = ((-i * inv) % q) * p + ((-j) % p)
        col = i * p + j
        antipode[row, col] = 1
    return sps.csr_matrix(antipode, dtype=complex)
def generate_generalized_dihedral_element_names(p, q, ele_name_g, ele_name_x):
    element_names = [f"{ele_name_g}^{i}{ele_name_x}^{j}" for i in range(q) for j in range(p)]
    return element_names
def create_generalized_dihedral_group(p, q, r, element_name_g, element_name_x):
    dim = p * q
    mult = generate_generalized_dihedral_mult_matrix(p, q, r)
    comult = Group_Comult_Matrix(dim)
    counit = Group_Counit(dim)
    integral = Group_Integral(dim)
    antipode = generate_generalized_dihedral_antipode(p, q, r)
    name = f'B_{p},{q},{r}'
    element_names = generate_generalized_dihedral_element_names(p, q, element_name_g, element_name_x)
    group = HopfAlgebra(name, element_names, mult, comult, counit, antipode)
    group.Input_Integral(integral)
    return group
p = 3
q = 2
r = 1
element_name_g = 'g'
element_name_x = 'x'
group = create_generalized_dihedral_group(p, q, r, element_name_g, element_name_x)