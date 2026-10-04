import random
from Crypto.Util import number
p = number.getPrime(9, None)
g = random.randint(5, 200)
alice_private_key = random.randint(0, p - 1)
bob_private_key = random.randint(0, p - 1)
alice_public_key = pow(g, alice_private_key, p)
bob_public_key = pow(g, bob_private_key, p)
print(f"g : {g}")
print(f"p : {p}")
print(f"Alice's public key: {alice_public_key}")
print(f"Bob's public key : {bob_public_key}")
alice_shared_secret = pow(bob_public_key, alice_private_key, p)
bob_shared_secret = pow(alice_public_key, bob_private_key, p)
if bob_shared_secret != alice_shared_secret:
    print("Woah! Something is terribly wrong.")
else:
    print(f"Alice's and Bob's shared secret: {alice_shared_secret}")
print("\n---Brute force---")
for possible_private_key in range(0, p - 1):
    possible_public_key = pow(g, possible_private_key, p)
    if possible_public_key == alice_public_key:
        break
brute_forced_secret = pow(bob_public_key, possible_private_key, p)
print(f"\nFound! Alice's and Bob's shared secret: {brute_forced_secret}")