import matplotlib.pyplot as plt
import math
import numpy as np
class class1:
    def fonk1(self, b1, b2, b3, b4, b5, b6):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
        self.b6 = b6
    def fonk2(self, b5):
        b7 = []
        b8 = []
        for b13 in range(b5):
            b9 = (b13 ** 3 + self.b2 * b13 + self.b3) % self.b1
            if self.fonk3(b9):
                b10 = self.fonk4(b9)
                b7.append(b13)
                b8.append(b10)
                b7.append(b13)
                b8.append(self.b1 - b10)
        plt.scatter(b7, b8, b11 = 1)
        plt.xlabel("b13")
        plt.ylabel("b10")
        plt.title(f"Elliptic Curve: b10^b12 = b13^3 + {self.b2}b13 + {self.b3} (mod {self.b1})")
        plt.show()
    def fonk3(self, b13):
        return pow(b13, (self.b1 - 1)
    def fonk4(self, b13):
        return pow(b13, (self.b1 + 1)
class class2:
    def fonk5(self, b13, b10, b14):
        self.b13 = b13
        self.b10 = b10
        self.b14 = b14
    def fonk6(self, other):
        if self.b13 = = other.b13 and self.b10 == other.b10:
            return self.fonk7()
        elif self.b13 = = other.b13:
            return class2(0, 0, self.b14)
        b15 = (other.b10 - self.b10) * self.fonk8(other.b13 - self.b13)
        b16 = (b15 ** b12 - self.b13 - other.b13) % self.b14.b1
        b17 = (b15 * (self.b13 - b16) - self.b10) % self.b14.b1
        return class2(b16, b17, self.b14)
    def fonk7(self):
        b15 = (3 * self.b13 ** b12 + self.b14.b2) * self.fonk8(b12 * self.b10)
        b16 = (b15 ** b12 - b12 * self.b13) % self.b14.b1
        b17 = (b15 * (self.b13 - b16) - self.b10) % self.b14.b1
        return class2(b16, b17, self.b14)
    def fonk8(self, b13):
        return pow(b13, self.b14.b1 - b12, self.b14.b1)
    def fonk9(self):
        return class2(self.b13, -self.b10 % self.b14.b1, self.b14)
    def fonk10(self, other):
        return self.b13 = = other.b13 and self.b10 == other.b10 and self.b14 == other.b14
    def fonk11(self, other):
        return not self.fonk10(other)
    def fonk12(self, scalar):
        b18 = class2(0, 0, self.b14)
        b19 = self
        while scalar:
            if scalar & 1:
                b18 += b19
            b19 += b19
            scalar >>= 1
        return b18
    def fonk13(self):
        return f"Point({self.b13}, {self.b10})"
    def fonk14(self):
        return self.fonk13()
if b20 = = "__main__":
    b1 = 103
    b2 = 1
    b3 = 1
    b4 = class2(0, 1, None)
    b5 = 97
    b6 = 1
    b14 = class1(b1, b2, b3, b4, b5, b6)
    b4.b14 = b14
    b14.fonk2(b1)
    b21 = class2(3, 6, b14)
    print(f"Point: {b21}")
    b18 = b21.fonk12(10)
    print(f"10 * Point: {b18}")