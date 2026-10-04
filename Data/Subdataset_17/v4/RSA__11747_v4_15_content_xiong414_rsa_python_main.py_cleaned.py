import math
import random
class RSA:
    def __init__(self, p, q):
        self.p = p
        self.q = q
        if not self.is_prime(self.p):
            raise ValueError('p is not a prime number')
        if not self.is_prime(self.q):
            raise ValueError('q is not a prime number')
        self._generate_keys()
    def is_prime(self, n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    def _generate_e(self, phi):
        while True:
            e = random.randint(2, phi - 1)
            if math.gcd(e, phi) == 1:
                return e
    def _extended_euclid(self, a, b):
        x1, x2, x3 = 1, 0, a
        y1, y2, y3 = 0, 1, b
        while y3 != 0 and y3 != 1:
            q = x3
            t1, t2, t3 = x1 - q * y1, x2 - q * y2, x3 - q * y3
            x1, x2, x3 = y1, y2, y3
            y1, y2, y3 = t1, t2, t3
        if y3 == 0:
            return None
        return y2 if y2 > 0 else y2 + a
    def _generate_keys(self):
        self.n = self.p * self.q
        phi = (self.p - 1) * (self.q - 1)
        self.e = self._generate_e(phi)
        self.d = self._extended_euclid(phi, self.e)
        self.public_key = (self.n, self.e)
        self.private_key = self.d
    def encrypt(self, plaintext):
        return pow(plaintext, self.e, self.n)
    def decrypt(self, ciphertext):
        return pow(ciphertext, self.d, self.n)
if __name__ == '__main__':
    rsa = RSA(557, 601)
    print(f"Public Key: {rsa.public_key}")
    print(f"Private Key: {rsa.private_key}")
    plaintext = 30091
    ciphertext = rsa.encrypt(plaintext)
    print(f"Encrypted: {ciphertext}")
    decrypted_text = rsa.decrypt(ciphertext)
    print(f"Decrypted: {decrypted_text}")