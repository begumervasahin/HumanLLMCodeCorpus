import numpy as np
from HopfClass import *
class class1:
    def fonk1(self, b2, b1):
        self.b1 = b1
        self.b2 = self.fonk2(b2)
        self.b3 = 'Currently unnamed.'
    def fonk2(self, b2):
        if isinstance(b2, str):
            if b2 = = '0':
                return np.zeros(self.b1.dim, b4 = complex)
            else:
                b5 = np.zeros(self.b1.dim, b4=complex)
                b6 = b2.split('+')
                for term in b6:
                    coefficient, b3 = term.split('*')
                    if b3 in self.b1.element_names:
                        b7 = self.b1.element_names.b7(b3)
                        b5[b7] = complex(coefficient)
                return b5
        return b2
    def fonk3(self, other):
        b8 = self.fonk4(other)
        b9 = self.fonk5(other)
        b10 = globals().get(f'{b8}Element')
        return b10(b9, AlgebraList[f'{self.b1.b3}(T){other.b1.b3}'])
    def fonk4(self, other):
        if self.b1.b11 = = 'HopfAlgebra' and other.b1.b11 == 'HopfAlgebra':
            return 'HopfAlgebra'
        elif self.b1.b11 = = 'Algebra' or other.b1.b11 == 'Algebra':
            return 'Algebra'
        elif (self.b1.b11 in ['ModuleAlgebra', 'HopfAlgebra'] and
              other.b1.b11 in ['ModuleAlgebra', 'HopfAlgebra']):
            return 'ModuleAlgebra'
        return 'VectorSpace'
    def fonk5(self, other):
        b9 = np.zeros(self.b1.dim * other.b1.dim, b4=complex)
        for i in range(self.b1.dim):
            for j in range(other.b1.dim):
                b9[i * other.b1.dim + j] = self.b2[i] * other.b2[j]
        return b9
    def fonk6(self, other):
        b10 = globals().get(f'{self.b1.b11}Element')
        return b10(self.b2 + other.b2, self.b1)
    def fonk7(self, other):
        b10 = globals().get(f'{self.b1.b11}Element')
        return b10(self.b2 - other.b2, self.b1)
    def fonk8(self):
        if self.b3 = = 'Currently unnamed.':
            b12 = [f'{self.b2[i]}*{self.b1.element_names[i]}'
                     for i in range(self.b1.dim) if self.b2[i] != 0]
            self.b3 = '+'.join(b12) if b12 else '0'
        return self.b3
class class2(class1):
    def fonk9(self, other):
        if isinstance(other, (complex, int, float, np.complex128)):
            b10 = globals().get(f'{self.b1.b11}Element')
            return b10(other * self.b2, self.b1)
        elif self.b1 = = other.b1:
            b13 = self.b1.multiply(self.b2, other.b2)
            b10 = globals().get(f'{self.b1.b11}Element')
            return b10(b13, self.b1)
        elif other.b1.b11 in ['Module', 'ModuleAlgebra']:
            b14 = other.b1.action(self.b2, other.b2)
            return class6(b14, other.b1)
    def fonk10(self, b16):
        b15 = self
        if b16 = = 0:
            b17 = np.zeros(self.b2.shape[0])
            b17[0] = 1
            b10 = globals().get(f'{self.b1.b11}Element')
            return b10(b17, self.b1)
        for _ in range(b16 - 1):
            b15 *= self
        return b15
class class3(class1):
    def fonk11(self):
        if self.b1.b11 = = 'CoAlgebra':
            b13 = self.b1.fonk11(self.b2)
            return class3(b13, AlgebraList[f'{self.b1.b3}(T){self.b1.b3}'])
        elif self.b1.b11 = = 'HopfAlgebra':
            b13 = self.b1.fonk11(self.b2)
            return class4(b13, AlgebraList[f'{self.b1.b3}(T){self.b1.b3}'])
    def fonk12(self):
        return self.b1.fonk12(self.b2)
class class4(class2, class3):
    def fonk13(self):
        return class4(self.b1.fonk13(self.b2), self.b1)
class class5(class1):
    def fonk14(self, ring_element):
        b2 = self.b1.action(ring_element.b2, self.b2)
        b10 = globals().get(f'{self.b1.b11}Element')
        return b10(b2, self.b1)
class class6(class5, class2):
    def fonk15(self, other):
        b2 = ProdVectorToTensorVector(self.b2, other.b2)
        return class6(b2, AlgebraList[f'{self.b1.b3}{other.b1.b3}'])
if b18 = = '__main__':
    pass