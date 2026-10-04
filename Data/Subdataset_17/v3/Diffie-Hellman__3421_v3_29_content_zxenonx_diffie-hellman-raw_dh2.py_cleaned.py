import random
import hashlib
BASE = 9
PRIME = 1001
def generate_secret(min_value, max_value):
    return random.randint(min_value, max_value)
def compute_public_value(base, secret, prime):
    return pow(base, secret, prime)
def compute_shared_key(public_value, secret, prime):
    return pow(public_value, secret, prime)
def hash_key(key):
    return hashlib.sha256(str(key).encode()).hexdigest()
alice_secret = generate_secret(5, 10)
bob_secret = generate_secret(10, 20)
alice_public = compute_public_value(BASE, alice_secret, PRIME)
bob_public = compute_public_value(BASE, bob_secret, PRIME)
print("Shared Parameters:")
print(f"  Base (g): {BASE}")
print(f"  Prime (p): {PRIME}")
print("\nAlice's Computations:")
print(f"  Alice's secret (a): {alice_secret}")
print(f"  Alice's public value (A): {alice_public} (g^a mod p)")
print("\nBob's Computations:")
print(f"  Bob's secret (b): {bob_secret}")
print(f"  Bob's public value (B): {bob_public} (g^b mod p)")
print("\nShared Key Computation:")
alice_shared_key = compute_shared_key(bob_public, alice_secret, PRIME)
print(f"  Alice's shared key: {alice_shared_key}")
print(f"  SHA-256 hash of Alice's shared key: {hash_key(alice_shared_key)}")
bob_shared_key = compute_shared_key(alice_public, bob_secret, PRIME)
print(f"  Bob's shared key: {bob_shared_key}")
print(f"  SHA-256 hash of Bob's shared key: {hash_key(bob_shared_key)}")