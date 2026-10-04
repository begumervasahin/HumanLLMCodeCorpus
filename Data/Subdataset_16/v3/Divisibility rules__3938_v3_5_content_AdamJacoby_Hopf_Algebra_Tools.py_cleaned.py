import numpy as np
import scipy.sparse as sps
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
def fonk7(b23):
    return [np.eye(b23, b11 = complex)[:, i] for i in range(b23)]
def fonk8(b33):
    b12 = b33.b3.shape[0]
    return csr_matrix(np.random.rand(b12, b12))
def fonk9(b33, b13, b14):
    b13 = csr_matrix(b13.tolist())
    b14 = csr_matrix(b14.tolist())
    if 'class1' in b33.b4:
        b15 = b13.dot(b33.b3.dot(kron(b14, b14)))
    if 'class5' in b33.b4:
        b16 = b33.b6.b23
        b17 = b13.dot(b33.b10)
        b18 = identity(b16, format='csr')
        b17 = b13.dot(b17.dot(kron(b18, b14)))
    if b33.b4 in ['class4', 'class3', 'class2']:
        b19 = kron(b13, b13).dot(b33.b7.dot(b14))
        b20 = b33.b8.dot(b14)
    if b33.b4 = = 'class1':
        return class1(b33.b1, b33.b2, b15)
    if b33.b4 = = 'class2':
        return class2(b33.b1, b33.b2, b19, b20)
    if b33.b4 = = 'class3':
        return class3(b33.b1, b33.b2, b15, b19, b20)
    if b33.b4 = = 'class4':
        b21 = b13.dot(b33.b9.dot(b14))
        return class4(b33.b1, b33.b2, b15, b19, b20, b21)
    if b33.b4 = = 'class5':
        b22 = class5(b33.b1, b33.b2, b33.b6, b17)
        if isinstance(b33, class6):
            return class6(b33.b1, b33.b2, b33.b6, b17, b15)
    if 'class1' in b33.b4 and b33.b5 != 'no':
        b33.Input_Casimir(kron(b13, b13).dot(b33.casimir))
    return b33
def fonk10(b33):
    b23 = b33.b23
    b24 = fonk7(b23)
    b24 = [vector.tolist() for vector in b24]
    b25 = fonk8(b33)
    b25 = Matrix(b25.toarray())
    b27, b26 = b25.transpose().rref()
    b27 = b27.tolist()
    b27 = [row for row in b27 if row != [0] * b23]
    b28 = len(b27)
    b29 = []
    a1 = 0
    b30 = []
    for vector in b27:
        b31 = vector.index(1)
        for i in range(a1 + 1, b31):
            b30.append(i)
        b29.append(vector)
        a1 = b31
    for i in range(b31 + 1, b23):
        b30.append(i)
    for index in b30:
        b29.append(b24[index])
    b13 = np.transpose(np.array(b29, b11=complex))
    b14 = np.linalg.inv(b13)
    return [b13, b14, b28]
if b32 = = '__main__':
    b33 = class1(b1="ExampleAlgebra", b2=["e1", "e2"], b3=np.array([[1, 0], [0, 1]]))
    b13 = np.random.rand(2, 2)
    b14 = np.linalg.inv(b13)
    b34 = fonk9(b33, b13, b14)
    b35 = fonk10(b33)
    print("Changed Basis:", b34)
    print("Center Result:", b35)