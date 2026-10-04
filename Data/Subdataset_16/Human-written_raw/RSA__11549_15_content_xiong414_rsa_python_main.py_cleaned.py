import math, random
import numpy as np
class class1():
    def fonk1(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
        if self.fonk2(self.b1) is False:
            print('pä¸æ¯ç´ æ°')
        elif self.fonk2(self.b2) is False:
            print('qä¸æ¯ç´ æ°')
        else:
            self.fonk5()
    def fonk2(self, b14):
        b3 = b14
        b1 = 2
        while (b1 <= math.sqrt(b3)):
            if (b3 % b1 = = 0):
                b3
            else:
                b1 += 1
        if b3 = = b14:
            return True
        else:
            return False
    def fonk3(self, b15):
        b4 = random.randint(2, b15 - 1)
        if math.gcd(b4, b15) != 1:
            return self.fonk3(b15)
        else:
            return b4
    def fonk4(self, a, b):
        b9, b10, b11, b12, b13, b5 = 1, 0, a, 0, 1, b
        while (b5 > 1):
            b2 = b11
            b6 = b9 - b2 * b12
            b7 = b10 - b2 * b13
            b8 = b11 - b2 * b5
            b9 = b12
            b10 = b13
            b11 = b5
            b12 = b6
            b13 = b7
            b5 = b8
        if b5 = = 0:
            return -1
        elif b13 > 0:
            return b13
        else:
            return b13 + a
    def fonk5(self):
        self.b14 = self.b1 * self.b2
        b15 = (self.b1 - 1) * (self.b2 - 1)
        self.b4 = self.fonk3(b15)
        self.b16 = self.fonk4(b15, self.b4)
        return [(self.b14, self.b4), self.b16]
    def fonk6(self, inp):
        return inp ** self.b4 % self.b14
    def fonk7(self, inp):
        return inp ** self.b16 % self.b14
if b17 = = '__main__':
    b18 = class1(557, 601)
    print(b18.fonk5())
    b19 = b18.fonk6(30091)
    print(b19)
    print(b18.fonk7(b19))