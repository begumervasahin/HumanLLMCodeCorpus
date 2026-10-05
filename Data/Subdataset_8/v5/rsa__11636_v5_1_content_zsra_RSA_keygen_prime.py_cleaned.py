import random
import math
import xgcd
def get_prime(min_val, max_val):
    primes_in_range = [num for num in range(min_val, max_val) if is_prime(num)]
    return random.choice(primes_in_range)
def is_prime(n):
    if not isinstance(n, int) or n < 2:
        return False
    if n in {2, 3, 5, 7}:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    d = n - 1
    s = 0
    while d % 2 == 0:
        d
        s += 1
    def trial_composite(a):
        if pow(a, d, n) == 1:
            return False
        for _ in range(s):
            if pow(a, 2**_ * d, n) == n - 1:
                return False
        return True
    for _ in range(8):
        a = random.randint(2, n - 1)
        if trial_composite(a):
            return False
    return True
def is_coprime(a, b):
    return xgcd.GCD(a, b) == 1