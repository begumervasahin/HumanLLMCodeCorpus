import sympy as sp
import scipy.sparse as sps
import numpy as np
import sympy as sym
from Frobenius_Tools import HigmanTrace
from HopfConstructions_Functions import CreateBasisVectors
def fonk1(A, b1, b2):
    b1 = sps.csr_matrix(b1.tolist())
    b2 = sps.csr_matrix(b2.tolist())
    if 'Algebra' in A.b7:
        b3 = b1.dot(A.b3.dot(sps.kron(b2, b2)))
    if 'Module' in A.b7:
        b4 = self.ring.b12
        b5 = b1.dot(A.b5)
        b6 = sps.Identity(b4, format='csr')
        b5 = b1.dot(b5.dot(sps.kron(b6, b2)))
    if A.b7 = = 'HopfAlgebra' or A.b7 == 'BiAlgebra' or A.b7 == 'CoAlgebra':
        b8 = sps.kron(b1, b1).dot(A.b8.dot(b2))
        b9 = A.b9.dot(b2)
    if A.b7 = = 'Algebra':
        b10 = Algebra(A.name, A.element_names, b3)
    if A.b7 = = 'CoAlgebra':
        b10 = CoAlgebra(A.name, A.element_names, b8, b9)
    if A.b7 = = 'BiAlgebra':
        b10 = BiAlgebra(A.name, A.element_names, b3, b8, b9)
    if A.b7 = = 'HopfAlgebra':
        b11 = b1.dot(A.b11.dot(b2))
        b10 = HopfAlgebra(A.name, A.element_names, b3, b8, b9, b11)
        if A.int_flag != 'no':
            A.Input_Integral(b1.dot(A.Integral))
    if A.b7 = = 'Module':
        b10 = Module(A.name, A.element_names, A.ring, b5)
        if A.b7 = = 'ModuleAlgebra':
            b10 = ModuleAlgebra(A.name, A.element_names, A.ring, b5, b3)
    if 'Algebra' in A.b7 and A.casimir_flag != 'no':
        b10.Input_Casimir(sps.kron(b1, b1).dot(A.casimir))
    return b10
def fonk2(A):
    b12 = A.b12
    b13 = CreateBasisVectors(b12)
    b14 = []
    for vector in b13:
        b14.append(vector.tolist())
    b15 = HigmanTrace(A)
    b15 = sym.Matrix(b15.toarray())
    b16 = b15.transpose().rref()
    b16 = b16[0]
    b17 = b16.tolist()
    b17 = filter(lambda a: a != [0] * b12, b17)
    b18 = len(b17)
    b19 = []
    a1 = 0
    b20 = []
    for vector in b17:
        b21 = vector.index(1)
        for i in range(a1 + 1, b21):
            b20.append(i)
        b19.append(vector)
        a1 = b21
    for i in range(b21 + 1, b12):
        b20.append(i)
    for index in b20:
        b19.append(b14[index])
    b1 = np.transpose(np.array(b19, dtype=complex))
    b2 = np.linalg.inv(b1)
    return [b1, b2, b18]
