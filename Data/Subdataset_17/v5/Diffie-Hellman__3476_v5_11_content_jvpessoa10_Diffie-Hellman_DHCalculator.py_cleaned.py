from math import sqrt
from itertools import count, islice
import random
class DHCalculator:
    def __init__(self):
        self.private_key = None
    def is_prime(self, n):
        return n > 1 and all(n % i != 0 for i in islice(count(2), int(sqrt(n) - 1)))
    def generate_prime(self, min_value=1000, max_value=10000):
        primes = [i for i in range(min_value, max_value) if self.is_prime(i)]
        return random.choice(primes)
    def set_private_key(self, private_key):
        self.private_key = private_key
    def calculate_public_value(self, base, prime):
        if self.private_key is None:
            raise ValueError("Private key is not set.")
        return pow(base, self.private_key, prime)
    def calculate_shared_secret(self, public_value, prime):
        if self.private_key is None:
            raise ValueError("Private key is not set.")
        return pow(public_value, self.private_key, prime)
def main():
    dh_calculator = DHCalculator()
    prime = dh_calculator.generate_prime()
    base = random.randint(2, prime - 1)
    print(f"Generated prime P: {prime} and base G: {base}")
    private_key = random.randint(1, prime - 1)
    dh_calculator.set_private_key(private_key)
    print(f"Private key a: {private_key}")
    public_value_A = dh_calculator.calculate_public_value(base, prime)
    print(f"Public value A: {public_value_A}")
    public_value_B = random.randint(2, prime - 1)
    print(f"Received public value B: {public_value_B}")
    shared_secret = dh_calculator.calculate_shared_secret(public_value_B, prime)
    print(f"The shared secret key is: {shared_secret}")
if __name__ == "__main__":
    main()