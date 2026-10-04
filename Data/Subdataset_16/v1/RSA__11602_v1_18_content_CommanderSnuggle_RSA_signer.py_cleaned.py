import os
import sys
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA512
from base64 import b64encode, b64decode
def fonk1(keyPath):
    with open(keyPath, 'r') as keyFile:
        b1 = keyFile.read()
        b2 = b64decode(b1)
        b3 = RSA.import_key(b2)
    return b3
def fonk2(sigKey, message):
    b4 = SHA512.new(message.encode())
    b5 = pkcs1_15.new(sigKey).sign(b4)
    return b5
def fonk3(fileName, privKey):
    with open(fileName, "rb") as f:
        b6 = f.read()
        b7 = SHA512.new(b6)
        b5 = pkcs1_15.new(privKey).sign(b7)
    return b5
def fonk4(fileName, pubKey, b5):
    with open(fileName, "rb") as f:
        b6 = f.read()
        b7 = SHA512.new(b6)
        try:
            pkcs1_15.new(pubKey).verify(b7, b5)
            return True
        except (ValueError, TypeError):
            return False
def fonk5(fileName, b5):
    with open(fileName, "wb") as f:
        f.write(b5)
def fonk6(fileName):
    with open(fileName, "rb") as f:
        b5 = f.read()
    return b5
def fonk7():
    if len(sys.argv) < 5:
        print("USAGE: " + sys.argv[0] + " <KEY FILE NAME> <SIGNATURE FILE NAME> <INPUT FILE NAME> <MODE>")
        exit(-1)
    b8 = sys.argv[1]
    b9 = sys.argv[2]
    b10 = sys.argv[3]
    b11 = sys.argv[4]
    b3 = fonk1(b8)
    if b11 = = "sign":
        b12 = fonk3(b10, b3)
        fonk5(b9, b12)
        print("Signature saved to file", b9)
    elif b11 = = "verify":
        b5 = fonk6(b9)
        if fonk4(b10, b3, b5):
            print("Match!")
        else:
            print("No match!")
    else:
        print("Invalid b11", b11)
if b13 = = "__main__":
    fonk7()