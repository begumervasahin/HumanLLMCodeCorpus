import numpy as np
import scipy.sparse as sps
from itertools import product
from ExampleGroup_Functions import Group_Comult_Matrix, Group_Counit, Group_Integral
from HopfClass import HopfAlgebra
def dihedral_group_mult_matrix(n):
    dim = 2 * n
    mult = np.zeros((dim, dim**2), dtype=complex)
    for i, j in product(range(n), [0, 1]):
        for k, l in product(range(n), [0, 1]):
            mult[2 * ((i + ((-1) ** j) * k) % n) + (j + l) % 2, dim * (i * 2 + j) + 2 * k + l] = 1
    return sps.csr_matrix(mult.tolist(), dtype=complex)
def dihedral_group_antipode(n):
    dim = 2 * n
    antipode = np.zeros((dim, dim), dtype=complex)
    for i, j in product(range(n), [0, 1]):
        antipode[2 * (((-1) ** (j + 1) * i) % n) + j, i * 2 + j] = 1
    return sps.csr_matrix(antipode.tolist(), dtype=complex)
def dihedral_group_element_names(n, ele_name_g, ele_name_x):
    return [f"{ele_name_g}^{i}{ele_name_x}^{j}" for i in range(n) for j in [0, 1]]
def dihedral_group(n, ele_name_g, ele_name_x):
    mult_matrix = dihedral_group_mult_matrix(n)
    comult_matrix = Group_Comult_Matrix(2 * n)
    counit_matrix = Group_Counit(2 * n)
    integral_matrix = Group_Integral(2 * n)
    antipode_matrix = dihedral_group_antipode(n)
    name = f"D_{n}"
    element_names = dihedral_group_element_names(n, ele_name_g, ele_name_x)
    dihedral_group = HopfAlgebra(name, element_names, mult_matrix, comult_matrix, counit_matrix, antipode_matrix)
    dihedral_group.Input_Integral(integral_matrix)
    return dihedral_group
if __name__ == "__main__":
    n = 5
    ele_name_g = "g"
    ele_name_x = "x"
    dihedral_group_instance = dihedral_group(n, ele_name_g, ele_name_x)
    print(dihedral_group_instance)