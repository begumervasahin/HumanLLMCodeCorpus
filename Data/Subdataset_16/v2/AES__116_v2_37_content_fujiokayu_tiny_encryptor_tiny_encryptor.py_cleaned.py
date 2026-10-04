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
    b1.add_argument('--b8', b3 = 'Nonce for decryption', type=str, default="")
    b1.add_argument('--b7', b3 = 'Key for decryption', type=str, default="")
    return b1.fonk1()
def fonk2(b5):
    if not os.path.isfile(b5.input_file):
        print("Error: The input file does not exist.")
        sys.exit(1)
    if b5.b4 = = 'd' and not b5.b8:
        print("Error: --b8 is required in decrypt mode.")
        sys.exit(1)
    if b5.b4 = = 'd' and not b5.b7:
        print("Error: --b7 is required in decrypt mode.")
        sys.exit(1)
def fonk3():
    b5 = fonk1()
    fonk2(b5)
    b6 = b5.b4 == 'e'
    b7 = get_random_bytes(a2) if not b5.b7 else b64decode(b5.b7)
    b8 = b64decode(b5.b8) if b5.b8 else None
    b9 = AesEncipher(AES.MODE_CTR, b7, b8)
    b10 = bytearray()
    with open(b5.input_file, 'rb') as f:
        for chunk in iter(lambda: f.read(a1), b''):
            if b6:
                b10.extend(b9.encrypt(chunk))
            else:
                b10.extend(b9.decrypt(chunk))
    b11 = f"{b5.input_file}_{'encrypted' if b6 else 'decrypted'}"
    with open(b11, 'wb') as translated_file:
        translated_file.write(b10)
    if b6:
        b12 = json.dumps({
            'b8': b64encode(b9.get_nonce()).decode('utf-8'),
            'b7': b64encode(b9.get_key()).decode('utf-8')
        })
        print("Encryption information:", b12)
if b13 = = '__main__':
    fonk3()