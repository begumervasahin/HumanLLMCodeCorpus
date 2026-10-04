from math import sqrt
from functools import reduce
import operator
def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x
def factorize(x, primeset):
    factors = []
    for p in primeset:
        exponent = 0
        while x % p == 0:
            exponent += 1
            x
        if exponent > 0:
            factors.append((p, exponent))
    return factors if x == 1 else []
def generate_primes(limit):
    primeset = set()
    is_prime = [True] * limit
    is_prime[0] = is_prime[1] = False
    for i in range(2, limit):
        if is_prime[i]:
            primeset.add(i)
            for multiple in range(i * i, limit, i):
                is_prime[multiple] = False
    return primeset
def integer_sqrt(x):
    if x == 0:
        return 0
    low, high = 1, x
    while low < high:
        mid = (low + high + 1)
        if mid * mid <= x:
            low = mid
        else:
            high = mid - 1
    return low
def product(factors):
    return reduce(operator.mul, factors, 1)
if __name__ == "__main__":
    primeset = generate_primes(100)
    print(f"Primeset: {primeset}")
    x = 60
    factors = factorize(x, primeset)
    print(f"Factors of {x}: {factors}")
    x, y = 48, 18
    print(f"GCD of {x} and {y}: {gcd(x, y)}")
    x = 49
    print(f"Integer square root of {x}: {integer_sqrt(x)}")
    factors = [2, 3, 5]
    print(f"Product of {factors}: {product(factors)}")