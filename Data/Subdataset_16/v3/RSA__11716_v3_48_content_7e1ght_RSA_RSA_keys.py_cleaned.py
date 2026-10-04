from random import randint
from math import gcd
class class1:
    def fonk1(self, b1):
        self.b1 = b1
    def fonk2(self, b12):
        if b12 <= 1:
            return False
        if b12 <= 3:
            return True
        if b12 % b2 = = 0 or b12 % 3 == 0:
            return False
        a1 = 5
        while a1 * a1 <= b12:
            if b12 % a1 = = 0 or b12 % (a1 + b2) == 0:
                return False
            a1 += 6
        return True
    def fonk3(self):
        return randint(b2**(self.b1 - 1) + 1, b2**self.b1 - 1)
    def fonk4(self):
        b3 = self.fonk3()
        while not self.fonk2(b3):
            b3 = self.fonk3()
        return b3
    def fonk5(self, b13):
        for a1 in range(3, b13):
            if gcd(a1, b13) == 1:
                return a1
        raise Exception("Failed to find a relative prime number.")
    def fonk6(self, a, b4):
        if b4 = = 0:
            return a, 1, 0
        d, x1, b5 = self.fonk6(b4, a % b4)
        b6 = b5
        b7 = x1 - (a
        return d, b6, b7
    def fonk7(self, b16, b17):
        a2 = b2
        b8 = pow(a2, b16[0], b16[1])
        b9 = pow(b8, b17[0], b17[1])
        return a2 = = b9
    def fonk8(self):
        while True:
            b10 = self.fonk4()
            b11 = self.fonk4()
            b12 = b10 * b11
            b13 = (b10 - 1) * (b11 - 1)
            b14 = self.fonk5(b13)
            b15, d, b15 = self.fonk6(b14, b13)
            if d < 0:
                d += b13
            b16 = (b14, b12)
            b17 = (d, b12)
            if self.fonk7(b16, b17):
                return b16, b17
if b18 = = "__main__":
    b19 = class1(16)
    b16, b17 = b19.fonk8()
    print("Public Key:", b16)
    print("Private Key:", b17)