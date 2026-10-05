from basicfunc import EllipticCurve
class ElGamal:
    def __init__(self, ec, g):
        assert ec.is_valid(g)
        self.ec = ec
        self.g = g
        self.n = ec.order(g)
    def gen(self, priv, g):
        return self.ec.mul(g, priv)
    def enc(self, plain, pub, g, r):
        assert self.ec.is_valid(plain)
        assert self.ec.is_valid(pub)
        return (self.ec.mul(g, r), self.ec.add(plain, self.ec.mul(pub, r)))
    def dec(self, cipher, priv):
        c1, c2 = cipher
        assert self.ec.is_valid(c1) and self.ec.is_valid(c2)
        return self.ec.add(c2, self.ec.neg(self.ec.mul(c1, priv)))
if __name__ == "__main__":
    ec = EllipticCurve(...)
    g = ...
    elgamal = ElGamal(ec, g)
    priv_key = ...
    pub_key = elgamal.gen(priv_key, g)
    plain_text = ...
    r = ...
    cipher_text = elgamal.enc(plain_text, pub_key, g, r)
    decrypted_text = elgamal.dec(cipher_text, priv_key)