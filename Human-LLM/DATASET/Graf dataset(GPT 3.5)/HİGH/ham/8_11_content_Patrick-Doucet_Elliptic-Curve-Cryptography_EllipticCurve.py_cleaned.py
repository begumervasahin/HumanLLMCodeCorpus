import matplotlib.pyplot as plt
import math
from numpy import arange
from numpy import meshgrid
class class1:
    def fonk1(self, b1, b2, b3, b4, b5, b6):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
        self.b6 = b6
    def fonk2(self, b5):
        b7 = list()
        b8 = list()
        for b18 in range(0, b5):
            b7.append(b18)
            b8.append(math.sqrt(b18**3 + self.b2*b18 + self.b3))
        plt.fonk2(b7, b8)
        plt.show()
class class2(class1):
    def fonk3(self, b9, b10, b11):
        self.b9 = b9
        self.b10 = b10
        self.b11 = b11
    def fonk4(self, other):
        if self.b9 < other.b9:
            b2 = self
            b3 = other
        else:
            b2 = other
            b3 = self
        if (b2.b9 = = 0 and b2.b10 == 0):
            return b3
        elif (b3.b9 = = 0 and b3.b10 == 0):
            return b2
        elif b3 = = b2.fonk6():
            return class2(0,0,b2.b11)
        else:
            if b2 = = b3:
                b12 = (3 * (b2.b9**2) + b2.b11.b2) * b2.fonk5(2*b2.b10)
            else:
                b12 = (b3.b10-b2.b10) * b2.fonk5(b3.b9 - b2.b9)
        b13 = class2(0,0,b2.b11)
        b13.b9 = ((b12**2 % b2.b11.b1) - b2.b9 - b3.b9) % b2.b11.b1
        b13.b10 = (b12*(b2.b9 - b13.b9) - b2.b10) % b2.b11.b1
        return b13
    def fonk5(self, b9):
        return pow(int(b9), self.b11.b1-2, self.b11.b1)
    def fonk6(self):
        if self.b9 = = 0 and self.b10 == 0:
            return self
        return class2(self.b9, (-self.b10) % self.b11.b1, self.b11)
    def fonk7(self, other):
        return self.b9 = = other.b9 and self.b10 == other.b10 and self.b11 == other.b11
    def fonk8(self, other):
        return self.b9 != other.b9 or self.b10 != other.b10 or self.b11 != other.b11
    def fonk9(self, b2):
        b14 = []
        b15 = b2
        while b15 != 0:
            b14.append(b15%2)
            b15 = b15
        b16 = class2(self.b9, self.b10, self.b11)
        b17 = class2(self.b9, self.b10, self.b11)
        b14.pop()
        b14.reverse()
        for b18 in b14:
            if b18 = = 0:
                b16 = b16 + b16
                b16.b9 = b16.b9 % self.b11.b1
                b16.b10 = b16.b10 % self.b11.b1
            else:
                b16 = b16 + b16
                b16.b9 = b16.b9 % self.b11.b1
                b16.b10 = b16.b10 % self.b11.b1
                b16 = b16 + b17
                b16.b9 = b16.b9 % self.b11.b1
                b16.b10 = b16.b10 % self.b11.b1
        return b16