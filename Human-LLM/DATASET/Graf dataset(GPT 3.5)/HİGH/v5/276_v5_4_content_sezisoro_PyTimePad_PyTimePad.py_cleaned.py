import sys
import argparse
import string
def fonk1(char, shift, decrypt):
    if decrypt:
        shift *= -1
    if char in string.ascii_letters:
        b1 = ord('A') if char.isupper() else ord('a')
        b2 = chr((ord(char) - b1 + shift) % 26 + b1)
    elif char in string.digits:
        b2 = chr((ord(char) - ord('0') + shift) % 10 + ord('0'))
    else:
        b2 = char
    return b2
def fonk2():
    b3 = argparse.ArgumentParser(description="Encrypt or decrypt a b7 using a conversion b8.")
    b3.add_argument("b8", b4 = int, help="conversion b8")
    b3.add_argument("-d", "--decrypt", b5 = "store_true", help="perform decryption")
    b6 = b3.parse_args()
    b7 = input("Enter the b7: ")
    b8 = str(b6.b8)
    if len(b7) > len(b8):
        b3.error("Error: b7 length cannot exceed b8 length.")
    b9 = [fonk1(char, int(b8[i % len(b8)]), b6.decrypt) for i, char in enumerate(b7)]
    b10 = ''.join(b9)
    print("Encrypted b7:" if not b6.decrypt else "Decrypted b7:", b10)
if b11 = = "__main__":
    fonk2()