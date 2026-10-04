import random
import secrets
import math
class RSA:
    def __init__(self):
        self.P, self.Q = self.find_2primes()
        self.N = self.P * self.Q
        self.L = (self.P - 1) * (self.Q - 1)
        self.E = self.generate_public_key()
        self.D = self.generate_private_key()
    def is_prime(self, n):
        if n == 2:
            return True
        if n == 1 or n % 2 == 0:
            return False
        d = (n - 1)
        while d % 2 == 0:
            d
        for _ in range(100):
            a = random.randint(1, n - 1)
            t = d
            y = pow(a, t, n)
            while t != n - 1 and y != 1 and y != n - 1:
                y = (y * y) % n
                t *= 2
            if y != n - 1 and t % 2 == 0:
                return False
        return True
    def find_2primes(self):
        primes = []
        while len(primes) < 2:
            candidate = secrets.randbits(10)
            if self.is_prime(candidate):
                primes.append(candidate)
        return primes
    def generate_public_key(self):
        e = random.randint(1, self.L)
        while math.gcd(e, self.L) != 1:
            e = random.randint(1, self.L)
        return e
    def generate_private_key(self):
        d = random.randint(1, self.L)
        while (self.E * d) % self.L != 1:
            d = random.randint(1, self.L)
        return d
    def public_key(self):
        return self.E, self.N
    def private_key(self):
        return self.D, self.N
def encrypt_text(e, n, text):
    text_int = [ord(char) for char in text]
    encrypted_int = [str(pow(char, e, n)) for char in text_int]
    return " ".join(encrypted_int)
def decrypt_text(d, n, encrypted_text):
    encrypted_int = [int(char) for char in encrypted_text.split()]
    decrypted_int = [pow(char, d, n) for char in encrypted_int]
    return "".join(chr(char) for char in decrypted_int)
if __name__ == "__main__":
    rsa = RSA()
    e, n = rsa.public_key()
    d, n = rsa.private_key()
    text = input("Enter text to encrypt: ")
    encrypted_text = encrypt_text(e, n, text)
    print("Encrypted text:", encrypted_text)
    decrypted_text = decrypt_text(d, n, encrypted_text)
    print("Decrypted text:", decrypted_text)
    print("-----------------------------------------------------")
    print(f"d: {d}, n: {n}")