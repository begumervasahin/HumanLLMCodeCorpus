
from ecdsa.numbertheory import inverse_mod as modinv
import sys
print("Welcome to RSA Encryption Program")
print("-------------------------------")
e = 65537
while True:
    try:
        p = int(input("Please enter a prime number (p): "))
        q = int(input("Please enter another prime number (q) such that p + q >= 26: "))
        if p + q < 26:
            print("The sum of p and q must be at least 26. Please try again.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter integers only.")
n = p * q
d = modinv(e, ((p - 1) * (q - 1)))
plaintext = input("Enter the message you want to encrypt: ").lower()
encrypted_values = [pow(ord(char), e, n) for char in plaintext]
decrypted_values = [pow(char, d, n) for char in encrypted_values]
decrypted_text = ''.join(chr(char) for char in decrypted_values)
print("\nEncryption Summary:")
print("-------------------")
print("Plaintext: " + plaintext)
print("Encrypted Values: " + str(encrypted_values))
print("Decrypted Values: " + str(decrypted_values))
print("Decrypted Text: " + decrypted_text)