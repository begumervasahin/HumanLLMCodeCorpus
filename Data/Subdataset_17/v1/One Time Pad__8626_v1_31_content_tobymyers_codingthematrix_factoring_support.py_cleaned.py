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
    a = [True] * limit
    a[0] = a[1] = False
    for i, isprime in enumerate(a):
        if isprime:
            primeset.add(i)
            for n in range(i * i, limit, i):
                a[n] = False
    return primeset
def intsqrt(x):
    L = 1
    H = x
    if H < L:
        L, H = H, L
    while H - L > 1:
        m = (L + H)
        d = x
        if d > m:
            L = m
        else:
            H = m
    return L if L * L == x else H
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