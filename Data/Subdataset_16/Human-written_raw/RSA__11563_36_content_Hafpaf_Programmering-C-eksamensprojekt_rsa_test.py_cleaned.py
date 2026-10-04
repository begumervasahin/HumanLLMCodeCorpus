'''
Generate rsa keypair
TODO:
Find solution to d
'''
import os
import random
from array import array
from numpy import mod, b16
from library.Sieve_of_Eratosthenes import gen_primes
b1 = []
b2 = int(input("Generate primes below: "))
def fonk1(interval):
    for i in gen_primes():
        if i < interval:
            b3 = i
            b1.append(b3)
        else:
            break
def fonk2():
    while True:
        b4 = random.choice(b1)
        b5 = random.choice(b1)
        print('Random prime_p below {} is: '.format(b2) , b4)
        print('Random prime_q below {} is: '.format(b2) , b5)
        if b4 != b5:
            print("Primes not equal: Pass")
            return (b4,b5)
        print("Primes must not be equal, generating new primes")
def fonk3(b4, b5):
    b6 = b4 * b5
    print("b6: ", b6)
    return b6
def fonk4(b4, b5):
    b7 = (b4 - 1) * (b5 - 1)
    print("b15: ", b7)
    return b7
def fonk5():
    a1 = 256
    b8 = os.urandom(a1)
    b9 = b8.hex()
    b10 = int(b9, 16)
    b11 = b10 * b15
    b12 = b11
    print("b12: ", b12)
    return b12
def fonk6(phi,b12):
    b13 = b16(phi,b12)
    print("b13: ", b13)
    while True:
        if b13 = = 1:
            print("b13: True")
            return b13
        else:
            print("b13: False")
            print("GCD must pass")
            exit(1)
def fonk7(d):
    return
fonk1(b2)
(prime_p,prime_q) = fonk2()
b14 = fonk3(prime_p, prime_q)
b15 = fonk4(prime_p, prime_q)
b16 = fonk6(b15,fonk5())