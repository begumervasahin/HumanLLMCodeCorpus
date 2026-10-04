import random
import math
PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
def potencia_modular_eficient(base, expo, mod):
    if expo == 0:
        return 1
    if base == 0:
        return 0
    half_power = potencia_modular_eficient(base, expo
    half_power_squared = (half_power * half_power) % mod
    if expo % 2 == 0:
        return half_power_squared
    else:
        return (half_power_squared * base) % mod
def fermat_primalitat(n):
    for prime in PRIMES:
        if prime >= n:
            break
        if potencia_modular_eficient(prime, n - 1, n) != 1:
            return False
    return True
def troba_primer(nbits):
    candidate = random.getrandbits(nbits)
    while not fermat_primalitat(candidate):
        candidate += 1
    return candidate
def mcd_euclides(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def bezout(a, b):
    r, s = [1, 0], [0, 1]
    while b != 0:
        quotient = a
        a, b = b, a % b
        r.append(r[-2] - quotient * r[-1])
        s.append(s[-2] - quotient * s[-1])
    gcd, x, y = a, r[-2], s[-2]
    return gcd, x, y
def invers_modular(k, n):
    gcd, x, _ = bezout(k, n)
    if gcd != 1:
        return False, k
    return True, x % n
def factors_primers(n):
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n
        d += 1
    if n > 1:
        factors.append(n)
    return factors
if __name__ == "__main__":
    print("Potencia modular eficient:", potencia_modular_eficient(2, 10, 1000))
    print("Fermat primalitat (17):", fermat_primalitat(17))
    print("Troba primer (10 bits):", troba_primer(10))
    print("MCD Euclides (48, 18):", mcd_euclides(48, 18))
    print("Bezout (48, 18):", bezout(48, 18))
    print("Invers modular (3, 11):", invers_modular(3, 11))
    print("Factors primers (100):", factors_primers(100))