from itertools import product
import scipy.sparse as sps
import sympy as sp
import numpy as np
from HopfConstructions_Functions import Left_Action_Matrix, Right_Action_Matrix, CreateBasisVectors, Tensor_Mult
from math import floor
def char_poly(M):
    temp = M.toarray()
    temp = sp.SparseMatrix(temp)
    return temp.berkowitz_charpoly()
def multiplicity(poly, root, Der):
    D = Der
    i = 1
    flag = 'go'
    while flag == 'go':
        if i <= (len(D) - 1):
            if D[i].eval(root) != 0:
                multiplicity = i
                flag = 'stop'
        else:
            temp = D[-1].diff()
            D.append(temp)
            if temp.eval(root) != 0:
                multiplicity = i
                flag = 'stop'
        i += 1
    return [multiplicity, D]
def divisors(n):
    out = []
    for i in range(1, floor(n**.5) + 1):
        if n % i == 0:
            out.append(i)
    return out
def remove_zeros_at_zero(poly):
    mon = poly.EM()
    mon = mon.as_expr()
    return sp.exquo(poly, mon)
def higman_trace(A):
    dim = A.dim
    if A.casimir_flag == 'no':
        A.GetCasimir()
    mult = A.mult
    V = CreateBasisVectors(dim)
    casimir = A.casimir
    higman_trace = sps.csr_matrix((dim, dim))
    for i, j in product(range(0, dim), range(0, dim)):
        if A.casimir[dim * i + j] != 0:
            higman_trace = higman_trace + Left_Action_Matrix(V[i], mult).dot(Right_Action_Matrix(V[j], mult))
    return higman_trace
def compute_M(A):
    dim = A.dim
    if A.casimir_flag == 'no':
        A.GetCasimir()
    mult = A.mult
    casimir = A.casimir
    tensor_mult = Tensor_Mult(A, A)
    C = mult.dot(tensor_mult.dot(np.kron(A.casimir, A.casimir)))
    return Left_Action_Matrix(C, A.mult)
