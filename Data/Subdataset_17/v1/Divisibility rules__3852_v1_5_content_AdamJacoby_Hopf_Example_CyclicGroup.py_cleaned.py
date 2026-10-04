import numpy as np
import scipy.sparse as sps
from itertools import product
from ExampleGroup_Functions import Group_Comult_Matrix, Group_Counit, Group_Integral
from HopfClass import HopfAlgebra
def CyclicGroup_Mult_Matrix(dim):
    mult = np.zeros((dim, dim**2), dtype=complex)
    N = range(dim)
    for i, j in product(N, N):
        mult[(i + j) % dim, i * dim + j] = 1
    mult = sps.csr_matrix(mult, dtype=complex)
    return mult
def CyclicGroup_Antipode(dim):
    antipode = np.zeros((dim, dim), dtype=complex)
    for i in range(dim):
        antipode[i, (-i) % dim] = 1
    antipode = sps.csr_matrix(antipode, dtype=complex)
    return antipode
def CyclicGroup_Element_Names(dim, ele_name):
    return [f"{ele_name}^{i}" for i in range(dim)]
def CyclicGroup(dim, element_name):
    mult = CyclicGroup_Mult_Matrix(dim)
    comult = Group_Comult_Matrix(dim)
    counit = Group_Counit(dim)
    integral = Group_Integral(dim)
    antipode = CyclicGroup_Antipode(dim)
    name = f"C_{dim}"
    element_names = CyclicGroup_Element_Names(dim, element_name)
    cyclic_group = HopfAlgebra(name, element_names, mult, comult, counit, antipode)
    cyclic_group.Input_Integral(integral)
    return cyclic_group
if __name__ == "__main__":
    dim = 5
    element_name = "g"
    cyclic_group = CyclicGroup(dim, element_name)
    print(cyclic_group)