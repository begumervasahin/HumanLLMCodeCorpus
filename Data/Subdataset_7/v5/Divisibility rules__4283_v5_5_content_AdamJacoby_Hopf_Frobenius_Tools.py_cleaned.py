from itertools import product
import scipy.sparse as sps
import sympy as sp
import numpy as np
from HopfConstructions_Functions import Left_Action_Matrix, Right_Action_Matrix, CreateBasisVectors, Tensor_Mult
from math import floor
def fonk1(matrix):
    b1 = matrix.toarray()
    b2 = sp.SparseMatrix(b1)
    return b2.berkowitz_charpoly()
def fonk2(poly, root, derivatives):
    a1 = 1
    while True:
        if a1 <= len(derivatives) - 1:
            if derivatives[a1].eval(root) != 0:
                return a1, derivatives
        else:
            b3 = derivatives[-1].diff()
            derivatives.append(b3)
            if b3.eval(root) != 0:
                return a1, derivatives
        a1 += 1
def fonk3(n):
    b4 = []
    for a1 in range(1, floor(n ** 0.5) + 1):
        if n % a1 = = 0:
            b4.append(a1)
    return b4
def fonk4(poly):
    b5 = poly.EM().as_expr()
    return sp.exquo(poly, b5)
def fonk5(A):
    b6 = A.b6
    if A.b7 = = 'no':
        A.GetCasimir()
    b8 = A.b8
    b9 = CreateBasisVectors(b6)
    b10 = A.b10
    b11 = sps.csr_matrix((b6, b6))
    for a1, j in product(range(b6), range(b6)):
        if A.b10[b6 * a1 + j] != 0:
            b11 += Left_Action_Matrix(b9[a1], b8).dot(
                Right_Action_Matrix(b9[j], b8))
    return b11
def fonk6(A):
    b6 = A.b6
    if A.b7 = = 'no':
        A.GetCasimir()
    b8 = A.b8
    b10 = A.b10
    b12 = Tensor_Mult(A, A)
    b13 = b8.dot(b12.dot(np.kron(A.b10, A.b10)))
    return Left_Action_Matrix(b13, A.b8)