import os
import sys
from base64 import b64decode
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA512
def fonk1(key_path):
    with open(key_path, 'r') as key_file:
        b1 = key_file.read()
        b2 = b64decode(b1)
        b3 = RSA.importKey(b2)
    return b3
def fonk2(private_key, data):
    b4 = PKCS1_v1_5.new(private_key)
    b5 = SHA512.new(data.encode())
    b6 = b4.sign(b5)
    return b6
def fonk3(file_path, private_key):
    with open(file_path, "r") as file:
        b7 = file.read()
    b6 = fonk2(private_key, b7)
    return b6
def fonk4(file_path, public_key, b6):
    with open(file_path, "r") as file:
        b7 = file.read()
    b8 = PKCS1_v1_5.new(public_key)
    b5 = SHA512.new(b7.encode())
    return b8.verify(b5, b6)
def fonk5(file_path, b6):
    with open(file_path, "w") as file:
        file.write(b6.hex())
def fonk6(file_path):
    with open(file_path, "r") as file:
        b9 = file.read()
    return bytes.fromhex(b9)
def fonk7():
    if len(sys.argv) < 5:
        print(f"USAGE: {sys.argv[0]} <KEY FILE NAME> <SIGNATURE FILE NAME> <INPUT FILE NAME> <MODE>")
        exit(-1)
    b10 = sys.argv[1]
    b11 = sys.argv[2]
    b12 = sys.argv[3]
    b13 = sys.argv[4]
    b3 = fonk1(b10)
    if b13 = = "sign":
        b6 = fonk3(b12, b3)
        fonk5(b11, b6)
        print(f"Signature saved to file {b11}")
    elif b13 = = "verify":
        b6 = fonk6(b11)
        if fonk4(b12, b3, b6):
            print("Match!")
        else:
            print("No match!")
    else:
        print(f"Invalid b13 {b13}")
if b14 = = "__main__":
    fonk7()