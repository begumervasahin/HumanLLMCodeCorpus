import numpy as np
import scipy.sparse as sps
import sympy as sym
from HopfClass import Algebra, CoAlgebra, BiAlgebra, HopfAlgebra, Module, ModuleAlgebra
from Frobenius_Tools import HigmanTrace
from HopfConstructions_Functions import CreateBasisVectors
def change_basis(alg, U, UI):
    U = sps.csr_matrix(U.tolist())
    UI = sps.csr_matrix(UI.tolist())
    if 'Algebra' in alg._type:
        mult = U.dot(alg.mult.dot(sps.kron(UI, UI)))
    if 'Module' in alg._type:
        ring_dim = alg.ring.dim
        action = U.dot(alg.action)
        ring_id = sps.identity(ring_dim, format='csr')
        action = U.dot(action.dot(sps.kron(ring_id, UI)))
    if alg._type in ['HopfAlgebra', 'BiAlgebra', 'CoAlgebra']:
        comult = sps.kron(U, U).dot(alg.comult.dot(UI))
        counit = alg.counit.dot(UI)
    if alg._type == 'Algebra':
        return Algebra(alg.name, alg.element_names, mult)
    if alg._type == 'CoAlgebra':
        return CoAlgebra(alg.name, alg.element_names, comult, counit)
    if alg._type == 'BiAlgebra':
        return BiAlgebra(alg.name, alg.element_names, mult, comult, counit)
    if alg._type == 'HopfAlgebra':
        antipode = U.dot(alg.antipode.dot(UI))
        result = HopfAlgebra(alg.name, alg.element_names, mult, comult, counit, antipode)
        if alg.int_flag != 'no':
            alg.Input_Integral(U.dot(alg.Integral))
        return result
    if alg._type == 'Module':
        module = Module(alg.name, alg.element_names, alg.ring, action)
        if isinstance(alg, ModuleAlgebra):
            return ModuleAlgebra(alg.name, alg.element_names, alg.ring, action, mult)
    if 'Algebra' in alg._type and alg.casimir_flag != 'no':
        alg.Input_Casimir(sps.kron(U, U).dot(alg.casimir))
    return alg
def center(alg):
    dim = alg.dim
    basis_vectors = CreateBasisVectors(dim)
    V = [vector.tolist() for vector in basis_vectors]
    higman_trace = HigmanTrace(alg)
    trace_matrix = sym.Matrix(higman_trace.toarray())
    rref_matrix, _ = trace_matrix.transpose().rref()
    rref_matrix = rref_matrix.tolist()
    rref_matrix = [row for row in rref_matrix if row != [0] * dim]
    center_dim = len(rref_matrix)
    change_of_basis = []
    past_index = 0
    complement = []
    for vector in rref_matrix:
        current_index = vector.index(1)
        complement.extend(range(past_index + 1, current_index))
        change_of_basis.append(vector)
        past_index = current_index
    complement.extend(range(current_index + 1, dim))
    change_of_basis.extend([V[index] for index in complement])
    U = np.transpose(np.array(change_of_basis, dtype=complex))
    UI = np.linalg.inv(U)
    return [U, UI, center_dim]
if __name__ == '__main__':
    algebra = Algebra(name="ExampleAlgebra", element_names=["e1", "e2"], multiplication_matrix=np.array([[1, 0], [0, 1]]))
    U = np.random.rand(2, 2)
    UI = np.linalg.inv(U)
    changed_basis = change_basis(algebra, U, UI)
    center_result = center(algebra)
    print("Changed Basis:", changed_basis)
    print("Center Result:", center_result)