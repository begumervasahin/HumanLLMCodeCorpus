import os
import random
from numpy import gcd
from library.Sieve_of_Eratosthenes import gen_primes
prime_array = []
def prime_limit(interval):
    for prime in gen_primes():
        if prime < interval:
            prime_array.append(prime)
        else:
            break
def select_distinct_primes(primes):
    while True:
        p = random.choice(primes)
        q = random.choice(primes)
        if p != q:
            return p, q
def calculate_n(p, q):
    return p * q
def calculate_phi(p, q):
    return (p - 1) * (q - 1)
def generate_public_exponent(phi_n):
    while True:
        e = random.randint(2, phi_n - 1)
        if gcd(phi_n, e) == 1:
            return e
def calculate_private_exponent(e, phi):
    def extended_gcd(a, b):
        if a == 0:
            return b, 0, 1
        g, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b
        y = x1
        return g, x, y
    g, x, _ = extended_gcd(e, phi)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    return x % phi
def generate_rsa_keypair(prime_interval):
    prime_limit(prime_interval)
    p, q = select_distinct_primes(prime_array)
    n = calculate_n(p, q)
    phi_n = calculate_phi(p, q)
    e = generate_public_exponent(phi_n)
    d = calculate_private_exponent(e, phi_n)
    return (n, e), (n, d)
prime_interval = int(input("Generate primes below: "))
public_key, private_key = generate_rsa_keypair(prime_interval)
print(f"Public Key: {public_key}")
print(f"Private Key: {private_key}")