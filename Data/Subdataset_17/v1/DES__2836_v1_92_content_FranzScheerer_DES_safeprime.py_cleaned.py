import random
import math
import hashlib
import sys
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a
def next_prime(p):
    while p % 12 != 11:
        p += 1
    return next_prime_s(p)
def next_prime_s(p):
    m_ = 5 * 7 * 11 * 13 * 17 * 19 * 23 * 29 * 31
    while True:
        while gcd(p, m_) != 1 or gcd((p - 1)
            p += 12
        if pow(7, p - 1, p) != 1:
            p += 12
            continue
        if pow(7, (p - 3)
            p += 12
            continue
        return p
p = 2 * (1416461893 + 10**500) + 1
g = 3
print("Check p:", pow(11, p - 1, p) == 1)
px = (p - 1)
print("Check (p-1)/2:", pow(11, px - 1, px) == 1)
print("\nPrime p:", p)
alice = 2134143854854758971
bob = 2994143854854754312412
Pa = pow(g, alice, p)
Pb = pow(g, bob, p)
print("Public key sent from Alice to Bob:", Pa)
print("Public key sent from Bob to Alice:", Pb)
kab = pow(Pb, alice, p)
kba = pow(Pa, bob, p)
print("Are the keys equal? We check it:", kab == kba)