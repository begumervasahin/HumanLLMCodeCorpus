import os
import random
import struct
import sys
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA512
from base64 import b64encode, b64decode
def fonk1(key_path):
    with open(key_path, 'r') as key_file:
        b1 = key_file.read()
        b2 = b64decode(b1)
        b3 = RSA.importKey(b2)
    return b3
def fonk2(sign_key, data):
    b4 = sign_key.sign(data, '')
    return b4
def fonk3(file_name, priv_key):
    with open(file_name, "r") as f:
        b5 = f.read()
    b6 = SHA512.new(b5.encode()).hexdigest()
    b4 = fonk2(priv_key, b6)
    return b4
def fonk4(file_name, pub_key, b4):
    with open(file_name, "r") as f:
        b5 = f.read()
    b7 = SHA512.new(b5.encode()).hexdigest()
    return pub_key.verify(b7, b4)
def fonk5(file_name, b4):
    with open(file_name, "w") as f:
        b8 = str(b4[0])
        f.write(b8)
def fonk6(file_name):
    with open(file_name, "r") as f:
        b5 = int(f.read())
    return (b5,)
def fonk7(b7, b4, verify_key):
    return verify_key.verify(b7, b4)
def fonk8():
    if len(sys.argv) < 5:
        print(f"USAGE: {sys.argv[0]} <KEY FILE NAME> <SIGNATURE FILE NAME> <INPUT FILE NAME> <MODE>")
        exit(-1)
    b9 = sys.argv[1]
    b10 = sys.argv[2]
    b11 = sys.argv[3]
    b12 = sys.argv[4]
    b3 = fonk1(b9)
    if b12 = = "sign":
        b4 = fonk3(b11, b3)
        fonk5(b10, b4)
        print(f"Signature saved to file {b10}")
    elif b12 = = "verify":
        b4 = fonk6(b10)
        if fonk4(b11, b3, b4):
            print("Match!")
        else:
            print("No match!")
    else:
        print(f"Invalid b12 {b12}")
if b13 = = "__main__":
    fonk8()