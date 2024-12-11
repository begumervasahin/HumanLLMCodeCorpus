import numpy as np
class class1:
    def fonk1(self, b1, b4):
        if not isinstance(b1, str):
            self.b1 = b1
        elif b1 = = '0':
            self.b1 = np.zeros((b4.dim))
        else:
            self.b1 = np.zeros((b4.dim), dtype=complex)
            b2 = b1.split('+')
            for item in b2:
                b3 = item.split('*')
                for i in range(b4.dim):
                    if b3[1] == b4.element_names[i]:
                        self.b1[i] = complex(b3[0])
                        break
        self.b4 = b4
        self.b5 = 'Currently unnamed.'
    def fonk2(self, b9):
        b6 = ''
        if self.b4.b7 = = 'HopfAlgebra' and b9.b4.b7 == 'HopfAlgebra':
            b6 = 'HopfAlgebra'
        elif self.b4.b7 = = 'Algebra' or b9.b4.b7:
            b6 = 'Algebra'
        elif (self.b4.b7 = = 'ModuleAlgebra' or self.b4.b7 == 'HopfAlgebra') and (
                b9.b4.b7 = = 'HopfAlgebra' or b9.b4.b7 == 'ModuleAlgebra'):
            b6 = 'ModuleAlgebra'
        else:
            b6 = 'VectorSpace'
        b8 = np.zeros((self.b4.dim * b9.b4.dim), dtype=complex)
        for i in range(self.b4.dim):
            for j in range(b9.b4.dim):
                b8[i * b9.b4.dim + j] = self.b1[i] * b9.b1[j]
        return eval(b6 + 'Element(b8, AlgebraList[\'' + self.b4.b5 + '(T)' + b9.b4.b5 + '\'])')
    def fonk3(self, b9):
        return eval(self.b4.b7 + 'Element(self.b1 + b9.b1, self.b4)')
    def fonk4(self, b9):
        return eval(self.b4.b7 + 'Element(self.b1 - b9.b1, self.b4)')
    def fonk5(self):
        if self.b5 = = 'Currently unnamed.':
            self.b5 = ''
            for i in range(self.b4.dim):
                if self.b1[i] != 0:
                    self.b5 = self.b5 + '+' + str(self.b1[i]) + '*' + self.b4.element_names[i]
            if self.b5 = = '':
                self.b5 = '0'
            return self.b5
        else:
            return self.b5
class class2(class1):
    def fonk6(self, b9):
        if isinstance(b9, (complex, int, float, np.complex128)):
            return eval(self.b4.b7 + 'Element(b9 * self.b1, self.b4)')
        elif self.b4 = = b9.b4:
            return eval(self.b4.b7 + 'Element(self.b4.Mult(self.b1, b9.b1), self.b4)')
        elif b9.b4.b7 = = 'Module':
            return class6(b9.b4.Action(self.b1, b9.b1), b9.b4)
        elif b9.b4.b7 = = 'ModuleAlgebra':
            return class6(b9.b4.Action(self.b1, b9.b1), b9.b4)
    def fonk7(self, b9):
        b8 = self
        if b9 = = 0:
            b2 = np.zeros(self.b1.shape[0])
            b2[0] = 1
            b8 = eval(self.b4.b7 + 'Element(b2, self.b4)')
        else:
            for _ in range(b9 - 1):
                b8 = b8 * self
        return b8
class class3(class1):
    def fonk8(self):
        if self.b4.b7 = = 'CoAlgebra':
            return class3(self.b4.fonk8(self.b1), AlgebraList[self.b4.b5 + '(T)' + self.b4.b5])
        if self.b4.b7 = = 'HopfAlgebra':
            return class4(self.b4.fonk8(self.b1), AlgebraList[self.b4.b5 + '(T)' + self.b4.b5])
    def fonk9(self):
        return self.b4.fonk9(self.b1)
class class4(class2, class3):
    def fonk10(self):
        return class4(self.b4.fonk10(self.b1), self.b4)
class class5(class1):
    def fonk11(self, ring_element):
        b1 = self.b4.Action(ring_element.b1, self.b1)
        return eval(self.b4.b7 + 'Element(b1, self.b4)')
class class6(class5, class2):
    def fonk12(self, b9):
        b1 = ProdVectorToTensorVector(self.b1, b9.b1)
        return class6(b1, AlgebraList[self.b4.b5])
