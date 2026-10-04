import numpy as np
import scipy.sparse as sps
from itertools import product
from ExampleGroup_Functions import Group_Comult_Matrix, Group_Counit, Group_Integral
from HopfClass import HopfAlgebra
def cyclic_group_mult_matrix(dim):
    mult = np.zeros((dim, dim**2), dtype=complex)
    for i, j in product(range(dim), repeat=2):
        mult[(i + j) % dim, i * dim + j] = 1
    return sps.csr_matrix(mult, dtype=complex)
def cyclic_group_antipode(dim):
    antipode = np.zeros((dim, dim), dtype=complex)
    for i in range(dim):
        antipode[i, (-i) % dim] = 1
    return sps.csr_matrix(antipode, dtype=complex)
def cyclic_group_element_names(dim, ele_name):
    return [f"{ele_name}^{i}" for i in range(dim)]
def cyclic_group(dim, element_name):
    mult = cyclic_group_mult_matrix(dim)
    comult = Group_Comult_Matrix(dim)
    counit = Group_Counit(dim)
    integral = Group_Integral(dim)
    antipode = cyclic_group_antipode(dim)
    name = f"C_{dim}"
    element_names = cyclic_group_element_names(dim, element_name)
    cyclic_group = HopfAlgebra(name, element_names, mult, comult, counit, antipode)
    cyclic_group.Input_Integral(integral)
    return cyclic_group
if __name__ == "__main__":
    dim = 5
    element_name = "g"
    cyclic_group = cyclic_group(dim, element_name)
    print(cyclic_group)