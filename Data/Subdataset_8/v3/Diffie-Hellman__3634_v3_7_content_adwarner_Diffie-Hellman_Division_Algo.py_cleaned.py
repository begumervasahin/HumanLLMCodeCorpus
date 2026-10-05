import numpy as np
def division_algorithm(n, d):
    result = []
    while n >= 1:
        result.append(str(n % d))
        n = n
    return ''.join(result)
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def sieve_of_eratosthenes(n):
    primes = []
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            primes.append(i)
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return primes
def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = extended_gcd(b % a, a)
        return (g, y - (b
def modular_inverse(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m