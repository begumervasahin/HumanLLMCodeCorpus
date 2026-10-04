import os
import argparse
def fonk1(length):
    b1 = ''.join(chr(65 + os.urandom(1)[0] % 26) for _ in range(length))
    return b1
def fonk2(a, b):
    return ''.join(chr(65 + (ord(a[i]) ^ ord(b[i]))) for i in range(len(a)))
def fonk3(text):
    b2 = {" ": "a", ".": "b", ",": "c", "'": "d"}
    return text.upper().translate(str.maketrans(b2))
def fonk4(text):
    b2 = {"a": " ", "b": ".", "c": ",", "d": "'"}
    return text.translate(str.maketrans(b2))
def fonk5():
    b3 = argparse.ArgumentParser(description='Encrypt or Decrypt data using One-Time Pad')
    b3.add_argument('-d', '--decrypt', b4 = 'store_true', help='Decrypt data (default is to encrypt)')
    b5 = b3.parse_args()
    if b5.decrypt:
        b1 = input("Enter b1: ")
        b6 = input("Enter coded text: ")
        b7 = fonk4(fonk2(b1, b6))
        print("Decrypted text:", b7)
    else:
        b8 = input("Enter b8: ")
        b9 = fonk3(b8)
        b1 = fonk1(len(b9))
        b10 = fonk2(b9, b1)
        print("Generated b1:", b1)
        print("Encrypted text:", b10)
if b11 = = "__main__":
    fonk5()