import os
import random
from numpy import gcd
from library.Sieve_of_Eratosthenes import gen_primes
b1 = []
b2 = int(input("Generate primes below: "))
def fonk1(interval):
    for prime in gen_primes():
        if prime < interval:
            b1.append(prime)
        else:
            break
def fonk2():
    while True:
        b3 = random.choice(b1)
        b4 = random.choice(b1)
        print(f'Random prime_p below {b2} is: {b3}')
        print(f'Random b15 below {b2} is: {b4}')
        if b3 != b4:
            print("Primes are not equal: Pass")
            return b3, b4
        print("Primes must not be equal, generating new primes")
def fonk3(b3, b4):
    b5 = b3 * b4
    print("b5:", b5)
    return b5
def fonk4(b3, b4):
    b6 = (b3 - 1) * (b4 - 1)
    print("b17:", b6)
    return b6
def fonk5(b17):
    while True:
        b7 = random.randint(2, b17 - 1)
        if gcd(b17, b7) == 1:
            print("b7:", b7)
            return b7
def fonk6(phi, b7):
    b8 = gcd(phi, b7)
    print("gcd_calc:", b8)
    if b8 = = 1:
        print("GCD is 1: True")
        return True
    else:
        print("GCD is not 1: False")
        return False
def fonk7(b7, phi):
    def fonk8(b9, b):
        if b9 = = 0:
            return b, 0, 1
        g, x1, b10 = fonk8(b % b9, b9)
        b11 = b10 - (b
        b12 = x1
        return g, b11, b12
    g, b11, b13 = fonk8(b7, phi)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        b14 = b11 % phi
        print("b14:", b14)
        return b14
fonk1(b2)
prime_p, b15 = fonk2()
b16 = fonk3(prime_p, b15)
b17 = fonk4(prime_p, b15)
b7 = fonk5(b17)
if not fonk6(b17, b7):
    exit(1)
b14 = fonk7(b7, b17)
print(f"Public Key: (b5: {b16}, b7: {b7})")
print(f"Private Key: (b5: {b16}, b14: {b14})")