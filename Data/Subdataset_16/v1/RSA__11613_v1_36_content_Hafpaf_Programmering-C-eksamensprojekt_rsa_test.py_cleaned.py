import os
import random
from numpy import b13
from library.Sieve_of_Eratosthenes import gen_primes
b1 = []
b2 = int(input("Generate primes below: "))
def fonk1(interval):
    for i in gen_primes():
        if i < interval:
            b1.append(i)
        else:
            break
def fonk2():
    while True:
        b3 = random.choice(b1)
        b4 = random.choice(b1)
        print(f'Random prime_p below {b2} is: {b3}')
        print(f'Random prime_q below {b2} is: {b4}')
        if b3 != b4:
            print("Primes not equal: Pass")
            return (b3, b4)
        print("Primes must not be equal, generating new primes")
def fonk3(b3, b4):
    b5 = b3 * b4
    print("b5: ", b5)
    return b5
def fonk4(b3, b4):
    b6 = (b3 - 1) * (b4 - 1)
    print("b11: ", b6)
    return b6
def fonk5(b11):
    while True:
        b7 = random.randint(2, b11 - 1)
        if b13(b11, b7) == 1:
            print("b7: ", b7)
            return b7
def fonk6(phi, b7):
    b8 = b13(phi, b7)
    print("b8: ", b8)
    return b8
def fonk7(b7, b11):
    b9 = pow(b7, -1, b11)
    print("b9: ", b9)
    return b9
fonk1(b2)
(prime_p, prime_q) = fonk2()
b10 = fonk3(prime_p, prime_q)
b11 = fonk4(prime_p, prime_q)
b12 = fonk5(b11)
b13 = fonk6(b11, b12)
b14 = fonk7(b12, b11)
print("Public key (b7, b5):", (b12, b10))
print("Private key (b9, b5):", (b14, b10))