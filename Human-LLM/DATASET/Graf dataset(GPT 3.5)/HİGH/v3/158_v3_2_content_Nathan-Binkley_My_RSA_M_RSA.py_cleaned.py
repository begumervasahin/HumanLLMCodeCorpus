from ecdsa.numbertheory import inverse_mod as modinv
import sys
def fonk1():
    a1 = 65537
    try:
        b1 = int(input("Enter a prime number: "))
        b2 = int(input("Enter another prime number (ensure their sum is at least 26 for alphabet encoding): "))
        if b1 + b2 < 26:
            raise ValueError("The sum of the input values should be at least 26.")
    except ValueError as ve:
        print("Error:", ve)
        sys.exit(1)
    b3 = b1 * b2
    b4 = modinv(a1, ((b1-1)*(b2-1)))
    b5 = input("Enter the text you want to encrypt: ").lower()
    print("Your b5 is:", b5)
    print("b1:", b1)
    print("b2:", b2)
    b6 = [ord(char) - 96 for char in b5 if char.isalpha()]
    print("Your b5 list is:", b6)
    b7 = [(num**a1) % b3 for num in b6]
    print("Your encrypted values are:", b7)
    b8 = [(num**b4) % b3 for num in b7]
    print("Your decrypted values are:", b8)
    b9 = ''.join([chr(num + 96) for num in b8])
    print("Plaintext (Decrypted) is:", b9)
if b10 = = "__main__":
    fonk1()