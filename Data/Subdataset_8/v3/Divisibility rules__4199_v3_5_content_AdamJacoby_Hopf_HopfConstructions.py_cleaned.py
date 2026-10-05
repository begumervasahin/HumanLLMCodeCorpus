import scipy.sparse as sps
import numpy as np
from HopfConstructions_Functions import *
from HopfClass import *
from Frobenius_Tools import HigmanTrace
def tensor_product(A, B):
    tensor_type = get_tensor_type(A, B)
    name = f"{A.name}(T){B.name}"
    element_names = [f"{A.element_names[iA]}(T){B.element_names[iB]}"
                     for iA in range(A.dim) for iB in range(B.dim)]
    if tensor_type == 'HopfAlgebra':
        mult = tensor_mult(A, B)
        comult = tensor_comult(A, B)
        counit = np.kron(A.counit, B.counit)
        antipode = sps.kron(A.antipode, B.antipode)
        result = HopfAlgebra(name, element_names, mult, comult, counit, antipode)
        if A.int_flag != 'no' and B.int_flag != 'no':
            result.input_integral(np.kron(A.int, B.int))
    elif tensor_type == 'BiAlgebra':
        mult = tensor_mult(A, B)
        comult = tensor_comult(A, B)
        counit = np.kron(A.counit, B.counit)
        result = BiAlgebra(name, element_names, mult, comult, counit)
    elif tensor_type == 'Algebra':
        mult = tensor_mult(A, B)
        result = Algebra(name, element_names, mult)
    elif tensor_type == 'CoAlgebra':
        comult = tensor_comult(A, B)
        counit = np.kron(A.counit, B.counit)
        result = CoAlgebra(name, element_names, comult, counit)
    return result
def drinfeld_twist(H, J, JI, twist_name):
    comult = drinfeld_twist_comult(H, J, JI)
    name = f"{H.name}({twist_name})"
    antipode = drinfeld_twist_antipode(H, J, JI)
    result = HopfAlgebra(name, H.element_names, H.mult, comult, H.counit, antipode)
    result.input_integral(H.int)
    return result
def left_adjoint_module(H):
    action = left_adjoint_action(H)
    return ModuleAlgebra(f"ad{H.name}", H.name, action, H.element_names, H.mult)
def left_smash_product(A, H):
    mult = left_smash_product_mult(A, H)
    ele_names = left_smash_element_names(A, H)
    return Algebra(f"{A.name}*")
def dual_hopf_algebra(H):
    mult = H.comult.transpose()
    comult = H.comult.transpose()
    antipode = H.antipode.transpose()
    element_names = dual_element_names(H.element_names)
    counit = np.zeros((H.dim), dtype=complex)
    counit[0] = 1
    return HopfAlgebra(f"{H.name}^*", element_names, mult, comult, counit, antipode)