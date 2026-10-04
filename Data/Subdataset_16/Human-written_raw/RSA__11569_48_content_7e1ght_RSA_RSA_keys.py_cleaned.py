from random import *
from math import *
from os import urandom
class class1:
    def fonk1(self, bitSize):
        self.b1 = bitSize
    def fonk2(self, b2):
        if b2 = =b3 or b2==3: return True
        if b2%b3 = =0 or b2<b3: return False
        for b4 in range(3,int(b2**0.5)+1,b3):
            if b2%b4 = =0:
                return False
        return True
    def fonk3(self):
        return randint(b3**(self.b1-1)+1, b3**self.b1)
    def fonk4(self):
        b5 = self.fonk3()
        while not self.fonk2(b5):
            b5 = self.fonk3()
        return b5
    def fonk5(self, a, b8):
        b6 = a*b8
        while a != 0 and b8 != 0:
            if a > b8:
                a %= b8
            else:
                b8 %= a
        b7 = b6
        if b7 = = b6: return True
        else: return False
    def fonk6(self, a):
        for b4 in range(3, int(a**1/b3)):
            if self.fonk5(b4, a): return b4
        raise Exception("ÐÐµ ÑÐ´Ð°Ð»Ð¾ÑÑ Ð½Ð°Ð¹ÑÐ¸ Ð¾ÑÐ½Ð¾ÑÐ¸ÑÐµÐ»ÑÐ½Ð¾ Ð¿ÑÐ¾ÑÑÐ¾Ðµ ÑÐ¸ÑÐ»Ð¾.")
    def fonk7(self, a, b8):
        if b8 = = 0:
            return a, 1, 0
        else:
            b19, x1, b9 = self.fonk7(b8, a%b8)
            b10 = b9
            b11 = x1-(a
            return b19, b10, b11
    def fonk8(self, keys):
        a1 = b3
        b12 = a1**keys[0][0]%keys[0][1]
        b13 = b12**keys[1][0]%keys[1][1]
        return a1 = = b13
    def fonk9(self):
        b14 = False
        while not b14:
            b15 = self.fonk4()
            b16 = self.fonk4()
            b2 = b15 * b16
            b17 = (b15-1) * (b16-1)
            b18 = self.fonk6(b17)
            b19 = self.fonk7(b18, b17)[1]
            if b19 < 0:
                b19 = b19+abs(b19)*b18+1
            b14 = self.fonk8([[b18, b2], [b19, b2]])
        return [[b18, b2], [b19, b2]]