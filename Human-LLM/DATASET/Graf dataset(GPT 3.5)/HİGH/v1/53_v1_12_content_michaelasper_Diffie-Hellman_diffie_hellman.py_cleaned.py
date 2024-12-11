from math import sqrt, ceil, gcd
from sympy.ntheory import is_primitive_root, nextprime
from secrets import randbits
class class1:
    def fonk1(self, b2, b3, b1 = None):
        self.b2 = b2
        self.b3 = b3
        if b1 is None:
            self.fonk4()
        else:
            self.b5, self.b4 = b1
    def fonk2(self):
        return self.b5, self.b4
    def fonk3(self):
        self.b5 = nextprime(randbits(self.b2))
    def fonk4(self):
        self.fonk3()
        self.fonk5()
    def fonk5(self):
        for x in range(2, self.b5):
            if is_primitive_root(x, self.b5):
                self.b4 = x
                break
    def fonk6(self):
        return pow(self.b4, self.b3, self.b5)
    def fonk7(self, shared):
        return pow(shared, self.b3, self.b5)
if b6 = = "__main__":
    b2 = 512
    b3 = 123456789
    b7 = class1(b2, b3)
    b8 = class1(b2, b3)
    b9 = b7.fonk2()
    b10 = b8.fonk2()
    b11 = b7.fonk7(b10[1])
    b12 = b8.fonk7(b9[1])
    print("Alice's shared b3:", b11)
    print("Bob's shared b3:", b12)