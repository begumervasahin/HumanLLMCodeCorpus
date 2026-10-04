import basicfunc
class ElGamal:
    def __init__(self, ec, g):
        assert ec.is_valid(g), "Generator point is not valid on the given elliptic curve."
        self.ec = ec
        self.g = g
        self.n = ec.order(g)
    def generate_public_key(self, private_key):
        return self.ec.mul(self.g, private_key)
    def encrypt(self, plaintext, public_key, random_int):
        assert self.ec.is_valid(plaintext), "Plaintext point is not valid on the elliptic curve."
        assert self.ec.is_valid(public_key), "Public key is not valid on the elliptic curve."
        c1 = self.ec.mul(self.g, random_int)
        c2 = self.ec.add(plaintext, self.ec.mul(public_key, random_int))
        return c1, c2
    def decrypt(self, ciphertext, private_key):
        c1, c2 = ciphertext
        assert self.ec.is_valid(c1), "Ciphertext point c1 is not valid on the elliptic curve."
        assert self.ec.is_valid(c2), "Ciphertext point c2 is not valid on the elliptic curve."
        return self.ec.add(c2, self.ec.neg(self.ec.mul(c1, private_key)))
if __name__ == "__main__":
    ec = basicfunc.EllipticCurve()
    g = ec.get_generator_point()
    elgamal = ElGamal(ec, g)
    alice_private_key = 123456789
    bob_private_key = 987654321
    alice_public_key = elgamal.generate_public_key(alice_private_key)
    bob_public_key = elgamal.generate_public_key(bob_private_key)
    plaintext_message = ec.get_random_point()
    random_integer = 135792468
    ciphertext = elgamal.encrypt(plaintext_message, bob_public_key, random_integer)
    decrypted_message = elgamal.decrypt(ciphertext, bob_private_key)
    print(f"Original message: {plaintext_message}")
    print(f"Encrypted message: {ciphertext}")
    print(f"Decrypted message: {decrypted_message}")