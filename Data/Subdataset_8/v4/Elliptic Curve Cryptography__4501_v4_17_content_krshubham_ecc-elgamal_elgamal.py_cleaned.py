from basicfunc import EllipticCurve
class ElGamal:
    def __init__(self, elliptic_curve, generator):
        assert elliptic_curve.is_valid(generator)
        self.elliptic_curve = elliptic_curve
        self.generator = generator
        self.order = elliptic_curve.order(generator)
    def generate_public_key(self, private_key, generator):
        return self.elliptic_curve.multiply(generator, private_key)
    def encrypt(self, plaintext, public_key, generator, random_factor):
        assert self.elliptic_curve.is_valid(plaintext)
        assert self.elliptic_curve.is_valid(public_key)
        return (
            self.elliptic_curve.multiply(generator, random_factor),
            self.elliptic_curve.add(
                plaintext, self.elliptic_curve.multiply(public_key, random_factor)
            ),
        )
    def decrypt(self, ciphertext, private_key, elliptic_curve):
        c1, c2 = ciphertext
        assert self.elliptic_curve.is_valid(c1) and elliptic_curve.is_valid(c2)
        return self.elliptic_curve.add(
            c2, self.elliptic_curve.negate(self.elliptic_curve.multiply(c1, private_key))
        )