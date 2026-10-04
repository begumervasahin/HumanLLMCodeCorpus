import math
import random
class RSA:
    def __init__(self, p, q):
        self.p = p
        self.q = q
        if not self.is_prime(self.p):
            raise ValueError("p is not a prime number")
        if not self.is_prime(self.q):
            raise ValueError("q is not a prime number")
        self.n = self.p * self.q
        self.phi = (self.p - 1) * (self.q - 1)
        self.e = self.generate_e(self.phi)
        self.d = self.extended_euclid(self.e, self.phi)
    def is_prime(self, n):
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    def generate_e(self, phi):
        e = random.randint(2, phi - 1)
        while math.gcd(e, phi) != 1:
            e = random.randint(2, phi - 1)
        return e
    def extended_euclid(self, a, b):
        x1, x2, x3 = 1, 0, a
        y1, y2, y3 = 0, 1, b
        while y3 != 0:
            q = x3
            t1, t2, t3 = x1 - q * y1, x2 - q * y2, x3 - q * y3
            x1, x2, x3 = y1, y2, y3
            y1, y2, y3 = t1, t2, t3
        return x1 % b if x1 % b > 0 else x1 % b + b
    def encrypt(self, plaintext):
        return pow(plaintext, self.e, self.n)
    def decrypt(self, ciphertext):
        return pow(ciphertext, self.d, self.n)
if __name__ == '__main__':
    rsa = RSA(557, 601)
    print("Public Key: (n={}, e={})".format(rsa.n, rsa.e))
    print("Private Key: d={}".format(rsa.d))
    plaintext = 30091
    ciphertext = rsa.encrypt(plaintext)
    print("Encrypted:", ciphertext)
    decrypted_text = rsa.decrypt(ciphertext)
    print("Decrypted:", decrypted_text)