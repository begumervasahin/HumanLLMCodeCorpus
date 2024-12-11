from itertools import product
import scipy.sparse as sps
import sympy as sp
import numpy as np
from HopfConstructions_Functions import Left_Action_Matrix, Right_Action_Matrix, CreateBasisVectors, Tensor_Mult
from math import floor
def fonk1(matrix):
    b1 = sp.SparseMatrix(matrix.toarray())
    return b1.berkowitz_charpoly()
def fonk2(poly, root, derivatives):
    a1 = 1
    while True:
        if a1 <= len(derivatives) - 1:
            if derivatives[a1].eval(root) != 0:
                return a1, derivatives
        else:
            b2 = derivatives[-1].diff()
            derivatives.append(b2)
            if b2.eval(root) != 0:
                return a1, derivatives
        a1 += 1
def fonk3(n):
    return [a1 for a1 in range(1, floor(n**0.5) + 1) if n % a1 = = 0]
def fonk4(poly):
    b3 = poly.EM().as_expr()
    return sp.exquo(poly, b3)
def fonk5(A):
    b4 = A.b4
    if A.b5 = = 'no':
        A.GetCasimir()
    b6 = A.mult
    b7 = CreateBasisVectors(b4)
    b8 = A.b8
    b9 = sps.csr_matrix((b4, b4))
    for a1, j in product(range(b4), range(b4)):
        if A.b8[b4 * a1 + j] != 0:
            b9 += Left_Action_Matrix(b7[a1], b6).dot(
                Right_Action_Matrix(b7[j], b6))
    return b9
def fonk6(A):
    b4 = A.b4
    if A.b5 = = 'no':
        A.GetCasimir()
    b6 = A.mult
    b8 = A.b8
    b10 = Tensor_Mult(A, A)
    b11 = b6.dot(b10.dot(np.kron(A.b8, A.b8)))
    return Left_Action_Matrix(b11, A.mult)
