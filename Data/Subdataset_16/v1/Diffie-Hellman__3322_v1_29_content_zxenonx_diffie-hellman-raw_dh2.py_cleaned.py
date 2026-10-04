import random
import hashlib
a1 = 9
a2 = 1001
b1 = random.randint(5, 10)
b2 = random.randint(10, 20)
b3 = pow(a1, b1, a2)
b4 = pow(a1, b2, a2)
print(f"a1: {a1} (shared base), a2: {a2} (prime number)")
print("\nAlice calculates:")
print(f"  a (Alice's secret): {b1}")
print(f"  Alice's public value (A): {b3} (a1^a mod a2)")
print("\nBob calculates:")
print(f"  b (Bob's secret): {b2}")
print(f"  Bob's public value (B): {b4} (a1^b mod a2)")
print("\nAlice calculates the shared key:")
b5 = pow(b4, b1, a2)
print(f"  Shared key (A^b mod a2): {b5}")
print(f"  SHA-256 Hash of key: {hashlib.sha256(str(b5).encode()).hexdigest()}")
print("\nBob calculates the shared key:")
b6 = pow(b3, b2, a2)
print(f"  Shared key (B^a mod a2): {b6}")
print(f"  SHA-256 Hash of key: {hashlib.sha256(str(b6).encode()).hexdigest()}")