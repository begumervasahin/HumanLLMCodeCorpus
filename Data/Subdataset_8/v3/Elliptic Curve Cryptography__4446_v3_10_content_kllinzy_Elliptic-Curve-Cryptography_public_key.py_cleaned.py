from curve import Curve
from point import Point
class Public_Key:
    def __init__(self, p, factor):
        self.p = p
        self.curve = Curve.make_curve(self.p)
        self.P = self.curve.random_point()
        self.Q = self.curve.multiply(factor, self.P)
    def __repr__(self):
        curve_repr = f"Curve: {self.curve}"
        public_key_repr = f"Public Key (P): {self.P}"
        derived_key_repr = f"Derived Public Key (Q): {self.Q}"
        return f"{curve_repr}\n{public_key_repr}\n{derived_key_repr}"
    @staticmethod
    def create(p, factor):
        return Public_Key(p, factor)
public_key = Public_Key(23, 5)
print(public_key)
another_public_key = Public_Key.create(47, 9)
print(another_public_key)
