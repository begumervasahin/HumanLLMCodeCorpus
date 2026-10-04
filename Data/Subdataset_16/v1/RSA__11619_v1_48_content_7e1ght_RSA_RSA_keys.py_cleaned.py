from random import randint
from math import gcd
class class1:
    def fonk1(self, bitSize):
        self.b1 = bitSize
    def fonk2(self, b14):
        if b14 in (b2, 3):
            return True
        if b14 % b2 = = 0 or b14 < b2:
            return False
        for b3 in range(3, int(b14**0.5) + 1, b2):
            if b14 % b3 = = 0:
                return False
        return True
    def fonk3(self):
        return randint(b2**(self.b1 - 1) + 1, b2**self.b1)
    def fonk4(self):
        b4 = self.fonk3()
        while not self.fonk2(b4):
            b4 = self.fonk3()
        return b4
    def fonk5(self, a, b5):
        return gcd(a, b5) == 1
    def fonk6(self, a):
        for b3 in range(3, a):
            if self.fonk5(b3, a):
                return b3
        raise Exception("ÐÐµ ÑÐ´Ð°Ð»Ð¾ÑÑ Ð½Ð°Ð¹ÑÐ¸ Ð¾ÑÐ½Ð¾ÑÐ¸ÑÐµÐ»ÑÐ½Ð¾ Ð¿ÑÐ¾ÑÑÐ¾Ðµ ÑÐ¸ÑÐ»Ð¾.")
    def fonk7(self, a, b5):
        if b5 = = 0:
            return a, 1, 0
        else:
            b17, x1, b6 = self.fonk7(b5, a % b5)
            b7 = b6
            b8 = x1 - (a
            return b17, b7, b8
    def fonk8(self, keys):
        a1 = b2
        b9 = pow(a1, keys[0][0], keys[0][1])
        b10 = pow(b9, keys[1][0], keys[1][1])
        return a1 = = b10
    def fonk9(self):
        b11 = False
        while not b11:
            b12 = self.fonk4()
            b13 = self.fonk4()
            b14 = b12 * b13
            b15 = (b12 - 1) * (b13 - 1)
            b16 = self.fonk6(b15)
            b17 = self.fonk7(b16, b15)[1]
            if b17 < 0:
                b17 = b17 + b15
            b11 = self.fonk8([[b16, b14], [b17, b14]])
        return [[b16, b14], [b17, b14]]
b18 = class1(16)
public_key, b19 = b18.fonk9()
print("Public class1:", public_key)
print("Private class1:", b19)