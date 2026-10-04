from math import sqrt
from functools import reduce
import operator
def gcd(x, y):
    return x if y == 0 else gcd(y, x % y)
def dumb_factor(x, primeset):
    factors = []
    for p in primeset:
        exponent = 0
        while x % p == 0:
            exponent += 1
            x
        if exponent > 0:
            factors.append((p, exponent))
    return factors if x == 1 else []
def primes(limit):
    primeset = set()
    is_prime = [True] * limit
    is_prime[0] = is_prime[1] = False
    for i, prime in enumerate(is_prime):
        if prime:
            primeset.add(i)
            for multiple in range(i * i, limit, i):
                is_prime[multiple] = False
    return primeset
def intsqrt(x):
    low, high = 1, x
    while high - low > 1:
        mid = (low + high)
        if mid * mid <= x:
            low = mid
        else:
            high = mid
    return low
def prod(factors):
    return reduce(operator.mul, factors, 1)
if __name__ == "__main__":
    primeset = primes(100)
    print(f"Primeset: {primeset}")
    x = 60
    factors = dumb_factor(x, primeset)
    print(f"Factors of {x}: {factors}")
    x, y = 48, 18
    print(f"GCD of {x} and {y}: {gcd(x, y)}")
    x = 49
    print(f"Integer square root of {x}: {intsqrt(x)}")
    factors = [2, 3, 5]
    print(f"Product of {factors}: {prod(factors)}")