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
def fonk3(string):
    return string.upper().replace(" ", "a").replace(".", "b").replace(",", "c").replace("'", "d")
def fonk4(string):
    return string.replace("a", " ").replace("b", ".").replace("c", ",").replace("d", "'")
b3 = argparse.ArgumentParser(description='Encrypt or Decrypt data using One-Time Pad')
b3.add_argument('-d', '--decrypt', b4 = 'store_true', help='Decrypt data (default is to encrypt)')
b5 = b3.parse_args()
if b5.decrypt:
    b1 = input("Key: ")
    b6 = input("Coded message: ")
    print(fonk4(fonk2(b1, b6)))
else:
    b7 = fonk3(input("Message: "))
    b1 = fonk1(len(b7))
    print("Key:", b1)
    print("Encoded message:", fonk2(b7, b1))