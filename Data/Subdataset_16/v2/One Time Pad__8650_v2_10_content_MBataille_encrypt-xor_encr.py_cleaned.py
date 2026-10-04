import os
import argparse
def fonk1(length):
    b1 = ""
    for _ in range(length):
        b1 += chr(65 + ord(os.urandom(1)) % 26)
    return b1
def fonk2(a, b):
    b2 = ""
    for i in range(len(a)):
        b2 += chr(64 + (ord(a[i]) ^ ord(b[i])))
    return b2
def fonk3(b8):
    return b8.upper().replace(" ", "a").replace(".", "b").replace(",", "c").replace("'", "d")
def fonk4(b8):
    return b8.replace("a", " ").replace("b", ".").replace("c", ",").replace("d", "'")
def fonk5():
    b3 = argparse.ArgumentParser(description='Encrypt or Decrypt data using One-Time Pad.')
    b3.add_argument('-d', '--decrypt', b4 = 'store_true', help='Decrypt data (default is to encrypt)')
    b5 = b3.parse_args()
    if b5.decrypt:
        b1 = input("Key: ")
        b6 = input("Coded b8: ")
        b7 = fonk4(fonk2(b1, b6))
        print("Decrypted b8:", b7)
    else:
        b8 = input("Message: ")
        b9 = fonk3(b8)
        b1 = fonk1(len(b9))
        b10 = fonk2(b9, b1)
        print("Key:", b1)
        print("Encrypted b8:", b10)
if b11 = = '__main__':
    fonk5()