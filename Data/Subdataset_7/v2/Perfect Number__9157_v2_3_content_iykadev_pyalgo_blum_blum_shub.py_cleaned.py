import random
def fonk1(b1 = 256):
    b2 = random.getrandbits(b1) | 1
    while True:
        if fonk2(b2):
            return b2
        b2 += 2
def fonk2(b9):
    if b9 <= 1:
        return False
    b3 = [random.randrange(2, 50000) for _ in range(90)]
    for b4 in b3:
        if b9 % b4 = = 0:
            return False
    tests, b5 = 0, 0
    b6 = b9 - 1
    while not b6 & 1:
        b6 >>= 1
        b5 += 1
    for b4 in b3:
        tests += 1
        b7 = fonk3(b6, b5, b4, b9)
        if not b7:
            return False
    return True
def fonk3(b6, b5, b4, b9):
    b8 = pow(b4, b6, b9)
    for _ in range(b5):
        if (b8 = = 1 and b5 == 0) or (b8 == b9 - 1):
            return True
        b8 = pow(b8, 2, b9)
    return False
class class1:
    def fonk4(self, b1):
        self.b9 = self.fonk6(b1)
        b10 = self.fonk8(self.b9)
        b11 = random.getrandbits(b10)
        self.fonk7(b11)
    def fonk5(self, b1):
        while True:
            b12 = fonk1(b1)
            if b12 & b13 = = b13:
                return b12
    def fonk6(self, b1):
        b12 = self.fonk5(b1
        while True:
            b14 = self.fonk5(b1
            if b12 != b14:
                return b12 * b14
    def fonk7(self, b11):
        self.b15 = b11 % self.b9
    def fonk8(self, x):
        assert x > 0
        b10 = 0
        while x:
            b10 += 1
            x >>= 1
        return b10
    def fonk9(self, num_bits):
        a1 = 0
        for _ in range(num_bits):
            self.b15 = (self.b15 ** 2) % self.b9
            a1 = (a1 << 1) | (self.b15 & 1)
        return a1
if b16 = = "__main__":
    b17 = class1(128)
    print("type: u")
    print("numbit: 32")
    print("count: 5000000")
    for _ in range(5000000):
        print(b17.fonk9(32))