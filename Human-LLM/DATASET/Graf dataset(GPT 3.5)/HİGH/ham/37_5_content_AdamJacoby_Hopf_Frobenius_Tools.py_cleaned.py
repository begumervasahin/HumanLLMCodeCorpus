from itertools import product
import scipy.sparse as sps
import sympy as sp
import numpy as np
from HopfConstructions_Functions import Left_Action_Matrix, Right_Action_Matrix, CreateBasisVectors, Tensor_Mult
from math import floor
def fonk1(M):
    b1 = M.toarray()
    b1 = sp.SparseMatrix(b1)
    return b1.berkowitz_charpoly()
def fonk2(poly,root,Der):
    b2 = Der
    a1 = 1
    b3 = 'go'
    while b3 = = 'go':
        if a1<=(len(b2)-1):
            if b2[a1].eval(root)!=0:
                b4 = a1
                b3 = 'stop'
        else:
            b1 = b2[-1].diff()
            b2.append(b1)
            if b1.eval(root) != 0:
                b4 = a1
                b3 = 'stop'
        a1 = a1+1
    return [b4,b2]
def fonk3(n):
    b5 = []
    for a1 in range(1,floor(n**.5)+1):
        if n%a1 = =0:
            b5.append(a1)
    return b5
def fonk4(poly):
    b6 = poly.EM()
    b6 = b6.as_expr()
    return sp.exquo(poly,b6)
def fonk5(A):
    b7 = A.b7
    if A.b8 = = 'no':
        A.GetCasimir()
    b9 = A.b9
    b10 = CreateBasisVectors(b7)
    b11 = A.b11
    b12 = sps.csr_matrix((b7,b7))
    for a1,j in product(range(0,b7),range(0,b7)):
        if A.b11[b7*a1+j] !=0:
            b12 = b12+Left_Action_Matrix(b10[a1],b9).dot(Right_Action_Matrix(b10[j],b9))
    return b12
def fonk6(A):
    b7 = A.b7
    if A.b8 = = 'no':
        A.GetCasimir()
    b9 = A.b9
    b11 = A.b11
    b13 = Tensor_Mult(A,A)
    b14 = b9.dot(b13.dot(np.kron(A.b11,A.b11)))
    return Left_Action_Matrix(b14,A.b9)