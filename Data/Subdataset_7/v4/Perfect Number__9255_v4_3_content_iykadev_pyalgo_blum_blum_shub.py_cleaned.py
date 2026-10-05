import sys
import random
def fonk1(b1 = 256):
    b2 = random.getrandbits(b1) | 1
    while 1:
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
            break
    if b7:
        return (1 - (1. / (4 ** tests)))
    return False
def fonk3(b6, b5, b4, b9):
    b8 = pow(b4, b6, b9)
    for _ in range(b5):
        if (b8 = = 1 and _ == 0) or (b8 == b9 - 1):
            return True
        b8 = pow(b8, 2, b9)
    return False
class class1:
    def fonk4(self, b1):
        self.b9 = self._generate_n(b1)
        b10 = self.fonk6(self.b9)
        b11 = random.getrandbits(b10)
        self.set_seed(b11)
    def fonk5(self, b1):
        """
        Generate appropriate prime number for use in Blum-Blum-Shub.
        This generates the appropriate primes (b12 = 3 mod 4) needed to compute the
        "b9-value" for Blum-Blum-Shub algorithm.
        b1 - Number of b1 in prime
        This generates the "b9 value" for use in the Blum-Blum-Shub algorithm.
        b1 - The number of b1 of security
        Sets or resets the b11 value and internal b13.
        b11 - The new b11
        """
        self.b13 = b11 % self.b9
    def fonk6(self, x):
        "Get the bit b10 of a positive number"
        assert x > 0
        a1 = 0
        while x:
            a1 += 1
            x >>= 1
        return a1
    def fonk7(self, num_bits):
        "Returns up to num_bits random b1"
        a2 = 0
        for _ in range(num_bits):
            self.b13 = (self.b13 ** 2) % self.b9
            a2 = (a2 << 1) | (self.b13 & 1)
        return a2
if b14 = = "__main__":
    b15 = class1(128)
    print("type: u")
    print("numbit: 32")
    print("count: 5000000")
    for _ in range(5000000):
        print(b15.fonk7(32))