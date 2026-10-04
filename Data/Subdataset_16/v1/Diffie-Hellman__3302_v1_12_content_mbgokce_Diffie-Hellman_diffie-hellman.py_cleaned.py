import random
from Crypto.Util import number
b1 = number.getPrime(9, None)
b2 = random.randint(5, 200)
b3 = random.randint(0, b1 - 1)
b4 = random.randint(0, b1 - 1)
b5 = pow(b2, b3, b1)
b6 = pow(b2, b4, b1)
print(f"b2 : {b2}")
print(f"b1 : {b1}")
print(f"Alice's public key: {b5}")
print(f"Bob's public key : {b6}")
b7 = pow(b6, b3, b1)
b8 = pow(b5, b4, b1)
if b8 != b7:
    print("Woah! Something is terribly wrong.")
else:
    print(f"Alice's and Bob's shared b10: {b7}")
print("\n---Brute force---")
for X in range(0, b1 - 1):
    b9 = pow(b2, X, b1)
    if b9 = = b5:
        break
b10 = pow(b6, X, b1)
print(f"\nFound! Alice's and Bob's shared b10: {b10}")