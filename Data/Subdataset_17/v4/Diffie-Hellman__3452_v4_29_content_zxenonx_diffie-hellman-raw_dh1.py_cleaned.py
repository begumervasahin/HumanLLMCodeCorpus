from __future__ import print_function
shared_prime = 23
shared_base = 5
alice_secret = 6
bob_secret = 15
print("Publicly Shared Variables:")
print(f"    Prime: {shared_prime}")
print(f"    Base:  {shared_base}")
alice_public_value = pow(shared_base, alice_secret, shared_prime)
print(f"\n  Alice's Public Value (sent to Bob): {alice_public_value}")
bob_public_value = pow(shared_base, bob_secret, shared_prime)
print(f"  Bob's Public Value (sent to Alice): {bob_public_value}")
print("\n------------\n")
print("Privately Calculated Shared Secrets:")
alice_shared_secret = pow(bob_public_value, alice_secret, shared_prime)
print(f"    Alice's Shared Secret: {alice_shared_secret}")
bob_shared_secret = pow(alice_public_value, bob_secret, shared_prime)
print(f"    Bob's Shared Secret: {bob_shared_secret}")