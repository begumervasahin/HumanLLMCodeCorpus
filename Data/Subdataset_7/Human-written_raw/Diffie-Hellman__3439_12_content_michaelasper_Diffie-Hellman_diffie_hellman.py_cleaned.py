from math import sqrt, ceil, gcd
from sympy.ntheory import is_primitive_root, generate
from secrets import randbits
class class1(object):
    def fonk1(self, b2, b6, b1 = 0):
        self.b2 = b2
        self.b3 = randbits(b2)
        if b1 = =0:
            self.fonk4()
        else:
            self.b4 = b1[0]
            self.b5 = b1[1]
        self.b6 = b6
    def fonk2(self):
        return (self.b4, self.b5)
    def fonk3(self):
        self.b4 = generate.nextprime(self.b3)
    def fonk4(self):
        self.fonk3()
        self.fonk5()
        return self.b4, self.b5
    def fonk5(self):
        for x in range(2,self.b4):
            if is_primitive_root(x,self.b4):
                self.b5 = x
                break
    def fonk6(self):
        return pow(self.b5, self.b6, self.b4)
    def fonk7(self, shared):
        return pow(shared, self.b6, self.b4)