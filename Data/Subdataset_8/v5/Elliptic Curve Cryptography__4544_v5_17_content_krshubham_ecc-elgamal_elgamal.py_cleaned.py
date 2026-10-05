from basicfunc import EllipticCurve
from typing import Tuple
class ElGamal:
    def __init__(self, elliptic_curve: EllipticCurve, generator: Tuple[int, int]):
        assert elliptic_curve.is_valid(generator)
        self.elliptic_curve = elliptic_curve
        self.generator = generator
        self.order = elliptic_curve.order(generator)
    def generate_public_key(self, private_key: int) -> Tuple[int, int]:
        return self.elliptic_curve.multiply(self.generator, private_key)
    def encrypt(self, plaintext: Tuple[int, int], public_key: Tuple[int, int], random_factor: int) -> Tuple[Tuple[int, int], Tuple[int, int]]:
        assert self.elliptic_curve.is_valid(plaintext)
        assert self.elliptic_curve.is_valid(public_key)
        return (
            self.elliptic_curve.multiply(self.generator, random_factor),
            self.elliptic_curve.add(
                plaintext, self.elliptic_curve.multiply(public_key, random_factor)
            ),
        )
    def decrypt(self, ciphertext: Tuple[Tuple[int, int], Tuple[int, int]], private_key: int) -> Tuple[int, int]:
        c1, c2 = ciphertext
        assert self.elliptic_curve.is_valid(c1) and self.elliptic_curve.is_valid(c2)
        return self.elliptic_curve.add(
            c2, self.elliptic_curve.negate(self.elliptic_curve.multiply(c1, private_key))
        )