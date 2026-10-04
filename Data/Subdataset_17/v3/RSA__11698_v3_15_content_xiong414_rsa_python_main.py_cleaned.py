import math
import random
class RSA:
    def __init__(self, p, q):
        self.p = p
        self.q = q
        self._validate_primes()
        self.n = self.p * self.q
        self.phi = (self.p - 1) * (self.q - 1)
        self.e = self._generate_e(self.phi)
        self.d = self._compute_modular_inverse(self.e, self.phi)
    def _validate_primes(self):
        if not self._is_prime(self.p):
            raise ValueError("p is not a prime number")
        if not self._is_prime(self.q):
            raise ValueError("q is not a prime number")
    def _is_prime(self, n):
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    def _generate_e(self, phi):
        while True:
            e = random.randint(2, phi - 1)
            if math.gcd(e, phi) == 1:
                return e
    def _compute_modular_inverse(self, a, b):
        x1, x2, x3 = 1, 0, a
        y1, y2, y3 = 0, 1, b
        while y3 != 0:
            q = x3
            x1, x2, x3, y1, y2, y3 = y1, y2, y3, x1 - q * y1, x2 - q * y2, x3 - q * y3
        return x1 % b if x1 > 0 else x1 % b + b
    def encrypt(self, plaintext):
        return pow(plaintext, self.e, self.n)
    def decrypt(self, ciphertext):
        return pow(ciphertext, self.d, self.n)
if __name__ == '__main__':
    rsa = RSA(557, 601)
    print(f"Public Key: (n={rsa.n}, e={rsa.e})")
    print(f"Private Key: d={rsa.d}")
    plaintext = 30091
    ciphertext = rsa.encrypt(plaintext)
    print(f"Encrypted: {ciphertext}")
    decrypted_text = rsa.decrypt(ciphertext)
    print(f"Decrypted: {decrypted_text}")