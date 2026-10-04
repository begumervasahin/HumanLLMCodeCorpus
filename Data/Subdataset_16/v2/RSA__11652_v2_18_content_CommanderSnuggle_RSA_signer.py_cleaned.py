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
def fonk3(file_name, priv_key):
    with open(file_name, "rb") as f:
        b6 = f.read()
        b7 = SHA512.new(b6)
        b5 = pkcs1_15.new(priv_key).sign(b7)
    return b5
def fonk4(file_name, pub_key, b5):
    with open(file_name, "rb") as f:
        b6 = f.read()
        b7 = SHA512.new(b6)
        try:
            pkcs1_15.new(pub_key).verify(b7, b5)
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
def fonk7():
    if len(sys.argv) < 5:
        print(f"USAGE: {sys.argv[0]} <KEY FILE NAME> <SIGNATURE FILE NAME> <INPUT FILE NAME> <MODE>")
        exit(-1)
    b8 = sys.argv[1]
    b9 = sys.argv[2]
    b10 = sys.argv[3]
    b11 = sys.argv[4]
    b3 = fonk1(b8)
    if b11 = = "sign":
        b12 = fonk3(b10, b3)
        fonk5(b9, b12)
        print(f"Signature saved to file {b9}")
    elif b11 = = "verify":
        b5 = fonk6(b9)
        if fonk4(b10, b3, b5):
            print("Match!")
        else:
            print("No match!")
    else:
        print(f"Invalid b11 {b11}")
if b13 = = "__main__":
    fonk7()