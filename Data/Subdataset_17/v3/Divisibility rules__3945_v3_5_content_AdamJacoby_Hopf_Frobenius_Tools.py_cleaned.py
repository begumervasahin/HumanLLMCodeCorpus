import scipy.sparse as sps
import sympy as sp
import numpy as np
from itertools import product
from math import floor
from HopfConstructions_Functions import Left_Action_Matrix, Right_Action_Matrix, CreateBasisVectors, Tensor_Mult
def char_poly(M):
    matrix = sp.SparseMatrix(M.toarray())
    return matrix.berkowitz_charpoly()
def multiplicity(poly, root, derivatives):
    D = derivatives
    i = 1
    while True:
        if i < len(D):
            if D[i].eval(root) != 0:
                return [i, D]
        else:
            temp = D[-1].diff()
            D.append(temp)
            if temp.eval(root) != 0:
                return [i, D]
        i += 1
def divisors(n):
    return [i for i in range(1, floor(n**0.5) + 1) if n % i == 0]
def remove_zeros_at_zero(poly):
    monomial = poly.EM().as_expr()
    return sp.exquo(poly, monomial)
def higman_trace(A):
    dim = A.dim
    if A.casimir_flag == 'no':
        A.GetCasimir()
    mult = A.mult
    V = CreateBasisVectors(dim)
    casimir = A.casimir
    higman_trace = sps.csr_matrix((dim, dim))
    for i, j in product(range(dim), repeat=2):
        if casimir[dim * i + j] != 0:
            higman_trace += Left_Action_Matrix(V[i], mult).dot(Right_Action_Matrix(V[j], mult))
    return higman_trace
def compute_M(A):
    dim = A.dim
    if A.casimir_flag == 'no':
        A.GetCasimir()
    mult = A.mult
    casimir = A.casimir
    tensor_mult = Tensor_Mult(A, A)
    C = mult.dot(tensor_mult.dot(np.kron(casimir, casimir)))
    return Left_Action_Matrix(C, A.mult)
if __name__ == "__main__":
    pass