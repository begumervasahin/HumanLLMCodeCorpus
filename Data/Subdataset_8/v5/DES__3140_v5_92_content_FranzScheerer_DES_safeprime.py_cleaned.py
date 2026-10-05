import random
p = 2 * (1416461893 + 10 ** 500) + 1
g = 3
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a
def next_prime(p):
    while p % 12 != 11:
        p += 1
    return next_prime_step(p)
def next_prime_step(p):
    m_ = 5 * 7 * 11 * 13 * 17 * 19 * 23 * 29 * 31
    while True:
        if gcd(p, m_) == 1 and gcd((p - 1)
            if pow(7, p - 1, p) == 1 and pow(7, (p - 3)
                return p
        p += 12
p = next_prime(p)
print("Check p prime:", pow(11, p - 1, p) == 1)
px = (p - 1)
print("Check (p-1)/2 prime:", pow(11, px - 1, px) == 1)
print("\nGenerated Prime p:", p)
alice_private_key = 2134143854854758971
bob_private_key = 2994143854854754312412
Pa = pow(g, alice_private_key, p)
Pb = pow(g, bob_private_key, p)
print("Public key sent from Alice to Bob:", Pa)
print("Public key sent from Bob to Alice:", Pb)
kab = pow(Pb, alice_private_key, p)
kba = pow(Pa, bob_private_key, p)
print("Are the keys equal? We check it:", kab == kba)