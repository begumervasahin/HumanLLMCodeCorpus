from basicfunc import EllipticCurve
from typing import Tuple
class class1:
    def fonk1(self, b1: EllipticCurve, b2: Tuple[int, int]):
        assert b1.is_valid(b2)
        self.b1 = b1
        self.b2 = b2
        self.b3 = b1.b3(b2)
    def fonk2(self, private_key: int) -> Tuple[int, int]:
        return self.b1.multiply(self.b2, private_key)
    def fonk3(self, plaintext: Tuple[int, int], public_key: Tuple[int, int], random_factor: int) -> Tuple[Tuple[int, int], Tuple[int, int]]:
        assert self.b1.is_valid(plaintext)
        assert self.b1.is_valid(public_key)
        return (
            self.b1.multiply(self.b2, random_factor),
            self.b1.add(
                plaintext, self.b1.multiply(public_key, random_factor)
            ),
        )
    def fonk4(self, ciphertext: Tuple[Tuple[int, int], Tuple[int, int]], private_key: int) -> Tuple[int, int]:
        c1, b4 = ciphertext
        assert self.b1.is_valid(c1) and self.b1.is_valid(b4)
        return self.b1.add(
            b4, self.b1.negate(self.b1.multiply(c1, private_key))
        )