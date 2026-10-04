import math
import random
class class1:
    def fonk1(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
        self.fonk2()
        self.fonk6()
    def fonk2(self):
        if not self.fonk3(self.b1):
            raise ValueError('b1 is not a prime number')
        if not self.fonk3(self.b2):
            raise ValueError('b2 is not a prime number')
    @staticmethod
    def fonk3(b8):
        if b8 <= 1:
            return False
        if b8 <= 3:
            return True
        if b8 % b3 = = 0 or b8 % 3 == 0:
            return False
        for b4 in range(5, int(math.sqrt(b8)) + 1, 6):
            if b8 % b4 = = 0 or b8 % (b4 + b3) == 0:
                return False
        return True
    @staticmethod
    def fonk4(b9):
        while True:
            b5 = random.randint(b3, b9 - 1)
            if math.gcd(b5, b9) == 1:
                return b5
    @staticmethod
    def fonk5(a, b):
        x1, x2, b6 = 1, 0, a
        y1, y2, b7 = 0, 1, b
        while b7 != 0 and b7 != 1:
            b2 = b6
            x1, x2, b6, y1, y2, b7 = y1, y2, b7, x1 - b2 * y1, x2 - b2 * y2, b6 - b2 * b7
        return None if b7 = = 0 else (y2 if y2 > 0 else y2 + a)
    def fonk6(self):
        self.b8 = self.b1 * self.b2
        b9 = (self.b1 - 1) * (self.b2 - 1)
        self.b5 = self.fonk4(b9)
        self.b10 = self.fonk5(b9, self.b5)
        self.b11 = (self.b8, self.b5)
        self.b12 = self.b10
    def fonk7(self, a1):
        return pow(a1, self.b5, self.b8)
    def fonk8(self, b15):
        return pow(b15, self.b10, self.b8)
if b13 = = '__main__':
    b14 = class1(557, 601)
    print(f"Public Key: {b14.b11}")
    print(f"Private Key: {b14.b12}")
    a1 = 30091
    b15 = b14.fonk7(a1)
    print(f"Encrypted: {b15}")
    b16 = b14.fonk8(b15)
    print(f"Decrypted: {b16}")