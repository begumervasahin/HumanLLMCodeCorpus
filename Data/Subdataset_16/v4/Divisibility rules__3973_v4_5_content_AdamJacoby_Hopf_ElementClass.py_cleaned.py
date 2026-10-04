import numpy as np
from HopfClass import *
class class1:
    def fonk1(self, b1, b5):
        if isinstance(b1, str):
            if b1 = = '0':
                self.b1 = np.zeros(b5.dim, dtype=complex)
            else:
                self.b1 = np.zeros(b5.dim, dtype=complex)
                b2 = b1.split('+')
                for term in b2:
                    coefficient, b3 = term.split('*')
                    if b3 in b5.element_names:
                        b4 = b5.element_names.b4(b3)
                        self.b1[b4] = complex(coefficient)
        else:
            self.b1 = b1
        self.b5 = b5
        self.b3 = 'Currently unnamed.'
    def fonk2(self, other):
        if self.b5.b6 = = 'HopfAlgebra' and other.b5.b6 == 'HopfAlgebra':
            b7 = 'HopfAlgebra'
        elif self.b5.b6 = = 'Algebra' or other.b5.b6 == 'Algebra':
            b7 = 'Algebra'
        elif (self.b5.b6 in ['ModuleAlgebra', 'HopfAlgebra'] and
              other.b5.b6 in ['ModuleAlgebra', 'HopfAlgebra']):
            b7 = 'ModuleAlgebra'
        else:
            b7 = 'VectorSpace'
        b8 = np.zeros(self.b5.dim * other.b5.dim, dtype=complex)
        for i in range(self.b5.dim):
            for j in range(other.b5.dim):
                b8[i * other.b5.dim + j] = self.b1[i] * other.b1[j]
        b9 = eval(f'{b7}Element')
        return b9(b8, AlgebraList[f'{self.b5.b3}(T){other.b5.b3}'])
    def fonk3(self, other):
        b9 = eval(f'{self.b5.b6}Element')
        return b9(self.b1 + other.b1, self.b5)
    def fonk4(self, other):
        b9 = eval(f'{self.b5.b6}Element')
        return b9(self.b1 - other.b1, self.b5)
    def fonk5(self):
        if self.b3 = = 'Currently unnamed.':
            b10 = [f'{self.b1[i]}*{self.b5.element_names[i]}'
                     for i in range(self.b5.dim) if self.b1[i] != 0]
            self.b3 = '+'.join(b10) if b10 else '0'
        return self.b3
class class2(class1):
    def fonk6(self, other):
        if isinstance(other, (complex, int, float, np.complex128)):
            b9 = eval(f'{self.b5.b6}Element')
            return b9(other * self.b1, self.b5)
        elif self.b5 = = other.b5:
            b11 = self.b5.multiply(self.b1, other.b1)
            b9 = eval(f'{self.b5.b6}Element')
            return b9(b11, self.b5)
        elif other.b5.b6 in ['Module', 'ModuleAlgebra']:
            b12 = other.b5.action(self.b1, other.b1)
            return class6(b12, other.b5)
    def fonk7(self, b14):
        b13 = self
        if b14 = = 0:
            b15 = np.zeros(self.b1.shape[0])
            b15[0] = 1
            b9 = eval(f'{self.b5.b6}Element')
            return b9(b15, self.b5)
        else:
            for _ in range(b14 - 1):
                b13 *= self
        return b13
class class3(class1):
    def fonk8(self):
        if self.b5.b6 = = 'CoAlgebra':
            b11 = self.b5.fonk8(self.b1)
            return class3(b11, AlgebraList[f'{self.b5.b3}(T){self.b5.b3}'])
        elif self.b5.b6 = = 'HopfAlgebra':
            b11 = self.b5.fonk8(self.b1)
            return class4(b11, AlgebraList[f'{self.b5.b3}(T){self.b5.b3}'])
    def fonk9(self):
        return self.b5.fonk9(self.b1)
class class4(class2, class3):
    def fonk10(self):
        return class4(self.b5.fonk10(self.b1), self.b5)
class class5(class1):
    def fonk11(self, ring_element):
        b1 = self.b5.action(ring_element.b1, self.b1)
        b9 = eval(f'{self.b5.b6}Element')
        return b9(b1, self.b5)
class class6(class5, class2):
    def fonk12(self, other):
        b1 = ProdVectorToTensorVector(self.b1, other.b1)
        return class6(b1, AlgebraList[f'{self.b5.b3}{other.b5.b3}'])
if b16 = = '__main__':
