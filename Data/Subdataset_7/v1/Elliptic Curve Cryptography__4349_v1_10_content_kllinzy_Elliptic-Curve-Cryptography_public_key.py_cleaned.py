from b1 import Curve
from point import Point
class class1:
    b1 = None
    a1 = 0
    b2 = None
    b3 = None
    def fonk1(self, a1, k):
        self.a1 = a1
        self.b1 = Curve.make_curve(self.a1)
        self.b2 = self.b1.random_point()
        self.b3 = self.b1.multiply(k, self.b2)
    def fonk2(self):
        return f"Curve: {self.b1}\nPublic Key (b2): {self.b2}\nDerived Public Key (b3): {self.b3}"
    @staticmethod
    def fonk3(a1, k):
        return class1(a1, k)
b4 = class1(23, 5)
print(b4)
b5 = class1.fonk3(47, 9)
print(b5)
