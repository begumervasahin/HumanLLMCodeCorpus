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
def fonk2(poly, root, derivative):
    b3 = derivative
    a1 = 1
    b4 = 'go'
    while b4 = = 'go':
        if a1 <= (len(b3) - 1):
            if b3[a1].eval(root) != 0:
                b5 = a1
                b4 = 'stop'
        else:
            b1 = b3[-1].diff()
            b3.append(b1)
            if b1.eval(root) != 0:
                b5 = a1
                b4 = 'stop'
        a1 += 1
    return [b5, b3]
def fonk3(n):
    b6 = []
    for a1 in range(1, floor(n**0.5) + 1):
        if n % a1 = = 0:
            b6.append(a1)
    return b6
def fonk4(poly):
    b7 = poly.EM()
    b7 = b7.as_expr()
    return sp.exquo(poly, b7)
def fonk5(A):
    b8 = A.b8
    if A.b9 = = 'no':
        A.GetCasimir()
    b10 = A.mult
    b11 = CreateBasisVectors(b8)
    b12 = A.b12
    b13 = sps.csr_matrix((b8, b8))
    for a1, j in product(range(b8), range(b8)):
        if A.b12[b8 * a1 + j] != 0:
            b13 = b13 + Left_Action_Matrix(b11[a1], b10).dot(
                Right_Action_Matrix(b11[j], b10))
    return b13
def fonk6(A):
    b8 = A.b8
    if A.b9 = = 'no':
        A.GetCasimir()
    b10 = A.mult
    b12 = A.b12
    b14 = Tensor_Mult(A, A)
    b15 = b10.dot(b14.dot(np.kron(A.b12, A.b12)))
    return Left_Action_Matrix(b15, A.mult)
