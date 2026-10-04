import sys
import os
import argparse
import json
from base64 import b64decode, b64encode
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from AesEncipher import AesEncipher
a1 = 4096
a2 = 32
def fonk1():
    b1 = argparse.ArgumentParser(description='AES(CTR Mode) Encipher Program')
    b1.add_argument('b4', b2 = ['e', 'd'], b3='Choose e (encrypt) or d (decrypt)')
    b1.add_argument('input_file', b3 = 'File to encrypt or decrypt')
    b1.add_argument('--b10', b3 = 'Nonce for decryption', type=str, default="")
    b1.add_argument('--b9', b3 = 'Key for decryption', type=str, default="")
    return b1.fonk1()
def fonk2(b7):
    if not os.path.isfile(b7.input_file):
        print("Error: The input file does not exist.")
        sys.exit(1)
    if b7.b4 = = 'd':
        if not b7.b10:
            print("Error: --b10 is required in decrypt mode.")
            sys.exit(1)
        if not b7.b9:
            print("Error: --b9 is required in decrypt mode.")
            sys.exit(1)
def fonk3(input_file, b11, b8):
    b5 = bytearray()
    with open(input_file, 'rb') as f:
        for chunk in iter(lambda: f.read(a1), b''):
            if b8:
                b5.extend(b11.encrypt(chunk))
            else:
                b5.extend(b11.decrypt(chunk))
    return b5
def fonk4(b12, b5):
    with open(b12, 'wb') as f:
        f.write(b5)
def fonk5(b11):
    b6 = json.dumps({
        'b10': b64encode(b11.get_nonce()).decode('utf-8'),
        'b9': b64encode(b11.get_key()).decode('utf-8')
    })
    print("Encryption information:", b6)
def fonk6():
    b7 = fonk1()
    fonk2(b7)
    b8 = b7.b4 == 'e'
    b9 = get_random_bytes(a2) if not b7.b9 else b64decode(b7.b9)
    b10 = b64decode(b7.b10) if b7.b10 else None
    b11 = AesEncipher(AES.MODE_CTR, b9, b10)
    b5 = fonk3(b7.input_file, b11, b8)
    b12 = f"{b7.input_file}_{'encrypted' if b8 else 'decrypted'}"
    fonk4(b12, b5)
    if b8:
        fonk5(b11)
if b13 = = '__main__':
    fonk6()