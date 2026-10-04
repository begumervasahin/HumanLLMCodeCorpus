from curve import Curve
from point import Point
class PublicKey:
    def __init__(self, prime, private_key):
        self.prime = prime
        self.curve = Curve.make_curve(prime)
        self.public_point_P = self.curve.random_point()
        self.public_point_Q = self.curve.multiply(private_key, self.public_point_P)
    def __repr__(self):
        return (
            f"Curve:\n{self.curve}\n"
            f"Public Point P: {self.public_point_P}\n"
            f"Public Point Q: {self.public_point_Q}"
        )
    @staticmethod
    def generate(prime, private_key):
        return PublicKey(prime, private_key)
if __name__ == "__main__":
    prime = 23
    private_key = 5
    public_key = PublicKey.generate(prime, private_key)
    print(public_key)