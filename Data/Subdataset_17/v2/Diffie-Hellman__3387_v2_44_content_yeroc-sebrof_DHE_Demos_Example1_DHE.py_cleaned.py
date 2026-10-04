import sys
from random import randrange
def generate_random_prime(primes):
    return primes[randrange(len(primes))]
def main():
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
    a = generate_random_prime(primes)
    b = generate_random_prime(primes)
    p = primes[randrange(5, len(primes))]
    g = generate_random_prime(primes)
    A = pow(g, a, p)
    B = pow(g, b, p)
    print("Public/Shared Values")
    print("g =", g)
    print("p =", p)
    print()
    print("Private Keys")
    print("a =", a)
    print("b =", b)
    print()
    print("Public Keys")
    print(f"A = {A} == g^a mod p == {g}^{a} mod {p}")
    print(f"B = {B} == g^b mod p == {g}^{b} mod {p}")
    print()
    secretA = pow(B, a, p)
    secretB = pow(A, b, p)
    print(f"Alice's secret generation == B^a mod p == {B}^{a} mod {p} == {secretA}")
    print(f"Bob's secret generation   == A^b mod p == {A}^{b} mod {p} == {secretB}")
if __name__ == "__main__":
    main()