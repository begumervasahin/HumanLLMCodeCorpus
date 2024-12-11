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