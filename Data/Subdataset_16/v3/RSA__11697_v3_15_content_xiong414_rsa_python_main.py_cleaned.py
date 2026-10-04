import math
import random
class class1:
    def fonk1(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
        self.fonk2()
        self.b3 = self.b1 * self.b2
        self.b4 = (self.b1 - 1) * (self.b2 - 1)
        self.b5 = self.fonk4(self.b4)
        self.b6 = self.fonk5(self.b5, self.b4)
    def fonk2(self):
        if not self.fonk3(self.b1):
            raise ValueError("b1 is not a prime number")
        if not self.fonk3(self.b2):
            raise ValueError("b2 is not a prime number")
    def fonk3(self, b3):
        if b3 <= 1:
            return False
        for b7 in range(2, int(math.sqrt(b3)) + 1):
            if b3 % b7 = = 0:
                return False
        return True
    def fonk4(self, b4):
        while True:
            b5 = random.randint(2, b4 - 1)
            if math.gcd(b5, b4) == 1:
                return b5
    def fonk5(self, a, b):
        x1, x2, b8 = 1, 0, a
        y1, y2, b9 = 0, 1, b
        while b9 != 0:
            b2 = b8
            x1, x2, b8, y1, y2, b9 = y1, y2, b9, x1 - b2 * y1, x2 - b2 * y2, b8 - b2 * b9
        return x1 % b if x1 > 0 else x1 % b + b
    def fonk6(self, a1):
        return pow(a1, self.b5, self.b3)
    def fonk7(self, b12):
        return pow(b12, self.b6, self.b3)
if b10 = = '__main__':
    b11 = class1(557, 601)
    print(f"Public Key: (b3 = {b11.b3}, b5={b11.b5})")
    print(f"Private Key: b6 = {b11.b6}")
    a1 = 30091
    b12 = b11.fonk6(a1)
    print(f"Encrypted: {b12}")
    b13 = b11.fonk7(b12)
    print(f"Decrypted: {b13}")