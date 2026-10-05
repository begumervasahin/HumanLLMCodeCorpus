from b2 import Curve
from point import Point
class class1:
    def fonk1(self, b1, factor):
        self.b1 = b1
        self.b2 = Curve.make_curve(self.b1)
        self.b3 = self.b2.random_point()
        self.b4 = self.b2.multiply(factor, self.b3)
    def fonk2(self):
        b5 = f"Curve: {self.b2}"
        b6 = f"Public Key (b3): {self.b3}"
        b7 = f"Derived Public Key (b4): {self.b4}"
        return f"{b5}\n{b6}\n{b7}"
    @staticmethod
    def fonk3(b1, factor):
        return class1(b1, factor)
b8 = class1(23, 5)
print(b8)
b9 = class1.fonk3(47, 9)
print(b9)
