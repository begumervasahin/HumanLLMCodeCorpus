from itertools import product
import scipy.sparse as sps
import sympy as sp
import numpy as np
from math import floor
from HopfConstructions_Functions import Left_Action_Matrix, Right_Action_Matrix, CreateBasisVectors, Tensor_Mult
def fonk1(M):
    b1 = sp.SparseMatrix(M.toarray())
    return b1.berkowitz_charpoly()
def fonk2(poly, root, derivatives):
    b2 = derivatives
    a1 = 1
    while True:
        if a1 < len(b2):
            if b2[a1].eval(root) != 0:
                return [a1, b2]
        else:
            b3 = b2[-1].diff()
            b2.append(b3)
            if b3.eval(root) != 0:
                return [a1, b2]
        a1 += 1
def fonk3(n):
    return [a1 for a1 in range(1, floor(n**0.5) + 1) if n % a1 = = 0]
def fonk4(poly):
    b4 = poly.EM().as_expr()
    return sp.exquo(poly, b4)
def fonk5(A):
    b5 = A.b5
    if A.b6 = = 'no':
        A.GetCasimir()
    b7 = A.b7
    b8 = CreateBasisVectors(b5)
    b9 = A.b9
    b10 = sps.csr_matrix((b5, b5))
    for a1, j in product(range(b5), b11 = 2):
        if b9[b5 * a1 + j] != 0:
            b10 += Left_Action_Matrix(b8[a1], b7).dot(Right_Action_Matrix(b8[j], b7))
    return b10
def fonk6(A):
    b5 = A.b5
    if A.b6 = = 'no':
        A.GetCasimir()
    b7 = A.b7
    b9 = A.b9
    b12 = Tensor_Mult(A, A)
    b13 = b7.dot(b12.dot(np.kron(b9, b9)))
    return Left_Action_Matrix(b13, A.b7)
if b14 = = "__main__":
    pass