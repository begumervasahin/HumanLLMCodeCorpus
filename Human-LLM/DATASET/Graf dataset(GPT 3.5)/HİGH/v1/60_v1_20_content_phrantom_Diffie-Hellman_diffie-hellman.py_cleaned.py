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
Step 1) User "a" needs to send to user "b":
                "a1", "b1", and "b4" (public number)
Step 2) User "b" sends to user "a":
                "b5" (public number)
Step 3) Each one calculates the shared secret and obtains the same key :-D
"""