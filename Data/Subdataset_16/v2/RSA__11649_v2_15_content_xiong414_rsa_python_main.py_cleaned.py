import math
import random
class class1:
    def fonk1(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
        if not self.fonk2(self.b1):
            raise ValueError("b1 is not a prime number")
        if not self.fonk2(self.b2):
            raise ValueError("b2 is not a prime number")
        self.b3 = self.b1 * self.b2
        self.b4 = (self.b1 - 1) * (self.b2 - 1)
        self.b5 = self.fonk3(self.b4)
        self.b6 = self.fonk4(self.b5, self.b4)
    def fonk2(self, b3):
        if b3 <= 1:
            return False
        for b7 in range(2, int(math.sqrt(b3)) + 1):
            if b3 % b7 = = 0:
                return False
        return True
    def fonk3(self, b4):
        b5 = random.randint(2, b4 - 1)
        while math.gcd(b5, b4) != 1:
            b5 = random.randint(2, b4 - 1)
        return b5
    def fonk4(self, a, b):
        x1, x2, b8 = 1, 0, a
        y1, y2, b9 = 0, 1, b
        while b9 != 0:
            b2 = b8
            t1, t2, b10 = x1 - b2 * y1, x2 - b2 * y2, b8 - b2 * b9
            x1, x2, b8 = y1, y2, b9
            y1, y2, b9 = t1, t2, b10
        return x1 % b if x1 % b > 0 else x1 % b + b
    def fonk5(self, a1):
        return pow(a1, self.b5, self.b3)
    def fonk6(self, b13):
        return pow(b13, self.b6, self.b3)
if b11 = = '__main__':
    b12 = class1(557, 601)
    print("Public Key: (b3 = {}, b5={})".format(b12.b3, b12.b5))
    print("Private Key: b6 = {}".format(b12.b6))
    a1 = 30091
    b13 = b12.fonk5(a1)
    print("Encrypted:", b13)
    b14 = b12.fonk6(b13)
    print("Decrypted:", b14)