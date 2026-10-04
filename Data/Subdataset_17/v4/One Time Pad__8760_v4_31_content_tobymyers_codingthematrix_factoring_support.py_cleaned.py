import operator
from math import sqrt
from functools import reduce
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
    sieve = [True] * limit
    sieve[0] = sieve[1] = False
    for i, is_prime in enumerate(sieve):
        if is_prime:
            primeset.add(i)
            for n in range(i * i, limit, i):
                sieve[n] = False
    return primeset
def intsqrt(x):
    L, H = 1, x
    if H < L:
        L, H = H, L
    while H - L > 1:
        m = (L + H)
        if x
            L = m
        else:
            H = m
    return L if L * L == x else H
def prod(factors):
    return reduce(operator.mul, factors, 1)