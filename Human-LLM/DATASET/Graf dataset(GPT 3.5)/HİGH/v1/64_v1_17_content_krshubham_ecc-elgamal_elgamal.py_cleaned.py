from basicfunc import EllipticCurve
class class1:
    def fonk1(self, b1, b2):
        assert b1.is_valid(b2)
        self.b1 = b1
        self.b2 = b2
        self.b3 = b1.order(b2)
    def fonk2(self, priv, b2):
        return self.b1.mul(b2, priv)
    def fonk3(self, plain, pub, b2, b10):
        assert self.b1.is_valid(plain)
        assert self.b1.is_valid(pub)
        return (self.b1.mul(b2, b10), self.b1.add(plain, self.b1.mul(pub, b10)))
    def fonk4(self, cipher, priv):
        c1, b4 = cipher
        assert self.b1.is_valid(c1) and self.b1.is_valid(b4)
        return self.b1.add(b4, self.b1.neg(self.b1.mul(c1, priv)))
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