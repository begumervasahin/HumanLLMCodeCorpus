import random
import math
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
def potencia_modular_eficient(base, expo, p):
    if expo == 0:
        return 1
    elif base == 0:
        return 0
    base_to_exp_div2 = potencia_modular_eficient(base, expo
    base_to_exp_div2 = (base_to_exp_div2 * base_to_exp_div2) % p
    if expo % 2 == 0:
        return base_to_exp_div2
    else:
        return (base_to_exp_div2 * base) % p
def fermat_primalitat(n):
    for b in primes:
        if b >= n:
            break
        if potencia_modular_eficient(b, n - 1, n) != 1:
            return False
    return True
def troba_primer(nbits):
    while True:
        test_number = random.getrandbits(nbits)
        if fermat_primalitat(test_number):
            return test_number
def mcd_euclides(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def bezout(a, b):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0
def invers_modular(k, n):
    gcd, x, _ = bezout(k, n)
    if gcd != 1:
        return False, k
    else:
        return True, x % n
def factors_primers(n):
    factors = []
    if n >= 2:
        d = 2
        while d * d <= n:
            while (n % d) == 0:
                factors.append(d)
                n
            d += 1
        if n > 1:
            factors.append(n)
    return factors