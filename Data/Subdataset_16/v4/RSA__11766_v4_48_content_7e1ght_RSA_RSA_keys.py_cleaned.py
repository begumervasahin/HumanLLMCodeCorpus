import random
import math
class class1:
    def fonk1(self, b1):
        self.b1 = b1
    def fonk2(self, b15):
        if b15 in (b2, 3):
            return True
        if b15 % b2 = = 0 or b15 < b2:
            return False
        for b3 in range(3, int(math.sqrt(b15)) + 1, b2):
            if b15 % b3 = = 0:
                return False
        return True
    def fonk3(self):
        return random.randint(b2**(self.b1 - 1) + 1, b2**self.b1)
    def fonk4(self):
        b4 = self.fonk3()
        while not self.fonk2(b4):
            b4 = self.fonk3()
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
    def fonk8(self, keys):
        a1 = b2
        public_key, b9 = keys
        b10 = pow(a1, public_key[0], public_key[1])
        b11 = pow(b10, b9[0], b9[1])
        return a1 = = b11
    def fonk9(self):
        b12 = False
        while not b12:
            b13 = self.fonk4()
            b14 = self.fonk4()
            b15 = b13 * b14
            b16 = (b13 - 1) * (b14 - 1)
            b17 = self.fonk6(b16)
            b18, d, b18 = self.fonk7(b17, b16)
            if d < 0:
                d += b16
            b12 = self.fonk8([[b17, b15], [d, b15]])
        return [[b17, b15], [d, b15]]