from itertools import product
import scipy.sparse as sps
import sympy as sp
import numpy as np
from HopfConstructions_Functions import Left_Action_Matrix, Right_Action_Matrix, CreateBasisVectors, Tensor_Mult
from math import floor
def char_poly(matrix):
    temp = matrix.toarray()
    sparse_matrix = sp.SparseMatrix(temp)
    return sparse_matrix.berkowitz_charpoly()
def multiplicity(poly, root, derivative):
    derivatives = derivative
    i = 1
    flag = 'go'
    while flag == 'go':
        if i <= (len(derivatives) - 1):
            if derivatives[i].eval(root) != 0:
                multiplicity = i
                flag = 'stop'
        else:
            temp = derivatives[-1].diff()
            derivatives.append(temp)
            if temp.eval(root) != 0:
                multiplicity = i
                flag = 'stop'
        i += 1
    return [multiplicity, derivatives]
def divisors(n):
    divisors_list = []
    for i in range(1, floor(n**0.5) + 1):
        if n % i == 0:
            divisors_list.append(i)
    return divisors_list
def remove_zeros_at_zero(poly):
    monomial = poly.EM()
    monomial = monomial.as_expr()
    return sp.exquo(poly, monomial)
def higman_trace(A):
    dim = A.dim
    if A.casimir_flag == 'no':
        A.GetCasimir()
    multiplication = A.mult
    basis_vectors = CreateBasisVectors(dim)
    casimir = A.casimir
    higman_trace = sps.csr_matrix((dim, dim))
    for i, j in product(range(dim), range(dim)):
        if A.casimir[dim * i + j] != 0:
            higman_trace = higman_trace + Left_Action_Matrix(basis_vectors[i], multiplication).dot(
                Right_Action_Matrix(basis_vectors[j], multiplication))
    return higman_trace
def compute_M(A):
    dim = A.dim
    if A.casimir_flag == 'no':
        A.GetCasimir()
    multiplication = A.mult
    casimir = A.casimir
    tensor_multiplication = Tensor_Mult(A, A)
    C = multiplication.dot(tensor_multiplication.dot(np.kron(A.casimir, A.casimir)))
    return Left_Action_Matrix(C, A.mult)
