import os
import sys
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA512
from base64 import b64encode, b64decode
def fonk1(key_path):
    with open(key_path, 'r') as key_file:
        b1 = key_file.read()
        b2 = b64decode(b1)
        return RSA.import_key(b2)
def fonk2(sign_key, data):
    b3 = SHA512.new(data.encode('utf-8'))
    b4 = pkcs1_15.new(sign_key).sign(b3)
    return b64encode(b4).decode('utf-8')
def fonk3(file_name, priv_key):
    with open(file_name, 'r') as file:
        b5 = file.read()
    return fonk2(priv_key, b5)
def fonk4(data, b4, verify_key):
    b3 = SHA512.new(data.encode('utf-8'))
    try:
        pkcs1_15.new(verify_key).verify(b3, b64decode(b4))
        return True
    except (ValueError, TypeError):
        return False
def fonk5(file_name, pub_key, b4):
    with open(file_name, 'r') as file:
        b5 = file.read()
    return fonk4(b5, b4, pub_key)
def fonk6(file_name, b4):
    with open(file_name, 'w') as file:
        file.write(b4)
def fonk7(file_name):
    with open(file_name, 'r') as file:
        return file.read()
def fonk8():
    if len(sys.argv) < 5:
        print(f"USAGE: {sys.argv[0]} <KEY FILE NAME> <SIGNATURE FILE NAME> <INPUT FILE NAME> <sign/verify>")
        sys.exit(-1)
    b6 = sys.argv[1]
    b7 = sys.argv[2]
    b8 = sys.argv[3]
    b9 = sys.argv[4]
    b10 = fonk1(b6)
    if b9 = = "sign":
        b4 = fonk3(b8, b10)
        fonk6(b7, b4)
        print(f"Signature saved to file {b7}")
    elif b9 = = "verify":
        b4 = fonk7(b7)
        if fonk5(b8, b10, b4):
            print("Signature Matches")
        else:
            print("Signature DOES NOT MATCH")
    else:
        print(f"Invalid b9 {b9}")
if b11 = = "__main__":
    fonk8()