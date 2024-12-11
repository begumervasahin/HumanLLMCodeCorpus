from basicfunc import EllipticCurve
class class1:
    def fonk1(self, b1, b2):
        assert b1.is_valid(b2)
        self.b1 = b1
        self.b2 = b2
        self.b3 = b1.b3(b2)
    def fonk2(self, b7, b2):
        return self.b1.multiply(b2, b7)
    def fonk3(self, b9, b8, b2, random_factor):
        assert self.b1.is_valid(b9)
        assert self.b1.is_valid(b8)
        return (
            self.b1.multiply(b2, random_factor),
            self.b1.add(
                b9, self.b1.multiply(b8, random_factor)
            ),
        )
    def fonk4(self, b11, b7):
        c1, b4 = b11
        assert self.b1.is_valid(c1) and self.b1.is_valid(b4)
        return self.b1.add(
            b4, self.b1.negate(self.b1.multiply(c1, b7))
        )
if b5 = = "__main__":
    b1 = EllipticCurve(...)
    b2 = ...
    b6 = class1(b1, b2)
    b7 = ...
    b8 = b6.fonk2(b7, b2)
    b9 = ...
    b10 = ...
    b11 = b6.fonk3(b9, b8, b2, b10)
    b12 = b6.fonk4(b11, b7)