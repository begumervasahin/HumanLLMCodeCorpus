
import numpy as np
import scipy.sparse as sps
from itertools import product
from ExampleGroup_Functions import Group_Comult_Matrix, Group_Counit, Group_Integral
from HopfClass import HopfAlgebra
def generate_generalized_dihedral_mult_matrix(p, q, r):
    dim = p * q
    mult = np.zeros((dim, dim**2), dtype=complex)
    for i, j in product(range(q), range(p)):
        for k, l in product(range(q), range(p)):
            row = p * ((i + r * k) % q) + (k + l) % p
            col = dim * (i * p + j) + p * k + l
            mult[row, col] = 1
    return sps.csr_matrix(mult, dtype=complex)
def generate_generalized_dihedral_antipode_matrix(p, q, r):
    dim = p * q
    antipode = np.zeros((dim, dim), dtype=complex)
    for i, j in product(range(q), range(p)):
        inv = (((r ** j) % q) ** (q - 2)) % q
        row = ((-i * inv) % q) * p + ((-j) % p)
        col = i * p + j
        antipode[row, col] = 1
    return sps.csr_matrix(antipode, dtype=complex)
def generate_generalized_dihedral_element_names(p, q, ele_name_g, ele_name_x):
    return [f"{ele_name_g}^{i}{ele_name_x}^{j}" for i in range(q) for j in range(p)]
def create_generalized_dihedral_group(p, q, r, ele_name_g, ele_name_x):
    dim = p * q
    mult_matrix = generate_generalized_dihedral_mult_matrix(p, q, r)
    comult_matrix = Group_Comult_Matrix(dim)
    counit_matrix = Group_Counit(dim)
    integral_matrix = Group_Integral(dim)
    antipode_matrix = generate_generalized_dihedral_antipode_matrix(p, q, r)
    name = f"B_{p},{q},{r}"
    element_names = generate_generalized_dihedral_element_names(p, q, ele_name_g, ele_name_x)
    generalized_dihedral_group = HopfAlgebra(name, element_names, mult_matrix, comult_matrix, counit_matrix, antipode_matrix)
    generalized_dihedral_group.Input_Integral(integral_matrix)
    return generalized_dihedral_group
if __name__ == "__main__":
    p = 3
    q = 4
    r = 2
    ele_name_g = "g"
    ele_name_x = "x"
    generalized_dihedral_group_instance = create_generalized_dihedral_group(p, q, r, ele_name_g, ele_name_x)
    print(generalized_dihedral_group_instance)