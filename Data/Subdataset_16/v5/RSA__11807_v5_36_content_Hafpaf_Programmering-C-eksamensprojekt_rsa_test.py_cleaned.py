import os
import random
from numpy import gcd
from library.Sieve_of_Eratosthenes import gen_primes
b1 = []
def fonk1(interval):
    for prime in gen_primes():
        if prime < interval:
            b1.append(prime)
        else:
            break
def fonk2(primes):
    while True:
        b2 = random.choice(primes)
        b3 = random.choice(primes)
        if b2 != b3:
            return b2, b3
def fonk3(b2, b3):
    return b2 * b3
def fonk4(b2, b3):
    return (b2 - 1) * (b3 - 1)
def fonk5(b11):
    while True:
        b4 = random.randint(2, b11 - 1)
        if gcd(b11, b4) == 1:
            return b4
def fonk6(b4, phi):
    def fonk7(b5, b):
        if b5 = = 0:
            return b, 0, 1
        g, x1, b6 = fonk7(b % b5, b5)
        b7 = b6 - (b
        b8 = x1
        return g, b7, b8
    g, b7, b9 = fonk7(b4, phi)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    return b7 % phi
def fonk8(b13):
    fonk1(b13)
    b2, b3 = fonk2(b1)
    b10 = fonk3(b2, b3)
    b11 = fonk4(b2, b3)
    b4 = fonk5(b11)
    b12 = fonk6(b4, b11)
    return (b10, b4), (b10, b12)
b13 = int(input("Generate primes below: "))
public_key, b14 = fonk8(b13)
print(f"Public Key: {public_key}")
print(f"Private Key: {b14}")