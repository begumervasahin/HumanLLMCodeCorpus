import scipy.sparse as sps
import numpy as np
from HopfConstructions_Functions import (
    Tensor_Mult,
    Tensor_Comult,
    Drinfeld_Twist_Comult,
    Drinfeld_Twist_Antipode,
    Left_Adjoint_Action,
    Left_Smash_Product_Mult,
    Left_Smash_Element_Names,
    Tensor_Type,
    Dual_Element_Names,
)
from HopfClass import HopfAlgebra, BiAlgebra, Algebra, CoAlgebra, ModuleAlgebra
def tensor_product(A, B):
    _type = Tensor_Type(A, B)
    name = f"{A.name}(T){B.name}"
    element_names = [f"{A.element_names[iA]}(T){B.element_names[iB]}" for iA in range(A.dim) for iB in range(B.dim)]
    if _type == 'HopfAlgebra':
        mult = Tensor_Mult(A, B)
        comult = Tensor_Comult(A, B)
        counit = np.kron(A.counit, B.counit)
        antipode = sps.kron(A.antipode, B.antipode)
        result = HopfAlgebra(name, element_names, mult, comult, counit, antipode)
        if A.int_flag != 'no' and B.int_flag != 'no':
            result.Input_Integral(np.kron(A.int, B.int))
    elif _type == 'BiAlgebra':
        mult = Tensor_Mult(A, B)
        comult = Tensor_Comult(A, B)
        counit = np.kron(A.counit, B.counit)
        result = BiAlgebra(name, element_names, mult, comult, counit)
    elif _type == 'Algebra':
        mult = Tensor_Mult(A, B)
        result = Algebra(name, element_names, mult)
    elif _type == 'CoAlgebra':
        comult = Tensor_Comult(A, B)
        counit = np.kron(A.counit, B.counit)
        result = CoAlgebra(name, element_names, comult, counit)
    return result
def drinfeld_twist(H, J, JI, twist_name):
    comult = Drinfeld_Twist_Comult(H, J, JI)
    name = f"{H.name}({twist_name})"
    antipode = Drinfeld_Twist_Antipode(H, J, JI)
    result = HopfAlgebra(name, H.element_names, H.mult, comult, H.counit, antipode)
    result.Input_Integral(H.int)
    return result
def left_adjoint_module(H):
    action = Left_Adjoint_Action(H)
    return ModuleAlgebra(f'ad{H.name}', H.name, action, H.element_names, H.mult)
def left_smash_product(A, H):
    mult = Left_Smash_Product_Mult(A, H)
    ele_names = Left_Smash_Element_Names(A, H)
    return Algebra(f"{A.name}(
def dual_hopf_algebra(H):
    mult = H.comult.transpose()
    comult = H.comult.transpose()
    antipode = H.antipode.transpose()
    element_names = Dual_Element_Names(H.element_names)
    counit = np.zeros((H.dim), dtype=complex)
    counit[0] = 1
    return HopfAlgebra(f"{H.name}^*", element_names, mult, comult, counit, antipode)
if __name__ == "__main__":
    pass