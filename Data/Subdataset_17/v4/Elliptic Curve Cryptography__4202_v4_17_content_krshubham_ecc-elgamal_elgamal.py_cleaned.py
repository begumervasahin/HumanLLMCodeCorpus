import basicfunc
class ElGamal:
    def __init__(self, ec, g):
        assert ec.is_valid(g), "Generator point is not valid on the given elliptic curve."
        self.ec = ec
        self.g = g
        self.n = ec.order(g)
    def generate_public_key(self, priv):
        return self.ec.mul(self.g, priv)
    def encrypt(self, plaintext, pub, r):
        assert self.ec.is_valid(plaintext), "Plaintext point is not valid on the elliptic curve."
        assert self.ec.is_valid(pub), "Public key is not valid on the elliptic curve."
        c1 = self.ec.mul(self.g, r)
        c2 = self.ec.add(plaintext, self.ec.mul(pub, r))
        return c1, c2
    def decrypt(self, cipher, priv):
        c1, c2 = cipher
        assert self.ec.is_valid(c1), "Ciphertext point c1 is not valid on the elliptic curve."
        assert self.ec.is_valid(c2), "Ciphertext point c2 is not valid on the elliptic curve."
        return self.ec.add(c2, self.ec.neg(self.ec.mul(c1, priv)))
if __name__ == "__main__":
    ec = basicfunc.EllipticCurve()
    g = ec.get_generator_point()
    elgamal = ElGamal(ec, g)
    alice_priv = 123456789
    bob_priv = 987654321
    alice_pub = elgamal.generate_public_key(alice_priv)
    bob_pub = elgamal.generate_public_key(bob_priv)
    message = ec.get_random_point()
    random_int = 135792468
    ciphertext = elgamal.encrypt(message, bob_pub, random_int)
    decrypted_message = elgamal.decrypt(ciphertext, bob_priv)
    print(f"Original message: {message}")
    print(f"Encrypted message: {ciphertext}")
    print(f"Decrypted message: {decrypted_message}")