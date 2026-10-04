from curve import Curve
from point import Point
class PublicKey:
    def __init__(self, p, k):
        self.p = p
        self.curve = Curve.make_curve(p)
        self.P = self.curve.random_point()
        self.Q = self.curve.multiply(k, self.P)
    def __repr__(self):
        return f"Curve: {self.curve}\nP: {self.P}\nQ: {self.Q}"
    @staticmethod
    def make_public_key(p, k):
        return PublicKey(p, k)
if __name__ == "__main__":
    p = 23
    k = 5
    public_key = PublicKey.make_public_key(p, k)
    print(public_key)