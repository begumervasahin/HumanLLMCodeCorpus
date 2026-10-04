import os
import random
from numpy import gcd
from library.Sieve_of_Eratosthenes import gen_primes
prime_array = []
prime_interval = int(input("Generate primes below: "))
def prime_limit(interval):
    for i in gen_primes():
        if i < interval:
            prime_array.append(i)
        else:
            break
def prime_numbers():
    while True:
        p = random.choice(prime_array)
        q = random.choice(prime_array)
        print(f'Random prime_p below {prime_interval} is: {p}')
        print(f'Random prime_q below {prime_interval} is: {q}')
        if p != q:
            print("Primes not equal: Pass")
            return (p, q)
        print("Primes must not be equal, generating new primes")
def calculate_n(p, q):
    n = p * q
    print("n: ", n)
    return n
def phi(p, q):
    phi_result = (p - 1) * (q - 1)
    print("phi_n: ", phi_result)
    return phi_result
def number_e(phi_n):
    while True:
        e = random.randint(2, phi_n - 1)
        if gcd(phi_n, e) == 1:
            print("e: ", e)
            return e
def gcd_calculation(phi, e):
    gcd_calc = gcd(phi, e)
    print("gcd_calc: ", gcd_calc)
    return gcd_calc
def mod_inverse(e, phi_n):
    d = pow(e, -1, phi_n)
    print("d: ", d)
    return d
prime_limit(prime_interval)
(prime_p, prime_q) = prime_numbers()
number_n = calculate_n(prime_p, prime_q)
phi_n = phi(prime_p, prime_q)
number_e_value = number_e(phi_n)
gcd = gcd_calculation(phi_n, number_e_value)
number_d = mod_inverse(number_e_value, phi_n)
print("Public key (e, n):", (number_e_value, number_n))
print("Private key (d, n):", (number_d, number_n))