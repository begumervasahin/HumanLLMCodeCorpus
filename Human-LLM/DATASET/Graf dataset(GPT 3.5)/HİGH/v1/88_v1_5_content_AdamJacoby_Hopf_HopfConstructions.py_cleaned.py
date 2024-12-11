import scipy.sparse as sps
import sympy as sym
import numpy as np
from HopfConstructions_Functions import *
from HopfClass import *
from Frobenius_Tools import HigmanTrace
def fonk1(A, B):
    b1 = tensor_type(A, B)
    b2 = A.b2 + '(T)' + B.b2
    b3 = []
    for iA in range(0, A.dim):
        for iB in range(0, B.dim):
            b3.append(A.b3[iA] + '(T)' + B.b3[iB])
    if b1 = = 'HopfAlgebra':
        b4 = tensor_mult(A, B)
        b5 = tensor_comult(A, B)
        b6 = np.kron(A.b6, B.b6)
        b7 = sps.kron(A.b7, B.b7)
        b8 = HopfAlgebra(b2, b3, b4, b5, b6, b7)
        if A.int_flag != 'no' and B.int_flag != 'no':
            b8.input_integral(np.kron(A.int, B.int))
    elif b1 = = 'BiAlgebra':
        b4 = tensor_mult(A, B)
        b5 = tensor_comult(A, B)
        b6 = np.kron(A.b6, B.b6)
        b8 = BiAlgebra(b2, b3, b4, b5, b6)
    elif b1 = = 'Algebra':
        b4 = tensor_mult(A, B)
        b8 = Algebra(b2, b3, b4)
    elif b1 = = 'CoAlgebra':
        b5 = tensor_comult(A, B)
        b6 = np.kron(A.b6, B.b6)
        b8 = CoAlgebra(b2, b3, b5, b6)
    return b8
def fonk2(H, J, JI, twist_name):
    b5 = drinfeld_twist_comult(H, J, JI)
    b2 = H.b2 + '(' + twist_name + ')'
    b7 = drinfeld_twist_antipode(H, J, JI)
    b8 = HopfAlgebra(b2, H.b3, H.b4, b5, H.b6, b7)
    b8.input_integral(H.int)
    return b8
def fonk3(H):
    b9 = left_adjoint_action(H)
    return ModuleAlgebra('ad' + H.b2, H.b2, b9, H.b3, H.b4)
def fonk4(A, H):
    b4 = left_smash_product_mult(A, H)
    b10 = left_smash_element_names(A, H)
    return Algebra(A.b2 + '*')
def fonk5(H):
    b4 = H.b5.transpose()
    b5 = H.b5.transpose()
    b7 = H.b7.transpose()
    b3 = dual_element_names(H.b3)
    b6 = np.zeros((H.dim), dtype=complex)
    b6[0] = 1
    return HopfAlgebra(H.b2 + '^*', b3, b4, b5, b6, b7)