import random
import hashlib
a1 = 9
a2 = 1001
b1 = random.randint(5, 10)
b2 = random.randint(10, 20)
b3 = pow(a1, b1, a2)
b4 = pow(a1, b2, a2)
print(f"Shared Parameters:")
print(f"  Base (g): {a1}")
print(f"  Prime (p): {a2}")
print("\nAlice's Calculations:")
print(f"  Alice's secret (a): {b1}")
print(f"  Alice's public value (A): {b3} (g^a mod p)")
print("\nBob's Calculations:")
print(f"  Bob's secret (b): {b2}")
print(f"  Bob's public value (B): {b4} (g^b mod p)")
print("\nShared Key Computation:")
b5 = pow(b4, b1, a2)
print(f"  Alice's shared key: {b5} (B^a mod p)")
print(f"  SHA-256 hash of Alice's shared key: {hashlib.sha256(str(b5).encode()).hexdigest()}")
b6 = pow(b3, b2, a2)
print(f"  Bob's shared key: {b6} (A^b mod p)")
print(f"  SHA-256 hash of Bob's shared key: {hashlib.sha256(str(b6).encode()).hexdigest()}")