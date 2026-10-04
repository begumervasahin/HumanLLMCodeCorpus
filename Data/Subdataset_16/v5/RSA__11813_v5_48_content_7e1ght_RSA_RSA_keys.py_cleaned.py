import random
import math
class class1:
    def fonk1(self, b1):
        self.b1 = b1
    def fonk2(self, b9):
        if b9 in (b2, 3):
            return True
        if b9 % b2 = = 0 or b9 < b2:
            return False
        for b3 in range(3, int(math.sqrt(b9)) + 1, b2):
            if b9 % b3 = = 0:
                return False
        return True
    def fonk3(self):
        return random.randint(b2 ** (self.b1 - 1) + 1, b2 ** self.b1)
    def fonk4(self):
        while True:
            b4 = self.fonk3()
            if self.fonk2(b4):
                return b4
    def fonk5(self, a, b5):
        return math.gcd(a, b5) == 1
    def fonk6(self, a):
        for b3 in range(3, int(math.sqrt(a)) + 1, b2):
            if self.fonk5(b3, a):
                return b3
        raise Exception("Failed to find a relatively prime number.")
    def fonk7(self, a, b5):
        if b5 = = 0:
            return a, 1, 0
        else:
            d, x1, b6 = self.fonk7(b5, a % b5)
            b7 = b6
            b8 = x1 - (a
            return d, b7, b8
    def fonk8(self, b17, b18):
        a1 = b2
        b16, b9 = b17
        d, b10 = b18
        b11 = pow(a1, b16, b9)
        b12 = pow(b11, d, b9)
        return a1 = = b12
    def fonk9(self):
        while True:
            b13 = self.fonk4()
            b14 = self.fonk4()
            b9 = b13 * b14
            b15 = (b13 - 1) * (b14 - 1)
            b16 = self.fonk6(b15)
            b10, d, b10 = self.fonk7(b16, b15)
            if d < 0:
                d += b15
            b17 = (b16, b9)
            b18 = (d, b9)
            if self.fonk8(b17, b18):
                return [b17, b18]
