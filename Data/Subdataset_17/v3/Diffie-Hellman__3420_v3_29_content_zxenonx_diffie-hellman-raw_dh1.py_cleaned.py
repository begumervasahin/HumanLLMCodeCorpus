from __future__ import print_function
PRIME = 23
BASE = 5
alice_secret = 6
bob_secret = 15
print("Publicly Shared Parameters:")
print(f"    Prime: {PRIME}")
print(f"    Base:  {BASE}")
alice_public_value = pow(BASE, alice_secret, PRIME)
print(f"\n  Alice's Public Value (sent to Bob): {alice_public_value}")
bob_public_value = pow(BASE, bob_secret, PRIME)
print(f"  Bob's Public Value (sent to Alice): {bob_public_value}")
print("\n------------\n")
print("Privately Calculated Shared Secrets:")
alice_shared_secret = pow(bob_public_value, alice_secret, PRIME)
print(f"    Alice's Shared Secret: {alice_shared_secret}")
bob_shared_secret = pow(alice_public_value, bob_secret, PRIME)
print(f"    Bob's Shared Secret: {bob_shared_secret}")