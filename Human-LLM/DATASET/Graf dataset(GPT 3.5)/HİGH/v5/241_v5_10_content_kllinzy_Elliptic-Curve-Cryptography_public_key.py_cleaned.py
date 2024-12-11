from b2 import Curve
from point import Point
class class1:
    def fonk1(self, modulus: int, factor: int):
        self.b1 = modulus
        self.b2 = Curve.make_curve(self.b1)
        self.b3 = self.b2.random_point()
        self.b4 = self.b2.multiply(factor, self.b3)
    def fonk2(self) -> str:
        return f"Curve: {self.b2}\nPublic Key (b3): {self.b3}\nDerived Public Key (b4): {self.b4}"
    @staticmethod
    def fonk3(modulus: int, factor: int) -> 'class1':
        return class1(modulus, factor)