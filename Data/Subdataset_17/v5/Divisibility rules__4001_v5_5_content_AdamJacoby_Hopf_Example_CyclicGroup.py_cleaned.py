import numpy as np
import scipy.sparse as sps
from itertools import product
from ExampleGroup_Functions import Group_Comult_Matrix, Group_Counit, Group_Integral
from HopfClass import HopfAlgebra
def generate_mult_matrix(dim):
    mult = np.zeros((dim, dim**2), dtype=complex)
    for i, j in product(range(dim), repeat=2):
        mult[(i + j) % dim, i * dim + j] = 1
    return sps.csr_matrix(mult, dtype=complex)
def generate_antipode_matrix(dim):
    antipode = np.zeros((dim, dim), dtype=complex)
    for i in range(dim):
        antipode[i, (-i) % dim] = 1
    return sps.csr_matrix(antipode, dtype=complex)
def generate_element_names(dim, base_name):
    return [f"{base_name}^{i}" for i in range(dim)]
def create_cyclic_group(dim, element_name):
    mult_matrix = generate_mult_matrix(dim)
    comult_matrix = Group_Comult_Matrix(dim)
    counit_matrix = Group_Counit(dim)
    integral_matrix = Group_Integral(dim)
    antipode_matrix = generate_antipode_matrix(dim)
    name = f"C_{dim}"
    element_names = generate_element_names(dim, element_name)
    cyclic_group = HopfAlgebra(name, element_names, mult_matrix, comult_matrix, counit_matrix, antipode_matrix)
    cyclic_group.Input_Integral(integral_matrix)
    return cyclic_group
if __name__ == "__main__":
    dim = 5
    element_name = "g"
    cyclic_group_instance = create_cyclic_group(dim, element_name)
    print(cyclic_group_instance)