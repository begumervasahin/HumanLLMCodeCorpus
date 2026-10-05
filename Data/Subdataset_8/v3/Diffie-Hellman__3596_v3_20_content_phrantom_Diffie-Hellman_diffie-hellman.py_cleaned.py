from Crypto.Util.number import getPrime
from random import randint
print("\n")
generator = 2
prime_number = getPrime(1024)
print("Generator:", generator)
print("Prime number:", prime_number)
private_key_A = randint(prime_number
private_key_B = randint(prime_number
public_key_A = pow(generator, private_key_A, prime_number)
public_key_B = pow(generator, private_key_B, prime_number)
shared_secret_A = pow(public_key_B, private_key_A, prime_number)
shared_secret_B = pow(public_key_A, private_key_B, prime_number)
assert shared_secret_A == shared_secret_B
print("\nPublic number of A:", public_key_A)
print("Public number of B:", public_key_B)
print("\nShared secret A:", shared_secret_A)
print("Shared secret B:", shared_secret_B)
"""
Step 1) User "A" sends the following information to user "B":
        - Generator
        - Prime number
        - Public key of A (public number)
Step 2) User "B" sends the following information to user "A":
        - Public key of B (public number)
Step 3) Both parties calculate the shared secret and obtain the same key :-D
"""