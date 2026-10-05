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
            mult[p * ((i + r * k) % q) + (k + l) % p, dim * (i * p + j) + p * k + l] = 1
    mult = sps.csr_matrix(mult.tolist(), dtype=complex)
    return mult
def generate_generalized_dihedral_antipode(p, q, r):
    dim = p * q
    antipode = np.zeros((dim, dim), dtype=complex)
    for i, j in product(range(q), range(p)):
        inv = (((r**j) % q)**(q - 2)) % q
        antipode[((-i * inv) % q) * p + ((-j) % p), i * p + j] = 1
    antipode = sps.csr_matrix(antipode.tolist(), dtype=complex)
    return antipode
def generate_generalized_dihedral_element_names(p, q, ele_name_g, ele_name_x):
    out = []
    for i in range(q):
        for j in range(p):
            out.append(ele_name_g + '^' + str(i) + ele_name_x + '^' + str(j))
    return out
def create_generalized_dihedral_group(p, q, r, element_name_g, element_name_x):
    dim = p * q
    mult = generate_generalized_dihedral_mult_matrix(p, q, r)
    comult = group_comult_matrix(dim)
    counit = group_counit(dim)
    integral = group_integral(dim)
    antipode = generate_generalized_dihedral_antipode(p, q, r)
    name = 'B_' + str(p) + ',' + str(q) + ',' + str(r)
    element_names = generate_generalized_dihedral_element_names(p, q, element_name_g, element_name_x)
    group = HopfAlgebra(name, element_names, mult, comult, counit, antipode)
    group.input_integral(integral)
    return group
p = 3
q = 2
r = 1
element_name_g = 'g'
element_name_x = 'x'
group = create_generalized_dihedral_group(p, q, r, element_name_g, element_name_x)