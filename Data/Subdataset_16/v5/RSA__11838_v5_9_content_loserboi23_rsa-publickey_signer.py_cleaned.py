import os
import sys
from base64 import b64decode, b64encode
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA512
def fonk1(key_path):
    with open(key_path, 'r') as key_file:
        b1 = key_file.read()
        b2 = b64decode(b1)
        b3 = RSA.import_key(b2)
    return b3
def fonk2(private_key, data):
    b4 = SHA512.new(data.encode('utf-8'))
    b5 = pkcs1_15.new(private_key).sign(b4)
    return b64encode(b5).decode('utf-8')
def fonk3(file_name, private_key):
    with open(file_name, 'r') as file:
        b6 = file.read()
    return fonk2(private_key, b6)
def fonk4(public_key, data, b5):
    b4 = SHA512.new(data.encode('utf-8'))
    try:
        pkcs1_15.new(public_key).verify(b4, b64decode(b5))
        return True
    except (ValueError, TypeError):
        return False
def fonk5(file_name, public_key, b5):
    with open(file_name, 'r') as file:
        b6 = file.read()
    return fonk4(public_key, b6, b5)
def fonk6(file_name, b5):
    with open(file_name, 'w') as file:
        file.write(b5)
def fonk7(file_name):
    with open(file_name, 'r') as file:
        b5 = file.read()
    return b5
def fonk8():
    if len(sys.argv) < 5:
        print(f"USAGE: {sys.argv[0]} <KEY FILE NAME> <SIGNATURE FILE NAME> <INPUT FILE NAME> <MODE>")
        sys.exit(-1)
    b7 = sys.argv[1]
    b8 = sys.argv[2]
    b9 = sys.argv[3]
    b10 = sys.argv[4]
    b3 = fonk1(b7)
    if b10 = = "sign":
        b5 = fonk3(b9, b3)
        fonk6(b8, b5)
        print(f"Signature saved to file {b8}")
    elif b10 = = "verify":
        b5 = fonk7(b8)
        if fonk5(b9, b3.publickey(), b5):
            print("Signature Matches")
        else:
            print("Signature DOES NOT MATCH")
    else:
        print(f"Invalid b10 {b10}")
if b11 = = "__main__":
    fonk8()