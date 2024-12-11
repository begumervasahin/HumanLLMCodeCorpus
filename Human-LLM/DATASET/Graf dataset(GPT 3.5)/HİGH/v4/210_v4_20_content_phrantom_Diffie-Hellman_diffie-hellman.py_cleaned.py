from Crypto.Util.number import getPrime
from random import randint
print("\n")
a1 = 2
b1 = getPrime(1024)
print("Generator:", a1)
print("Prime number:", b1)
b2 = randint(b1
b3 = randint(b1
b4 = pow(a1, b2, b1)
b5 = pow(a1, b3, b1)
b6 = pow(b5, b2, b1)
b7 = pow(b4, b3, b1)
assert b6 = = b7
print("\nPublic number of A:", b4)
print("Public number of B:", b5)
print("\nShared secret A:", b6)
print("Shared secret B:", b7)
"""
Step 1) User "A" sends the following information to user "B":
        - Generator
        - Prime number
        - Public key of A (public number)
Step 2) User "B" sends the following information to user "A":
        - Public key of B (public number)
Step 3) Both parties calculate the shared secret and obtain the same key :-D
"""