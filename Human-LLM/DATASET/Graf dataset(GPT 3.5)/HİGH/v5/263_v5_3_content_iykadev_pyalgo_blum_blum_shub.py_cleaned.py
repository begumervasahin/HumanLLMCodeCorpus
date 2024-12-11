import sys
import random
class class1:
    @staticmethod
    def fonk1(b7):
        if b7 <= 1:
            return False
        b1 = [random.randrange(2, 50000) for _ in range(90)]
        for b2 in b1:
            if b7 % b2 = = 0:
                return False
        tests, b3 = 0, 0
        b4 = b7 - 1
        while not b4 & 1:
            b4 >>= 1
            b3 += 1
        for b2 in b1:
            tests += 1
            b5 = class1.fonk2(b4, b3, b2, b7)
            if not b5:
                break
        if b5:
            return (1 - (1. / (b10 ** tests)))
        return False
    @staticmethod
    def fonk2(b4, b3, b2, b7):
        b6 = pow(b2, b4, b7)
        for _ in range(b3):
            if (b6 = = 1 and _ == 0) or (b6 == b7 - 1):
                return True
            b6 = pow(b6, 2, b7)
        return False
class class2:
    def fonk3(self, bits):
        self.b7 = self.fonk5(bits)
        b8 = random.getrandbits(self.fonk7(self.b7))
        self.fonk6(b8)
    def fonk4(self, bits):
        while True:
            b9 = random.getrandbits(bits)
            if class1.fonk1(b9) and b9 % b10 = = 3:
                return b9
    def fonk5(self, bits):
        b9 = self.fonk4(bits
        while True:
            b11 = self.fonk4(bits
            if b9 != b11:
                return b9 * b11
    def fonk6(self, b8):
        self.b12 = b8 % self.b7
    def fonk7(self, x):
        assert x > 0
        b11 = 0
        while x:
            b11 += 1
            x >>= 1
        return b11
    def fonk8(self, num_bits):
        a1 = 0
        for _ in range(num_bits):
            self.b12 = (self.b12 ** 2) % self.b7
            a1 = (a1 << 1) | (self.b12 & 1)
        return a1
if b13 = = "__main__":
    b14 = class2(128)
    print("type: u")
    print("numbit: 32")
    print("count: 5000000")
    for _ in range(5000000):
        print(b14.fonk8(32))