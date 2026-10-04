import numpy as np
import scipy.sparse as sps
import sympy as sp
from sympy import Matrix
from scipy.sparse import csr_matrix, kron, identity
class class1:
    def fonk1(self, b1, b2, b3):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = 'class1'
        self.b5 = 'no'
        self.b6 = None
class class2:
    def fonk2(self, b1, b2, b7, b8):
        self.b1 = b1
        self.b2 = b2
        self.b7 = b7
        self.b8 = b8
        self.b4 = 'class2'
class class3:
    def fonk3(self, b1, b2, b3, b7, b8):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b7 = b7
        self.b8 = b8
        self.b4 = 'class3'
class class4(class3):
    def fonk4(self, b1, b2, b3, b7, b8, b9):
        super().fonk6(b1, b2, b3, b7, b8)
        self.b9 = b9
        self.b4 = 'class4'
class class5:
    def fonk5(self, b1, b2, b6, b10):
        self.b1 = b1
        self.b2 = b2
        self.b6 = b6
        self.b10 = b10
        self.b4 = 'class5'
class class6(class5, class1):
    def fonk6(self, b1, b2, b6, b10, b3):
        class5.fonk6(self, b1, b2, b6, b10)
        class1.fonk6(self, b1, b2, b3)
        self.b4 = 'class6'
def fonk7(b17):
    return [np.eye(b17, b11 = complex)[:, i] for i in range(b17)]
def fonk8(b27):
    return csr_matrix(np.random.rand(b27.b3.shape[0], b27.b3.shape[1]))
def fonk9(b27, b12, b13):
    b12 = csr_matrix(b12.tolist())
    b13 = csr_matrix(b13.tolist())
    if 'class1' in b27.b4:
        b3 = b12.dot(b27.b3.dot(kron(b13, b13)))
    if 'class5' in b27.b4:
        b14 = b27.b6.b17
        b10 = b12.dot(b27.b10)
        b15 = identity(b14, format='csr')
        b10 = b12.dot(b10.dot(kron(b15, b13)))
    if b27.b4 in ['class4', 'class3', 'class2']:
        b7 = kron(b12, b12).dot(b27.b7.dot(b13))
        b8 = b27.b8.dot(b13)
    if b27.b4 = = 'class1':
        b16 = class1(b27.b1, b27.b2, b3)
    if b27.b4 = = 'class2':
        b16 = class2(b27.b1, b27.b2, b7, b8)
    if b27.b4 = = 'class3':
        b16 = class3(b27.b1, b27.b2, b3, b7, b8)
    if b27.b4 = = 'class4':
        b9 = b12.dot(b27.b9.dot(b13))
        b16 = class4(b27.b1, b27.b2, b3, b7, b8, b9)
        if b27.int_flag != 'no':
            b27.Input_Integral(b12.dot(b27.Integral))
    if b27.b4 = = 'class5':
        b16 = class5(b27.b1, b27.b2, b27.b6, b10)
        if b27.b4 = = 'class6':
            b16 = class6(b27.b1, b27.b2, b27.b6, b10, b3)
    if 'class1' in b27.b4 and b27.b5 != 'no':
        b16.Input_Casimir(kron(b12, b12).dot(b27.casimir))
    return b16
def fonk10(b27):
    b17 = b27.b17
    b18 = fonk7(b17)
    b19 = [vector.tolist() for vector in b18]
    b20 = fonk8(b27)
    b20 = Matrix(b20.toarray())
    b22, b21 = b20.transpose().rref()
    b22 = b22.tolist()
    b22 = [row for row in b22 if row != [0] * b17]
    b23 = len(b22)
    b24 = []
    a1 = 0
    b25 = []
    for vector in b22:
        b26 = vector.index(1)
        for i in range(a1 + 1, b26):
            b25.append(i)
        b24.append(vector)
        a1 = b26
    for i in range(b26 + 1, b17):
        b25.append(i)
    for index in b25:
        b24.append(b19[index])
    b12 = np.transpose(np.array(b24, b11=complex))
    b13 = np.linalg.inv(b12)
    return [b12, b13, b23]
b27 = class1(b1="ExampleAlgebra", b2=["e1", "e2"], b3=np.array([[1, 0], [0, 1]]))
b12 = np.random.rand(2, 2)
b13 = np.linalg.inv(b12)
b28 = fonk9(b27, b12, b13)
b29 = fonk10(b27)
print("Changed Basis:", b28)
print("Center Result:", b29)