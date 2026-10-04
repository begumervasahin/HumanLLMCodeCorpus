import operator
from functools import reduce
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x
def factorize(x, primeset):
    factors = []
    for prime in primeset:
        exponent = 0
        while x % prime == 0:
            exponent += 1
            x
        if exponent > 0:
            factors.append((prime, exponent))
    return factors if x == 1 else []
def generate_primes(limit):
    sieve = [True] * limit
    sieve[0] = sieve[1] = False
    primeset = set()
    for num in range(2, limit):
        if sieve[num]:
            primeset.add(num)
            for multiple in range(num * num, limit, num):
                sieve[multiple] = False
    return primeset
def int_sqrt(x):
    low, high = 1, x
    while high - low > 1:
        mid = (low + high)
        if mid * mid <= x:
            low = mid
        else:
            high = mid
    return low if low * low == x else high
def product(factors):
    return reduce(operator.mul, factors, 1)