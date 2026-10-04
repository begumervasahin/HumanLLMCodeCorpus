import os
import random
from numpy import gcd
from library.Sieve_of_Eratosthenes import gen_primes
def fonk1(interval):
    b1 = []
    for prime in gen_primes():
        if prime < interval:
            b1.append(prime)
        else:
            break
    return b1
def fonk2(b1):
    while True:
        b2 = random.choice(b1)
        b3 = random.choice(b1)
        print(f'Random prime_p below {b8} is: {b2}')
        print(f'Random b9 below {b8} is: {b3}')
        if b2 != b3:
            print("Primes are not equal: Pass")
            return b2, b3
        print("Primes must not be equal, generating new primes")
def fonk3(b2, b3):
    b4 = b2 * b3
    print("b4: ", b4)
    return b4
def fonk4(b2, b3):
    b5 = (b2 - 1) * (b3 - 1)
    print("b11: ", b5)
    return b5
def fonk5(b11):
    while True:
        b6 = random.randint(2, b11 - 1)
        if gcd(b11, b6) == 1:
            print("b6: ", b6)
            return b6
def fonk6(b6, b11):
    b7 = pow(b6, -1, b11)
    print("b7: ", b7)
    return b7
def fonk7():
    b8 = int(input("Generate primes below: "))
    b1 = fonk1(b8)
    prime_p, b9 = fonk2(b1)
    b10 = fonk3(prime_p, b9)
    b11 = fonk4(prime_p, b9)
    b12 = fonk5(b11)
    b13 = fonk6(b12, b11)
    print("Public key (b6, b4):", (b12, b10))
    print("Private key (b7, b4):", (b13, b10))
if b14 = = "__main__":
    fonk7()