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
    U, UI, b2 = Center(A)
    b1 = UI.dot(b1.dot(U))
    b1 = np.array(b1.tolist())
    b1 = b1[0:b2, 0:b2]
    print(b1.shape)
    return b1
def fonk2(A):
    b3 = A.b3
    if A.b4 = = 'no':
        A.GetCasimir()
    b5 = A.b5
    b6 = A.b6
    b7 = Tensor_Mult(A, A)
    b8 = b5.dot(b7.dot(np.kron(b6, b6)))
    b8 = AlgebraElement(b8, A)
    b9 = b8**2 - (b3**2) * b8
    b10 = sp.b10(b3**2)
    for b16 in b10[1:]:
        b9 = b9 * b8**2 - (b3**2 / b16) * b8
    b11 = np.b11(b3)
    if np.array_equal(b9.vector, b11):
        print('Yes FD')
    else:
        print('No FD')
def fonk3(A):
    b3 = A.b3
    b12 = []
    b13 = []
    b1 = Compute_M(A)
    b14 = CharPoly(b1)
    b15 = [b14]
    b16 = b3
    b17 = floor(b3**0.5)
    a1 = 1
    while a1 <= b17:
        b18 = b3**2 / a1**2
        if b14.eval(b18) == 0:
            b13.append(a1)
            b9 = Multiplicity(b14, b18, b15)
            b12.append(b9[0] / a1**2)
            b16 -= b9[0]
            b15 = b9[1]
            b17 = floor(b16**0.5)
        a1 += 1
    return [b13, b12]
def fonk4(A):
    b3 = A.b3
    b12 = []
    b13 = []
    b1 = Compute_M(A)
    b19 = HigmanTrace(A) / b3
    b1 = b1.dot(b19)
    b14 = CharPoly(b1)
    b14 = Remove_Zeros_At_Zero(b14)
    print(b14)
    b15 = [b14]
    b16 = b3
    b17 = floor(b3**0.5)
    a1 = 1
    while a1 <= b17:
        b18 = b3**2 / a1**2
        if b14.eval(b18) == 0:
            b13.append(a1)
            b9 = Multiplicity(b14, b18, b15)
            b12.append(b9[0])
            b16 -= b9[0]
            b15 = b9[1]
            b17 = floor(b16**0.5)
        a1 += 1
    return [b13, b12]
def fonk5(A):
    b3 = A.b3
    b13 = []
    b1 = Compute_M(A)
    b1 = np.array(b1.toarray())
    b16 = b3
    b20 = float(b3)
    b17 = floor(b3**0.5)
    b21 = b17
    a1 = 1
    while a1 <= b17:
        b22 = float(a1)
        b23 = b20**2 / b22**2
        if a1 = = b21:
            b24 = ((b20**2 * (2 * b22 - 1) / (b22**2 * (b22 - 1)**2))**b20) / 2
        else:
            b24 = ((b20**2 * (2 * b22 + 1) / (b22**2 * (b22 + 1)**2))**b20) / 2
        if np.linalg.det(b1 - b23 * np.identity(b3)) < b24:
            b13.append(a1)
            b16 -= a1**2
            b17 = floor(b16**0.5)
        a1 += 1
    return b13
def fonk6(A):
    b3 = A.b3
    b1 = Compute_M(A)
    b1 = np.array(b1.toarray())
    b9 = np.round(np.sqrt(b3**2 / np.real(np.linalg.eigvals(b1)))).tolist()
    b25 = sorted(list(set(b9)))
    b26 = [b9.count(val) / val**2 for val in b25]
    print(f'The dimensions of the irreps: {b25}')
    print(f'With corresponding b26: {b26}')
def fonk7(A):
    b3 = A.b3
    b1 = fonk1(A)
    b9 = np.round(np.sqrt(b3**2 / np.real(np.linalg.eigvals(b1)))).tolist()
    b25 = sorted(list(set(b9)))
    b26 = [b9.count(val) for val in b25]
    print(f'The dimensions of the irreps: {b25}')
    print(f'With corresponding b26: {b26}')
if b27 = = "__main__":
    pass