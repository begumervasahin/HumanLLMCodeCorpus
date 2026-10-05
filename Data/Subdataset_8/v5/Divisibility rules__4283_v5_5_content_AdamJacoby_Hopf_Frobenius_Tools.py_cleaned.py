from itertools import product
import scipy.sparse as sps
import sympy as sp
import numpy as np
from HopfConstructions_Functions import Left_Action_Matrix, Right_Action_Matrix, CreateBasisVectors, Tensor_Mult
from math import floor
def calculate_characteristic_polynomial(matrix):
    dense_matrix = matrix.toarray()
    sparse_matrix = sp.SparseMatrix(dense_matrix)
    return sparse_matrix.berkowitz_charpoly()
def find_multiplicity(poly, root, derivatives):
    i = 1
    while True:
        if i <= len(derivatives) - 1:
            if derivatives[i].eval(root) != 0:
                return i, derivatives
        else:
            temp_derivative = derivatives[-1].diff()
            derivatives.append(temp_derivative)
            if temp_derivative.eval(root) != 0:
                return i, derivatives
        i += 1
def get_divisors(n):
    divisors_list = []
    for i in range(1, floor(n ** 0.5) + 1):
        if n % i == 0:
            divisors_list.append(i)
    return divisors_list
def remove_zeros_at_root(poly):
    leading_monomial = poly.EM().as_expr()
    return sp.exquo(poly, leading_monomial)
def calculate_higman_trace(A):
    dim = A.dim
    if A.casimir_flag == 'no':
        A.GetCasimir()
    mult = A.mult
    basis_vectors = CreateBasisVectors(dim)
    casimir = A.casimir
    higman_trace = sps.csr_matrix((dim, dim))
    for i, j in product(range(dim), range(dim)):
        if A.casimir[dim * i + j] != 0:
            higman_trace += Left_Action_Matrix(basis_vectors[i], mult).dot(
                Right_Action_Matrix(basis_vectors[j], mult))
    return higman_trace
def compute_matrix_product(A):
    dim = A.dim
    if A.casimir_flag == 'no':
        A.GetCasimir()
    mult = A.mult
    casimir = A.casimir
    tensor_mult = Tensor_Mult(A, A)
    product_matrix = mult.dot(tensor_mult.dot(np.kron(A.casimir, A.casimir)))
    return Left_Action_Matrix(product_matrix, A.mult)