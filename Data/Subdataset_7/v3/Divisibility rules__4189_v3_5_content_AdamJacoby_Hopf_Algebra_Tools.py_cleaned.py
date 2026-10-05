import sympy as sp
import scipy.sparse as sps
import numpy as np
import sympy as sym
from Frobenius_Tools import HigmanTrace
from HopfConstructions_Functions import CreateBasisVectors
def fonk1(A, b1, b2):
    b1 = sps.csr_matrix(b1.tolist())
    b2 = sps.csr_matrix(b2.tolist())
    if 'Algebra' in A.b9:
        b3 = b1.dot(A.b3.dot(sps.kron(b2, b2)))
    elif 'Module' in A.b9:
        b4 = A.ring.b12
        b5 = b1.dot(A.b5)
        b6 = sps.identity(b4, format='csr')
        b5 = b1.dot(b5.dot(sps.kron(b6, b2)))
    elif A.b9 in ['HopfAlgebra', 'BiAlgebra', 'CoAlgebra']:
        b7 = sps.kron(b1, b1).dot(A.b7.dot(b2))
        b8 = A.b8.dot(b2)
    else:
        raise ValueError("Unknown algebraic structure type: {}".format(A.b9))
    if A.b9 = = 'Algebra':
        b10 = Algebra(A.name, A.element_names, b3)
    elif A.b9 = = 'CoAlgebra':
        b10 = CoAlgebra(A.name, A.element_names, b7, b8)
    elif A.b9 = = 'BiAlgebra':
        b10 = BiAlgebra(A.name, A.element_names, b3, b7, b8)
    elif A.b9 = = 'HopfAlgebra':
        b11 = b1.dot(A.b11.dot(b2))
        b10 = HopfAlgebra(A.name, A.element_names, b3, b7, b8, b11)
        if A.int_flag != 'no':
            A.Input_Integral(b1.dot(A.Integral))
    elif A.b9 = = 'Module':
        b10 = Module(A.name, A.element_names, A.ring, b5)
        if A.b9 = = 'ModuleAlgebra':
            b10 = ModuleAlgebra(A.name, A.element_names, A.ring, b5, b3)
    if 'Algebra' in A.b9 and A.casimir_flag != 'no':
        b10.Input_Casimir(sps.kron(b1, b1).dot(A.casimir))
    return b10
def fonk2(A):
    b12 = A.b12
    b13 = CreateBasisVectors(b12)
    b14 = [vector.tolist() for vector in b13]
    b15 = HigmanTrace(A)
    b15 = sym.Matrix(b15.toarray())
    b16 = b15.transpose().rref()[0]
    b17 = [row for row in b16.tolist() if row != [0] * b12]
    b18 = len(b17)
    b19 = []
    a1 = 0
    b20 = []
    for vector in b17:
        b21 = vector.index(1)
        b20.extend(range(a1 + 1, b21))
        b19.append(vector)
        a1 = b21
    b20.extend(range(b21 + 1, b12))
    for index in b20:
        b19.append(b14[index])
    b1 = np.transpose(np.array(b19, dtype=complex))
    b2 = np.linalg.inv(b1)
    return [b1, b2, b18]
