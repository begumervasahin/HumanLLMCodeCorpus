import numpy as np
def division_algorithm(n, d):
    result = []
    while n >= 1:
        result.append(str(n % d))
        n
    return ''.join(result)
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def sieve_of_eratosthenes(n):
    primes = []
    numbers = list(range(2, n + 1))
    while len(numbers) > 0:
        prime = numbers[0]
        primes.append(prime)
        numbers = [num for num in numbers if num % prime != 0]
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