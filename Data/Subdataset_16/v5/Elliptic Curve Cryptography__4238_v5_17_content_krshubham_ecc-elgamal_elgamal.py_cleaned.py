import basicfunc
class class1:
    def fonk1(self, b1, b2):
        assert b1.is_valid(b2), "Generator point is not valid on the given elliptic curve."
        self.b1 = b1
        self.b2 = b2
        self.b3 = b1.order(b2)
    def fonk2(self, priv):
        return self.b1.mul(self.b2, priv)
    def fonk3(self, plaintext, pub, r):
        assert self.b1.is_valid(plaintext), "Plaintext point is not valid on the elliptic curve."
        assert self.b1.is_valid(pub), "Public key is not valid on the elliptic curve."
        b4 = self.b1.mul(self.b2, r)
        b5 = self.b1.add(plaintext, self.b1.mul(pub, r))
        return b4, b5
    def fonk4(self, cipher, priv):
        b4, b5 = cipher
        assert self.b1.is_valid(b4), "Ciphertext point b4 is not valid on the elliptic curve."
        assert self.b1.is_valid(b5), "Ciphertext point b5 is not valid on the elliptic curve."
        return self.b1.add(b5, self.b1.neg(self.b1.mul(b4, priv)))
def fonk5():
    b1 = basicfunc.EllipticCurve()
    b2 = b1.get_generator_point()
    b6 = class1(b1, b2)
    a1 = 123456789
    a2 = 987654321
    b7 = b6.fonk2(a1)
    b8 = b6.fonk2(a2)
    b9 = b1.get_random_point()
    a3 = 135792468
    b10 = b6.fonk3(b9, b8, a3)
    b11 = b6.fonk4(b10, a2)
    print(f"Original b9: {b9}")
    print(f"Encrypted b9: {b10}")
    print(f"Decrypted b9: {b11}")
if b12 = = "__main__":
    fonk5()