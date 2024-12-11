import random
def fonk1(b1 = 256):
    b2 = random.getrandbits(b1) | 1
    while not fonk2(b2):
        b2 += 2
    return b2
def fonk2(b10, b3 = 90):
    if b10 <= 1:
        return False
    b4 = [random.randrange(2, 50000) for _ in range(b3)]
    for b5 in b4:
        if b10 % b5 = = 0:
            return False
    tests, b6 = 0, 0
    b7 = b10 - 1
    while not b7 & 1:
        b7 >>= 1
        b6 += 1
    for b5 in b4:
        tests += 1
        b8 = fonk3(b7, b6, b5, b10)
        if not b8:
            return False
    return True
def fonk3(b7, b6, b5, b10):
    b9 = pow(b5, b7, b10)
    for _ in range(b6):
        if (b9 = = 1 and b6 == 0) or (b9 == b10 - 1):
            return True
        b9 = pow(b9, 2, b10)
    return False
class class1:
    def fonk4(self, b1):
        self.b10 = self.fonk6(b1)
        b11 = self.fonk8(self.b10)
        b12 = random.getrandbits(b11)
        self.fonk7(b12)
    def fonk5(self, b1):
        while True:
            b13 = fonk1(b1)
            if b13 & b14 = = b14:
                return b13
    def fonk6(self, b1):
        b13 = self.fonk5(b1
        while True:
            b15 = self.fonk5(b1
            if b13 != b15:
                return b13 * b15
    def fonk7(self, b12):
        self.b16 = b12 % self.b10
    def fonk8(self, x):
        assert x > 0
        b11 = 0
        while x:
            b11 += 1
            x >>= 1
        return b11
    def fonk9(self, num_bits):
        a1 = 0
        for _ in range(num_bits):
            self.b16 = (self.b16 ** 2) % self.b10
            a1 = (a1 << 1) | (self.b16 & 1)
        return a1
if b17 = = "__main__":
    b18 = class1(128)
    print("type: u")
    print("numbit: 32")
    print("count: 5000000")
    for _ in range(5000000):
        print(b18.fonk9(32))