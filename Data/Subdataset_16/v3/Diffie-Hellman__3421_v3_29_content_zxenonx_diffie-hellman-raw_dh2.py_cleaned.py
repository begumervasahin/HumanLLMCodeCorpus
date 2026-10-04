import random
import hashlib
a1 = 9
a2 = 1001
def fonk1(min_value, max_value):
    return random.randint(min_value, max_value)
def fonk2(base, secret, prime):
    return pow(base, secret, prime)
def fonk3(public_value, secret, prime):
    return pow(public_value, secret, prime)
def fonk4(key):
    return hashlib.sha256(str(key).encode()).hexdigest()
b1 = fonk1(5, 10)
b2 = fonk1(10, 20)
b3 = fonk2(a1, b1, a2)
b4 = fonk2(a1, b2, a2)
print("Shared Parameters:")
print(f"  Base (g): {a1}")
print(f"  Prime (p): {a2}")
print("\nAlice's Computations:")
print(f"  Alice's secret (a): {b1}")
print(f"  Alice's public value (A): {b3} (g^a mod p)")
print("\nBob's Computations:")
print(f"  Bob's secret (b): {b2}")
print(f"  Bob's public value (B): {b4} (g^b mod p)")
print("\nShared Key Computation:")
b5 = fonk3(b4, b1, a2)
print(f"  Alice's shared key: {b5}")
print(f"  SHA-256 hash of Alice's shared key: {fonk4(b5)}")
b6 = fonk3(b3, b2, a2)
print(f"  Bob's shared key: {b6}")
print(f"  SHA-256 hash of Bob's shared key: {fonk4(b6)}")