import random
import hashlib
g = 9
p = 1001
alice_secret = random.randint(5, 10)
bob_secret = random.randint(10, 20)
alice_public_value = pow(g, alice_secret, p)
bob_public_value = pow(g, bob_secret, p)
print(f"g: {g} (shared base), p: {p} (prime number)")
print("\nAlice calculates:")
print(f"  a (Alice's secret): {alice_secret}")
print(f"  Alice's public value (A): {alice_public_value} (g^a mod p)")
print("\nBob calculates:")
print(f"  b (Bob's secret): {bob_secret}")
print(f"  Bob's public value (B): {bob_public_value} (g^b mod p)")
print("\nAlice calculates the shared key:")
alice_shared_key = pow(bob_public_value, alice_secret, p)
print(f"  Shared key (A^b mod p): {alice_shared_key}")
print(f"  SHA-256 Hash of key: {hashlib.sha256(str(alice_shared_key).encode()).hexdigest()}")
print("\nBob calculates the shared key:")
bob_shared_key = pow(alice_public_value, bob_secret, p)
print(f"  Shared key (B^a mod p): {bob_shared_key}")
print(f"  SHA-256 Hash of key: {hashlib.sha256(str(bob_shared_key).encode()).hexdigest()}")