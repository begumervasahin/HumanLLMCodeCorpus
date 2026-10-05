from ExampleGroup_Functions import *
from HopfClass import HopfAlgebra
import numpy as np
import scipy.sparse as sps
from itertools import product
def create_dihedral_group_mult_matrix(n):
    dim = 2 * n
    mult = np.zeros((dim, dim**2), dtype=complex)
    for i, j, k, l in product(range(n), [0, 1], repeat=2):
        mult[2 * ((i + ((-1) ** j) * k) % n) + (j + l) % 2, dim * (i * 2 + j) + 2 * k + l] = 1
    mult_sparse = sps.csr_matrix(mult, dtype=complex)
    return mult_sparse
def create_dihedral_group_antipode(n):
    dim = 2 * n
    antipode = np.zeros((dim, dim), dtype=complex)
    for i, j in product(range(n), [0, 1]):
        antipode[2 * (((-1) ** (j + 1) * i) % n) + j, i * 2 + j] = 1
    antipode_sparse = sps.csr_matrix(antipode, dtype=complex)
    return antipode_sparse
def generate_dihedral_group_element_names(n, ele_name_g, ele_name_x):
    element_names = [f"{ele_name_g}^{i}{ele_name_x}^{j}" for i in range(n) for j in [0, 1]]
    return element_names
def create_dihedral_group(n, element_name_g, element_name_x):
    dim = 2 * n
    mult = create_dihedral_group_mult_matrix(n)
    comult = Group_Comult_Matrix(dim)
    counit = Group_Counit(dim)
    intg = Group_Integral(dim)
    antipode = create_dihedral_group_antipode(n)
    name = f"D_{n}"
    element_names = generate_dihedral_group_element_names(n, element_name_g, element_name_x)
    dihedral_group = HopfAlgebra(name, element_names, mult, comult, counit, antipode)
    dihedral_group.Input_Integral(intg)
    return dihedral_group
n = 3
element_name_g = 'g'
element_name_x = 'x'
dihedral_group = create_dihedral_group(n, element_name_g, element_name_x)
print(dihedral_group)