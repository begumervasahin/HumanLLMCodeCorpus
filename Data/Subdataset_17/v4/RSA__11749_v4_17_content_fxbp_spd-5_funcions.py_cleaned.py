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
        q = dividend
        dividend, divisor = divisor, dividend % divisor
        r.append(q * r[-1] + r[-2])
        s.append(q * s[-1] + s[-2])
    s_res = s[-1]
    r_res = r[-1]
    if len(r) % 2 == 0:
        s_res *= -1
    else:
        r_res *= -1
    return dividend, r_res, s_res
def invers_modular(k, n):
    mcd, r, s = bezoud(k, n)
    if mcd != 1:
        return False, k
    else:
        return True, r % n
def factors_primers(nombre):
    llista_fp = []
    if nombre >= 2:
        d = 2
        while d <= math.sqrt(nombre):
            if nombre % d == 0:
                llista_fp.append(d)
                nombre
            else:
                d += 1
        llista_fp.append(int(nombre))
    return llista_fp