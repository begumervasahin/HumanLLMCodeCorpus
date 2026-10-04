import random
import math
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
def potencia_modular_eficient(base, expo, p):
    if expo == 0:
        return 1
    elif base == 0:
        return 0
    else:
        base_to_exp_div2 = potencia_modular_eficient(base, expo
        if expo % 2 == 0:
            return (base_to_exp_div2 * base_to_exp_div2) % p
        else:
            return (base_to_exp_div2 * base_to_exp_div2 * base) % p
def fermat_primalitat(n):
    for b in primes:
        if b >= n:
            break
        if potencia_modular_eficient(b, n - 1, n) != 1:
            return False
    return True
def troba_primer(nbits):
    test_number = random.getrandbits(nbits)
    while not fermat_primalitat(test_number):
        test_number += 1
    return test_number
def mcd_euclides(dividend, divisor):
    while divisor != 0:
        dividend, divisor = divisor, dividend % divisor
    return dividend
def bezoud(dividend, divisor):
    r, s = [1, 0], [0, 1]
    while divisor != 0:
        quotient = dividend
        dividend, divisor = divisor, dividend % divisor
        r.append(quotient * r[-1] + r[-2])
        s.append(quotient * s[-1] + s[-2])
    sRes, rRes = s[-2], r[-2]
    if (len(s) - 2) % 2 == 0:
        sRes = -sRes
    else:
        rRes = -rRes
    return dividend, rRes, sRes
def invers_modular(k, n):
    gcd, x, y = bezoud(k, n)
    if gcd != 1:
        return False, k
    else:
        return True, x % n
def factors_primers(nombre):
    llista_fp = []
    if nombre >= 2:
        d = 2
        while d * d <= nombre:
            while (nombre % d) == 0:
                llista_fp.append(d)
                nombre
            d += 1
        if nombre > 1:
            llista_fp.append(nombre)
    return llista_fp
if __name__ == "__main__":
    print("Potencia modular eficient:", potencia_modular_eficient(2, 10, 1000))
    print("Fermat primalitat (17):", fermat_primalitat(17))
    print("Troba primer (10 bits):", troba_primer(10))
    print("MCD Euclides (48, 18):", mcd_euclides(48, 18))
    print("Bezoud (48, 18):", bezoud(48, 18))
    print("Invers modular (3, 11):", invers_modular(3, 11))
    print("Factors primers (100):", factors_primers(100))