from ExampleGroup_Functions import *
from HopfClass import HopfAlgebra
import numpy as np
import scipy.sparse as sps
from itertools import product
def create_cyclic_group_mult_matrix(dim):
    mult = np.zeros((dim, dim**2), dtype=complex)
    for i, j in product(range(dim), repeat=2):
        mult[(i + j) % dim, i * dim + j] = 1
    mult = sps.csr_matrix(mult, dtype=complex)
    return mult
def create_cyclic_group_antipode(dim):
    antipode = np.zeros((dim, dim), dtype=complex)
    for i in range(dim):
        antipode[i, (-i) % dim] = 1
    antipode = sps.csr_matrix(antipode, dtype=complex)
    return antipode
def generate_cyclic_group_element_names(dim, element_name):
    return [f"{element_name}^{i}" for i in range(dim)]
def create_cyclic_group(dim, element_name):
    mult = create_cyclic_group_mult_matrix(dim)
    comult = Group_Comult_Matrix(dim)
    counit = Group_Counit(dim)
    intg = Group_Integral(dim)
    antipode = create_cyclic_group_antipode(dim)
    name = f"C_{dim}"
    element_names = generate_cyclic_group_element_names(dim, element_name)
    cyclic_group = HopfAlgebra(name, element_names, mult, comult, counit, antipode)
    cyclic_group.Input_Integral(intg)
    return cyclic_group
dim = 4
element_name = 'a'
cyclic_group = create_cyclic_group(dim, element_name)
print(cyclic_group)