from curve import Curve
from point import Point
class Public_Key:
    curve = None
    p = 0
    P = None
    Q = None
    def __init__(self, p, k):
        self.p = p
        self.curve = Curve.make_curve(self.p)
        self.P = self.curve.random_point()
        self.Q = self.curve.multiply(k, self.P)
    def __repr__(self):
        return f"Curve: {self.curve}\nPublic Key (P): {self.P}\nDerived Public Key (Q): {self.Q}"
    @staticmethod
    def make_public_key(p, k):
        return Public_Key(p, k)
public_key = Public_Key(23, 5)
print(public_key)
another_public_key = Public_Key.make_public_key(47, 9)
print(another_public_key)
