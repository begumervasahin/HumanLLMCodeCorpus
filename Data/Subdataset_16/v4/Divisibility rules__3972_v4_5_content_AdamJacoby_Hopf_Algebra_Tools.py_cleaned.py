import numpy as np
import scipy.sparse as sps
import sympy as sym
from HopfClass import Algebra, CoAlgebra, BiAlgebra, HopfAlgebra, Module, ModuleAlgebra
from Frobenius_Tools import HigmanTrace
from HopfConstructions_Functions import CreateBasisVectors
def fonk1(alg, b1, b2):
    b1 = sps.csr_matrix(b1.tolist())
    b2 = sps.csr_matrix(b2.tolist())
    if 'Algebra' in alg.b9:
        b3 = b1.dot(alg.b3.dot(sps.kron(b2, b2)))
    if 'Module' in alg.b9:
        b4 = alg.ring.b13
        b5 = b1.dot(alg.b5)
        b6 = sps.identity(b4, format='csr')
        b5 = b1.dot(b5.dot(sps.kron(b6, b2)))
    if alg.b9 in ['HopfAlgebra', 'BiAlgebra', 'CoAlgebra']:
        b7 = sps.kron(b1, b1).dot(alg.b7.dot(b2))
        b8 = alg.b8.dot(b2)
    if alg.b9 = = 'Algebra':
        return Algebra(alg.name, alg.element_names, b3)
    if alg.b9 = = 'CoAlgebra':
        return CoAlgebra(alg.name, alg.element_names, b7, b8)
    if alg.b9 = = 'BiAlgebra':
        return BiAlgebra(alg.name, alg.element_names, b3, b7, b8)
    if alg.b9 = = 'HopfAlgebra':
        b10 = b1.dot(alg.b10.dot(b2))
        b11 = HopfAlgebra(alg.name, alg.element_names, b3, b7, b8, b10)
        if alg.int_flag != 'no':
            alg.Input_Integral(b1.dot(alg.Integral))
        return b11
    if alg.b9 = = 'Module':
        b12 = Module(alg.name, alg.element_names, alg.ring, b5)
        if isinstance(alg, ModuleAlgebra):
            return ModuleAlgebra(alg.name, alg.element_names, alg.ring, b5, b3)
    if 'Algebra' in alg.b9 and alg.casimir_flag != 'no':
        alg.Input_Casimir(sps.kron(b1, b1).dot(alg.casimir))
    return alg
def fonk2(alg):
    b13 = alg.b13
    b14 = CreateBasisVectors(b13)
    b15 = [vector.tolist() for vector in b14]
    b16 = HigmanTrace(alg)
    b17 = sym.Matrix(b16.toarray())
    b19, b18 = b17.transpose().rref()
    b19 = b19.tolist()
    b19 = [row for row in b19 if row != [0] * b13]
    b20 = len(b19)
    b21 = []
    a1 = 0
    b22 = []
    for vector in b19:
        b23 = vector.index(1)
        b22.extend(range(a1 + 1, b23))
        b21.append(vector)
        a1 = b23
    b22.extend(range(b23 + 1, b13))
    b21.extend([b15[index] for index in b22])
    b1 = np.transpose(np.array(b21, dtype=complex))
    b2 = np.linalg.inv(b1)
    return [b1, b2, b20]
if b24 = = '__main__':
    b25 = Algebra(name="ExampleAlgebra", element_names=["e1", "e2"], multiplication_matrix=np.array([[1, 0], [0, 1]]))
    b1 = np.random.rand(2, 2)
    b2 = np.linalg.inv(b1)
    b26 = fonk1(b25, b1, b2)
    b27 = fonk2(b25)
    print("Changed Basis:", b26)
    print("Center Result:", b27)