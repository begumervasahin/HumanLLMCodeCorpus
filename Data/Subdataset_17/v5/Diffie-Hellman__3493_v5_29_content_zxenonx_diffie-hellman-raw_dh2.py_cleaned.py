import random
import hashlib
BASE = 9
PRIME = 1001
alice_secret = random.randint(5, 10)
bob_secret = random.randint(10, 20)
alice_public = pow(BASE, alice_secret, PRIME)
bob_public = pow(BASE, bob_secret, PRIME)
print(f"Shared Parameters:")
print(f"  Base (g): {BASE}")
print(f"  Prime (p): {PRIME}")
print("\nAlice's Calculations:")
print(f"  Alice's secret (a): {alice_secret}")
print(f"  Alice's public value (A): {alice_public} (g^a mod p)")
print("\nBob's Calculations:")
print(f"  Bob's secret (b): {bob_secret}")
print(f"  Bob's public value (B): {bob_public} (g^b mod p)")
print("\nShared Key Computation:")
alice_shared_key = pow(bob_public, alice_secret, PRIME)
print(f"  Alice's shared key: {alice_shared_key} (B^a mod p)")
print(f"  SHA-256 hash of Alice's shared key: {hashlib.sha256(str(alice_shared_key).encode()).hexdigest()}")
bob_shared_key = pow(alice_public, bob_secret, PRIME)
print(f"  Bob's shared key: {bob_shared_key} (A^b mod p)")
print(f"  SHA-256 hash of Bob's shared key: {hashlib.sha256(str(bob_shared_key).encode()).hexdigest()}")