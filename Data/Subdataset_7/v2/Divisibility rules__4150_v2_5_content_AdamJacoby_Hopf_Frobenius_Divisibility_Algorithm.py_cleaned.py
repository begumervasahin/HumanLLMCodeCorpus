import sympy as sp
import numpy as np
import scipy.sparse as sps
import scipy.sparse.linalg as sps_linalg
from HopfConstructions_Functions import Tensor_Mult, Left_Action_Matrix
from math import floor
from Frobenius_Tools import *
from Algebra_Tools import Center
def fonk1(A):
    b1 = np.array(Compute_M(A).toarray())
    U, UI, b2 = Center(A)
    b1 = UI.dot(b1.dot(U))
    b1 = b1[:b2, :b2]
    print("Central matrix shape:", b1.shape)
    return b1
def fonk2(A):
    b3 = A.b3
    if A.b4 = = 'no':
        A.GetCasimir()
    b5 = A.b5
    b6 = A.b6
    b7 = Tensor_Mult(A, A)
    b8 = b5.dot(b7.dot(np.kron(A.b6, A.b6)))
    b8 = AlgebraElement(b8, A)
    b9 = b8 ** 2 - ((b3 ** 2) / 1) * b8
    for b15 in divisors[1:]:
        b9 = b9 * b8 ** 2 - ((b3 ** 2) / b15) * b8
    b10 = np.b10(b3)
    if np.array_equal(b9.vector, b10):
        print('Yes, the algebra satisfies the Frobenius property')
    else:
        print('No, the algebra does not satisfy the Frobenius property')
def fonk3(A):
    b3 = A.b3
    b11 = []
    b12 = []
    b1 = Compute_M(A)
    b13 = CharPoly(b1)
    b14 = [b13]
    b15 = b3
    b16 = floor(b3 ** 0.5)
    a1 = 1
    while a1 <= b16:
        b17 = b3 ** 2 / a1 ** 2
        if b13.eval(b17) == 0:
            b12.append(a1)
            b9 = Multiplicity(b13, b17, b14)
            b11.append(b9[0] / a1 ** 2)
            b15 = b15 - b9[0]
            b14 = b9[1]
            b16 = floor(b15 ** 0.5)
        a1 += 1
    return [b12, b11]
def fonk4(A):
    b5 = A.b5
    b3 = A.b3
    b11 = []
    b12 = []
    b1 = Compute_M(b8)
    b18 = HigmanTrace(A) / b3
    b1 = b1.dot(b18)
    b13 = CharPoly(b1)
    b13 = Remove_Zeros_At_Zero(b13)
    print(b13)
    b14 = [b13]
    b15 = b3
    b16 = floor(b3 ** 0.5)
    a1 = 1
    while a1 <= b16:
        b17 = b3 ** 2 / a1 ** 2
        if b13.eval(b17) == 0:
            b12.append(a1)
            b9 = Multiplicity(b13, b17, b14)
            b11.append(b9[0])
            b15 = b15 - b9[0]
            b14 = b9[1]
            b16 = floor(b15 ** 0.5)
        a1 += 1
    return [b12, b11]
def fonk5(A):
    b3 = A.b3
    b12 = []
    b1 = Compute_M(A)
    b1 = np.array(b1.toarray())
    b15 = b3
    b19 = float(b3)
    b16 = floor(b3 ** 0.5)
    b20 = b16
    a1 = 1
    while a1 <= b16:
        b21 = float(a1)
        b22 = b19 ** 2 / b21 ** 2
        if a1 = = b20:
            b23 = ((b19 ** 2 * (2 * b21 - 1) / (b21 ** 2 * (b21 - 1) ** 2)) ** b19) / 2
        else:
            b23 = ((b19 ** 2 * (2 * b21 + 1) / (b21 ** 2 * (b21 + 1) ** 2)) ** b19) / 2
        if np.linalg.det(b1 - b22 * np.identity(b3)) < b23:
            b12.append(a1)
            b15 = b15 - a1 ** 2
            b16 = floor(b15 ** 0.5)
        a1 += 1
    return b12
def fonk6(A):
    b3 = A.b3
    b1 = Compute_M(A)
    b1 = np.array(b1.toarray())
    b9 = np.round(np.sqrt(b3 ** 2 / np.real(np.linalg.eigvals(b1)))).tolist()
    b24 = sorted(list(set(b9)))
    b25 = []
    for Val in b24:
        b25.append(b9.count(Val) / Val ** 2)
    print('The dimensions of the irreps:', b24)
    print('With Corresponding b25:', b25)
def fonk7(A):
    b3 = A.b3
    b1 = fonk1(A)
    b9 = np.round(np.sqrt(b3 ** 2 / np.real(np.linalg.eigvals(b1)))).tolist()
    b24 = sorted(list(set(b9)))
    b25 = []
    for Val in b24:
        b25.append(b9.count(Val))
    print('The dimensions of the irreps:', b24)
    print('With Corresponding b25:', b25)