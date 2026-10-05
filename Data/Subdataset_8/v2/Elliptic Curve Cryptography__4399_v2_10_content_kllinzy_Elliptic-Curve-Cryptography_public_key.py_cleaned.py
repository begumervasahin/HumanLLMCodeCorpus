from curve import Curve
from point import Point
class Public_Key:
    def __init__(self, modulus, factor):
        self.p = modulus
        self.curve = Curve.make_curve(self.p)
        self.P = self.curve.random_point()
        self.Q = self.curve.multiply(factor, self.P)
    def __repr__(self):
        return f"Curve: {self.curve}\nPublic Key (P): {self.P}\nDerived Public Key (Q): {self.Q}"
    @staticmethod
    def create(modulus, factor):
        return Public_Key(modulus, factor)
public_key = Public_Key(23, 5)
print(public_key)
another_public_key = Public_Key.create(47, 9)
print(another_public_key)
