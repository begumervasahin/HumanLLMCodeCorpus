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
    b2 = Center(A)
    b3 = b2[0]
    b4 = b2[2]
    b5 = b2[1]
    b1 = b5.dot(b1.dot(b3))
    b1 = np.array(b1.tolist())
    b1 = b1[0:b4,0:b4]
    print(b1.shape)
    return b1
def fonk2(A):
    b6 = A.b6
    if A.b7 = = 'no':
        A.GetCasimir()
    b8 = A.b8
    b9 = A.b9
    b10 = Tensor_Mult(A,A)
    b11 = b8.dot(b10.dot(np.kron(A.b9,A.b9)))
    b11 = AlgebraElement(b11,A)
    b2 = b11**2-((b6**2)/1)*b11
    for b17  in divisors[1:]:
        b2 = b2*b11**2-((b6**2)/b17)*b11
    b12 = np.b12(b6)
    if np.array_equal(b2.vector, b12):
        print('Yes FD')
    else:
        print('No FD')
def fonk3(A):
    b6 = A.b6
    b13 = []
    b14 = []
    b1 = Compute_M(A)
    b15 = CharPoly(b1)
    b16 = [b15]
    b17 = b6
    b18 = floor(b6**.5)
    a1 = 1
    while a1 <= b18:
        b19 = b6**2/a1**2
        if b15.eval(b19) == 0:
            b14.append(a1)
            b2 = Multiplicity(b15, b19, b16)
            b13.append(b2[0]/a1**2)
            b17 = b17 - b2[0]
            b16 = b2[1]
            b18 = floor(b17**.5)
        a1 = a1 + 1
    return [b14, b13]
def fonk4(A):
    b8 = A.b8
    b6 = A.b6
    b13 = []
    b14 = []
    b1 = Compute_M(b11)
    b20 = HigmanTrace(A)/b6
    b1 = b1.dot(b20)
    b15 = CharPoly(b1)
    b15 = Remove_Zeros_At_Zero(b15)
    print(b15)
    b16 = [b15]
    b17 = b6
    b18 = floor(b6**.5)
    a1 = 1
    while a1 <= b18:
        b19 = b6**2/a1**2
        if b15.eval(b19) == 0:
            b14.append(a1)
            b2 = Multiplicity(b15, b19, b16)
            b13.append(b2[0])
            b17 = b17 - b2[0]
            b16 = b2[1]
            b18 = floor(b17**.5)
        a1 = a1 + 1
    return [b14, b13]
def fonk5(A):
    b6 = A.b6
    b14 = []
    b1 = Compute_M(A)
    b1 = np.array(b1.toarray())
    b17 = b6
    b21 = float(b6)
    b18 = floor(b6**.5)
    b22 = b18
    a1 = 1
    while a1 <= b18:
        b23 = float(a1)
        b24 = b21**2/b23**2
        if a1 = = b22:
            b25 = ((b21**2*(2*b23-1)/(b23**2*(b23-1)**2))**b21)/2
        else:
            b25 = ((b21**2*(2*b23+1)/(b23**2*(b23+1)**2))**b21)/2
        if np.linalg.det(b1-b24*np.identity(b6)) < b25:
            b14.append(a1)
            b17 = b17 - a1**2
            b18 = floor(b17**.5)
        a1 = a1 + 1
    return b14
def fonk6(A):
    b6 = A.b6
    b1 = Compute_M(A)
    b1 = np.array(b1.toarray())
    b2 = np.round(np.sqrt(b6**2/np.real(np.linalg.eigvals(b1)))).tolist()
    b26 = sorted(list(set(b2)))
    b27 = []
    for Val in b26:
        b27.append(b2.count(Val)/Val**2)
    print('The dimensions of the irreps:', b26)
    print('With Corresponding b27:', b27)
def fonk7(A):
    b6 = A.b6
    b1 = fonk1(A)
    b2 = np.round(np.sqrt(b6**2/np.real(np.linalg.eigvals(b1)))).tolist()
    b26 = sorted(list(set(b2)))
    b27 = []
    for Val in b26:
        b27.append(b2.count(Val))
    print('The dimensions of the irreps:', b26)
    print('With Corresponding b27:', b27)