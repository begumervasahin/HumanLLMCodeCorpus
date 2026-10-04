from __future__ import print_function
shared_prime = 23
shared_base = 5
alice_secret = 6
bob_secret = 15
print("Publicly Shared Variables:")
print("    Publicly Shared Prime: ", shared_prime)
print("    Publicly Shared Base:  ", shared_base)
alice_public = (shared_base ** alice_secret) % shared_prime
print("\n  Alice Sends Over Public Channel: ", alice_public)
bob_public = (shared_base ** bob_secret) % shared_prime
print("  Bob Sends Over Public Channel: ", bob_public)
print("\n------------\n")
print("Privately Calculated Shared Secret:")
alice_shared_secret = (bob_public ** alice_secret) % shared_prime
print("    Alice Shared Secret: ", alice_shared_secret)
bob_shared_secret = (alice_public ** bob_secret) % shared_prime
print("    Bob Shared Secret: ", bob_shared_secret)