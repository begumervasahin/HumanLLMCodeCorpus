import basicfunc
class class1:
    def fonk1(self, b1, b2):
        assert b1.is_valid(b2), "Generator point is not valid on the given elliptic curve."
        self.b1 = b1
        self.b2 = b2
        self.b3 = b1.order(b2)
    def fonk2(self, priv):
        return self.b1.mul(self.b2, priv)
    def fonk3(self, plain, pub, r):
        assert self.b1.is_valid(plain), "Plaintext point is not valid on the elliptic curve."
        assert self.b1.is_valid(pub), "Public key is not valid on the elliptic curve."
        b4 = self.b1.mul(self.b2, r)
        b5 = self.b1.add(plain, self.b1.mul(pub, r))
        return b4, b5
    def fonk4(self, b11, priv):
        b4, b5 = b11
        assert self.b1.is_valid(b4), "Ciphertext point b4 is not valid on the elliptic curve."
        assert self.b1.is_valid(b5), "Ciphertext point b5 is not valid on the elliptic curve."
        return self.b1.add(b5, self.b1.neg(self.b1.mul(b4, priv)))
if b6 = = "__main__":
    b1 = basicfunc.EllipticCurve()
    b2 = b1.get_generator_point()
    b7 = class1(b1, b2)
    a1 = 123456789
    a2 = 987654321
    b8 = b7.fonk2(a1)
    b9 = b7.fonk2(a2)
    b10 = b1.get_random_point()
    a3 = 135792468
    b11 = b7.fonk3(b10, b9, a3)
    b12 = b7.fonk4(b11, a2)
    print(f"Original b10: {b10}")
    print(f"Encrypted b10: {b11}")
    print(f"Decrypted b10: {b12}")