import random
from Crypto.Util import number
p = number.getPrime(9, None)
g = random.randint(5, 200)
x = random.randint(0, p - 1)
y = random.randint(0, p - 1)
alice_key = pow(g, x, p)
bob_key = pow(g, y, p)
print(f"g : {g}")
print(f"p : {p}")
print(f"Alice's public key: {alice_key}")
print(f"Bob's public key : {bob_key}")
alice_shared_secret = pow(bob_key, x, p)
bob_shared_secret = pow(alice_key, y, p)
if bob_shared_secret != alice_shared_secret:
    print("Woah! Something is terribly wrong.")
else:
    print(f"Alice's and Bob's shared secret: {alice_shared_secret}")
print("\n---Brute force---")
for X in range(0, p - 1):
    alice_public = pow(g, X, p)
    if alice_public == alice_key:
        break
secret = pow(bob_key, X, p)
print(f"\nFound! Alice's and Bob's shared secret: {secret}")