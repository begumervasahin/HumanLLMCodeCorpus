from ExampleGroup_Functions import *
from HopfClass import HopfAlgebra
import numpy as np
import scipy.sparse as sps
from itertools import product
def dihedral_group_mult_matrix(n):
    dim = 2 * n
    mult = np.zeros((dim, dim**2), dtype=complex)
    for i, j, k, l in product(range(n), [0, 1], repeat=2):
        row = 2 * ((i + ((-1) ** j) * k) % n) + (j + l) % 2
        col = dim * (i * 2 + j) + 2 * k + l
        mult[row, col] = 1
    return sps.csr_matrix(mult)
def dihedral_group_antipode(n):
    dim = 2 * n
    antipode = np.zeros((dim, dim), dtype=complex)
    for i, j in product(range(n), [0, 1]):
        row = 2 * (((-1) ** (j + 1) * i) % n) + j
        col = i * 2 + j
        antipode[row, col] = 1
    return sps.csr_matrix(antipode)
def dihedral_group_element_names(n, ele_name_g, ele_name_x):
    element_names = [f"{ele_name_g}^{i}{ele_name_x}^{j}" for i in range(n) for j in [0, 1]]
    return element_names
def dihedral_group(n, element_name_g, element_name_x):
    dim = 2 * n
    mult = dihedral_group_mult_matrix(n)
    comult = Group_Comult_Matrix(dim)
    counit = Group_Counit(dim)
    intg = Group_Integral(dim)
    antipode = dihedral_group_antipode(n)
    name = f"D_{n}"
    element_names = dihedral_group_element_names(n, element_name_g, element_name_x)
    dihedral_group = HopfAlgebra(name, element_names, mult, comult, counit, antipode)
    dihedral_group.Input_Integral(intg)
    return dihedral_group