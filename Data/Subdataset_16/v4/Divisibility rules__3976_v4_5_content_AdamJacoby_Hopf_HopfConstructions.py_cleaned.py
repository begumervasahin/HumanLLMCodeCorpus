import scipy.sparse as sps
import numpy as np
from HopfConstructions_Functions import (
    Tensor_Mult, Tensor_Comult, Drinfeld_Twist_Comult, Drinfeld_Twist_Antipode,
    Left_Adjoint_Action, Left_Smash_Product_Mult, Left_Smash_Element_Names,
    Tensor_Type, Dual_Element_Names
)
from HopfClass import HopfAlgebra, BiAlgebra, Algebra, CoAlgebra, ModuleAlgebra
from Frobenius_Tools import HigmanTrace
def fonk1(A, B):
    b1 = Tensor_Type(A, B)
    b2 = f"{A.b2}(T){B.b2}"
    b3 = [f"{A.b3[iA]}(T){B.b3[iB]}" for iA in range(A.dim) for iB in range(B.dim)]
    if b1 = = 'HopfAlgebra':
        b4 = Tensor_Mult(A, B)
        b5 = Tensor_Comult(A, B)
        b6 = np.kron(A.b6, B.b6)
        b7 = sps.kron(A.b7, B.b7)
        b8 = HopfAlgebra(b2, b3, b4, b5, b6, b7)
        if A.int_flag != 'no' and B.int_flag != 'no':
            b8.Input_Integral(np.kron(A.int, B.int))
    elif b1 = = 'BiAlgebra':
        b4 = Tensor_Mult(A, B)
        b5 = Tensor_Comult(A, B)
        b6 = np.kron(A.b6, B.b6)
        b8 = BiAlgebra(b2, b3, b4, b5, b6)
    elif b1 = = 'Algebra':
        b4 = Tensor_Mult(A, B)
        b8 = Algebra(b2, b3, b4)
    elif b1 = = 'CoAlgebra':
        b5 = Tensor_Comult(A, B)
        b6 = np.kron(A.b6, B.b6)
        b8 = CoAlgebra(b2, b3, b5, b6)
    return b8
def fonk2(H, J, JI, twist_name):
    b5 = Drinfeld_Twist_Comult(H, J, JI)
    b2 = f"{H.b2}({twist_name})"
    b7 = Drinfeld_Twist_Antipode(H, J, JI)
    b8 = HopfAlgebra(b2, H.b3, H.b4, b5, H.b6, b7)
    b8.Input_Integral(H.int)
    return b8
def fonk3(H):
    b9 = Left_Adjoint_Action(H)
    return ModuleAlgebra(f'ad{H.b2}', H.b2, b9, H.b3, H.b4)
def fonk4(A, H):
    b4 = Left_Smash_Product_Mult(A, H)
    b3 = Left_Smash_Element_Names(A, H)
    return Algebra(f"{A.b2}(
def fonk5(H):
    b4 = H.b5.transpose()
    b5 = H.b5.transpose()
    b7 = H.b7.transpose()
    b3 = Dual_Element_Names(H.b3)
    b6 = np.zeros(H.dim, dtype=complex)
    b6[0] = 1
    return HopfAlgebra(f"{H.b2}^*", b3, b4, b5, b6, b7)
if b10 = = "__main__":
    pass