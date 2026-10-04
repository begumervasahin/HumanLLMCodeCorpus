import sympy as sp
import numpy as np
import scipy.sparse as sps
import scipy.sparse.linalg as sps_linalg
from itertools import product
from math import floor
from HopfConstructions_Functions import Tensor_Mult, Left_Action_Matrix
from Frobenius_Tools import Compute_M, CharPoly, Multiplicity, HigmanTrace, Remove_Zeros_At_Zero
from Algebra_Tools import Center, AlgebraElement
def fonk1(A):
    b1 = np.array(Compute_M(A).toarray())
    b2 = Center(A)
    b3 = b2[0]
    b4 = b2[2]
    b5 = b2[1]
    b1 = b5.dot(b1.dot(b3))
    b1 = np.array(b1.tolist())
    b1 = b1[0:b4, 0:b4]
    print(b1.shape)
    return b1
def fonk2(A):
    b6 = A.b6
    if A.b7 = = 'no':
        A.GetCasimir()
    b8 = A.b8
    b9 = A.b9
    b10 = Tensor_Mult(A, A)
    b11 = b8.dot(b10.dot(np.kron(A.b9, A.b9)))
    b11 = AlgebraElement(b11, A)
    b2 = b11**2 - ((b6**2)/1)*b11
    b12 = sp.b12(b6**2)
    for b18 in b12[1:]:
        b2 = b2*b11**2 - ((b6**2)/b18)*b11
    b13 = np.b13(b6)
    if np.array_equal(b2.vector, b13):
        print('Yes FD')
    else:
        print('No FD')
def fonk3(A):
    b6 = A.b6
    b14 = []
    b15 = []
    b1 = Compute_M(A)
    b16 = CharPoly(b1)
    b17 = [b16]
    b18 = b6
    b19 = floor(b6**0.5)
    a1 = 1
    while a1 <= b19:
        b20 = b6**2 / a1**2
        if b16.eval(b20) == 0:
            b15.append(a1)
            b2 = Multiplicity(b16, b20, b17)
            b14.append(b2[0] / a1**2)
            b18 = b18 - b2[0]
            b17 = b2[1]
            b19 = floor(b18**0.5)
        a1 += 1
    return [b15, b14]
def fonk4(A):
    b8 = A.b8
    b6 = A.b6
    b14 = []
    b15 = []
    b1 = Compute_M(A)
    b21 = HigmanTrace(A) / b6
    b1 = b1.dot(b21)
    b16 = CharPoly(b1)
    b16 = Remove_Zeros_At_Zero(b16)
    print(b16)
    b17 = [b16]
    b18 = b6
    b19 = floor(b6**0.5)
    a1 = 1
    while a1 <= b19:
        b20 = b6**2 / a1**2
        if b16.eval(b20) == 0:
            b15.append(a1)
            b2 = Multiplicity(b16, b20, b17)
            b14.append(b2[0])
            b18 = b18 - b2[0]
            b17 = b2[1]
            b19 = floor(b18**0.5)
        a1 += 1
    return [b15, b14]
def fonk5(A):
    b6 = A.b6
    b15 = []
    b1 = Compute_M(A)
    b1 = np.array(b1.toarray())
    b18 = b6
    b22 = float(b6)
    b19 = floor(b6**0.5)
    b23 = b19
    a1 = 1
    while a1 <= b19:
        b24 = float(a1)
        b25 = b22**2 / b24**2
        if a1 = = b23:
            b26 = ((b22**2 * (2 * b24 - 1) / (b24**2 * (b24 - 1)**2))**b22) / 2
        else:
            b26 = ((b22**2 * (2 * b24 + 1) / (b24**2 * (b24 + 1)**2))**b22) / 2
        if np.linalg.det(b1 - b25 * np.identity(b6)) < b26:
            b15.append(a1)
            b18 = b18 - a1**2
            b19 = floor(b18**0.5)
        a1 += 1
    return b15
def fonk6(A):
    b6 = A.b6
    b1 = Compute_M(A)
    b1 = np.array(b1.toarray())
    b2 = np.round(np.sqrt(b6**2 / np.real(np.linalg.eigvals(b1)))).tolist()
    b27 = sorted(list(set(b2)))
    b28 = [b2.count(val) / val**2 for val in b27]
    print(f'The dimensions of the irreps: {b27}')
    print(f'With corresponding b28: {b28}')
def fonk7(A):
    b6 = A.b6
    b1 = fonk1(A)
    b2 = np.round(np.sqrt(b6**2 / np.real(np.linalg.eigvals(b1)))).tolist()
    b27 = sorted(list(set(b2)))
    b28 = [b2.count(val) for val in b27]
    print(f'The dimensions of the irreps: {b27}')
    print(f'With corresponding b28: {b28}')
if b29 = = "__main__":
    pass