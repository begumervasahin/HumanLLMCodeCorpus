import random
import math
class Key:
    def __init__(self, bit_size):
        self.bit_size = bit_size
    def is_prime(self, n):
        if n in (2, 3):
            return True
        if n % 2 == 0 or n < 2:
            return False
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True
    def generate_random_number(self):
        return random.randint(2 ** (self.bit_size - 1) + 1, 2 ** self.bit_size)
    def generate_prime(self):
        while True:
            num = self.generate_random_number()
            if self.is_prime(num):
                return num
    def is_relatively_prime(self, a, b):
        return math.gcd(a, b) == 1
    def find_relative_prime(self, a):
        for i in range(3, int(math.sqrt(a)) + 1, 2):
            if self.is_relatively_prime(i, a):
                return i
        raise Exception("Failed to find a relatively prime number.")
    def extended_gcd(self, a, b):
        if b == 0:
            return a, 1, 0
        else:
            d, x1, y1 = self.extended_gcd(b, a % b)
            x = y1
            y = x1 - (a
            return d, x, y
    def test_keys(self, public_key, private_key):
        test_value = 2
        e, n = public_key
        d, _ = private_key
        encrypted = pow(test_value, e, n)
        decrypted = pow(encrypted, d, n)
        return test_value == decrypted
    def generate_keys(self):
        while True:
            p = self.generate_prime()
            q = self.generate_prime()
            n = p * q
            euler_totient = (p - 1) * (q - 1)
            e = self.find_relative_prime(euler_totient)
            _, d, _ = self.extended_gcd(e, euler_totient)
            if d < 0:
                d += euler_totient
            public_key = (e, n)
            private_key = (d, n)
            if self.test_keys(public_key, private_key):
                return [public_key, private_key]
