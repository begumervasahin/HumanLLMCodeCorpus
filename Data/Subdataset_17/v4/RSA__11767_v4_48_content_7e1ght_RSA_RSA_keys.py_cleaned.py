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
        return random.randint(2**(self.bit_size - 1) + 1, 2**self.bit_size)
    def generate_prime(self):
        num = self.generate_random_number()
        while not self.is_prime(num):
            num = self.generate_random_number()
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
    def test_keys(self, keys):
        test_value = 2
        public_key, private_key = keys
        encrypted = pow(test_value, public_key[0], public_key[1])
        decrypted = pow(encrypted, private_key[0], private_key[1])
        return test_value == decrypted
    def generate_keys(self):
        test_passed = False
        while not test_passed:
            p = self.generate_prime()
            q = self.generate_prime()
            n = p * q
            euler_totient = (p - 1) * (q - 1)
            e = self.find_relative_prime(euler_totient)
            _, d, _ = self.extended_gcd(e, euler_totient)
            if d < 0:
                d += euler_totient
            test_passed = self.test_keys([[e, n], [d, n]])
        return [[e, n], [d, n]]