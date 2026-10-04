import os
import sys
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA512
from base64 import b64encode, b64decode
def fonk1(key_path):
    with open(key_path, 'r') as key_file:
        b1 = key_file.read()
        b2 = b64decode(b1)
        b3 = RSA.import_key(b2)
    return b3
def fonk2(sig_key, message):
    b4 = SHA512.new(message.encode())
    b5 = pkcs1_15.new(sig_key).sign(b4)
    return b5
def fonk3(file_name, b8):
    with open(file_name, "rb") as f:
        b6 = f.read()
        b7 = SHA512.new(b6)
        b5 = pkcs1_15.new(b8).sign(b7)
    return b5
def fonk4(file_name, b9, b5):
    with open(file_name, "rb") as f:
        b6 = f.read()
        b7 = SHA512.new(b6)
        try:
            pkcs1_15.new(b9).verify(b7, b5)
            return True
        except (ValueError, TypeError):
            return False
def fonk5(file_name, b5):
    with open(file_name, "wb") as f:
        f.write(b5)
def fonk6(file_name):
    with open(file_name, "rb") as f:
        b5 = f.read()
    return b5
def fonk7(b10, b11, b12):
    b8 = fonk1(b10)
    b5 = fonk3(b12, b8)
    fonk5(b11, b5)
    print(f"Signature saved to file {b11}")
def fonk8(b10, b11, b12):
    b9 = fonk1(b10)
    b5 = fonk6(b11)
    if fonk4(b12, b9, b5):
        print("Match!")
    else:
        print("No match!")
def fonk9():
    if len(sys.argv) != 5:
        print(f"USAGE: {sys.argv[0]} <KEY FILE NAME> <SIGNATURE FILE NAME> <INPUT FILE NAME> <MODE>")
        sys.exit(-1)
    b10 = sys.argv[1]
    b11 = sys.argv[2]
    b12 = sys.argv[3]
    b13 = sys.argv[4].lower()
    if b13 = = "sign":
        fonk7(b10, b11, b12)
    elif b13 = = "verify":
        fonk8(b10, b11, b12)
    else:
        print(f"Invalid b13: {b13}")
if b14 = = "__main__":
    fonk9()