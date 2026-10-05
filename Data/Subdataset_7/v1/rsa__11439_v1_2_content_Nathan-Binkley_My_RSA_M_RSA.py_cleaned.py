from ecdsa.numbertheory import inverse_mod as modinv
import sys
def fonk1():
    a1 = 65537
    try:
        b1 = int(input("Input a prime number: "))
        b2 = int(input("Input a different prime number (minimum added value of 26 for letters in alphabet): "))
        if b1 + b2 < 26:
            raise ValueError("Sum of input values should be at least 26")
    except ValueError as ve:
        print("Error:", ve)
        sys.exit(1)
    b3 = b1 * b2
    b4 = modinv(a1, ((b1-1)*(b2-1)))
    b5 = input("What would you like to encrypt? ").lower()
    print("Your b5 is:", b5)
    print("b1:", b1)
    print("b2:", b2)
    b6 = [ord(char) - 96 for char in b5 if char.isalpha()]
    print("Your b5 list is:", b6)
    b7 = [(i**a1) % b3 for i in b6]
    print("Your encrypted values are:", b7)
    b8 = [(i**b4) % b3 for i in b7]
    print("Your end result list is:", b8)
    b9 = ''.join([chr(num + 96) for num in b8])
    print("Plaintext (Unencrypted) is:", b9)
if b10 = = "__main__":
    fonk1()