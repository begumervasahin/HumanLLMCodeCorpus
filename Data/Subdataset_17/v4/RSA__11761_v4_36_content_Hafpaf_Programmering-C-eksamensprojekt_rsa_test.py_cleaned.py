import os
import random
from numpy import gcd
from library.Sieve_of_Eratosthenes import gen_primes
prime_array = []
prime_interval = int(input("Generate primes below: "))
def prime_limit(interval):
    for prime in gen_primes():
        if prime < interval:
            prime_array.append(prime)
        else:
            break
def prime_numbers():
    while True:
        p = random.choice(prime_array)
        q = random.choice(prime_array)
        print(f'Random prime_p below {prime_interval} is: {p}')
        print(f'Random prime_q below {prime_interval} is: {q}')
        if p != q:
            print("Primes are not equal: Pass")
            return p, q
        print("Primes must not be equal, generating new primes")
def calculate_n(p, q):
    n = p * q
    print("n:", n)
    return n
def phi(p, q):
    phi_result = (p - 1) * (q - 1)
    print("phi_n:", phi_result)
    return phi_result
def number_e(phi_n):
    while True:
        e = random.randint(2, phi_n - 1)
        if gcd(phi_n, e) == 1:
            print("e:", e)
            return e
def gcd_calculation(phi, e):
    gcd_result = gcd(phi, e)
    print("gcd_calc:", gcd_result)
    if gcd_result == 1:
        print("GCD is 1: True")
        return True
    else:
        print("GCD is not 1: False")
        return False
def number_d(e, phi):
    def egcd(a, b):
        if a == 0:
            return b, 0, 1
        g, x1, y1 = egcd(b % a, a)
        x = y1 - (b
        y = x1
        return g, x, y
    g, x, _ = egcd(e, phi)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        d = x % phi
        print("d:", d)
        return d
prime_limit(prime_interval)
prime_p, prime_q = prime_numbers()
number_n = calculate_n(prime_p, prime_q)
phi_n = phi(prime_p, prime_q)
e = number_e(phi_n)
if not gcd_calculation(phi_n, e):
    exit(1)
d = number_d(e, phi_n)
print(f"Public Key: (n: {number_n}, e: {e})")
print(f"Private Key: (n: {number_n}, d: {d})")