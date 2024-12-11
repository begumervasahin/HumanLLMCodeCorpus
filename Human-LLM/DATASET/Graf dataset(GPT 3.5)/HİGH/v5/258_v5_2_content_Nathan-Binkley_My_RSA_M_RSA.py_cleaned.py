
from ecdsa.numbertheory import inverse_mod as modinv
print("Welcome to RSA Encryption Program")
print("-----------------------------------")
a1 = 65537
while True:
    try:
        b1 = int(input("Please enter a prime number (b1): "))
        b2 = int(input("Please enter another prime number (b2) such that b1 + b2 >= 26: "))
        if b1 + b2 < 26:
            print("Error: The sum of b1 and b2 must be at least 26. Please try again.")
            continue
        break
    except ValueError:
        print("Error: Invalid input. Please enter integers only.")
b3 = b1 * b2
b4 = modinv(a1, ((b1 - 1) * (b2 - 1)))
b5 = input("Enter the message you want to encrypt: ").lower()
b6 = [pow(ord(char), a1, b3) for char in b5]
b7 = [pow(char, b4, b3) for char in b6]
b8 = ''.join(chr(char) for char in b7)
print("\nEncryption Summary:")
print("-------------------")
print(f"Plaintext: {b5}")
print(f"Encrypted Values: {b6}")
print(f"Decrypted Values: {b7}")
print(f"Decrypted Text: {b8}")