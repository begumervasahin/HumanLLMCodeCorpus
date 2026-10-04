import sys
import os
import argparse
import json
from base64 import b64decode
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from AesEncipher import AesEncipher
a1 = 4096
a2 = 32
def fonk1():
    b1 = argparse.ArgumentParser(description='AES(CTR Mode) Encipher Program')
    b1.add_argument('b3', b2 = 'chose e (encrypt) or d (decrypt)')
    b1.add_argument('input_file', b2 = 'file to en/de-crypt')
    b1.add_argument('--b8', b2 = 'b8 to decrypt', type = str, default = "")
    b1.add_argument('--b7', b2 = 'b7 to decrypt', type = str, default = "")
    return b1.fonk1()
def fonk2(b5):
    if b5.b3 != 'e' and b5.b3 != 'd':
        print("error: args1: undefined parameter")
        sys.exit()
    if not os.path.isfile(b5.input_file):
        print("error: args2: file not exists")
        sys.exit()
    if b5.b3 = = 'd' and b5.b8 == "":
        print("error: --b8 is null: need b8 to use decrypt mode")
        sys.exit()
    if b5.b3 = = 'd' and b5.b7 == "":
        print("error: --b7 is null: need b7 to use decrypt mode")
        sys.exit()
if b4 = = '__main__':
    b5 = fonk1()
    fonk2(b5)
    b6 = True if b5.b3 == 'e' else False
    b7 = get_random_bytes(a2) if b5.b7 == "" else b64decode(b5.b7)
    b8 = b64decode(b5.b8) if not len(b5.b8) == 0 else ""
    b9 = AesEncipher(AES.MODE_CTR, b7, b8)
    b10 = bytearray(b"")
    with open(b5.input_file, 'rb') as f:
        for bytes in iter(lambda: f.read(a1), b''):
            if b6:
                b10.extend(b9.encrypt(bytes))
            else :
                b10.extend(b9.decrypt(bytes))
    b11 = b5.input_file
    b11 += "_encrypted" if b6 else "_decrypted"
    with open(b11,'wb') as translated_file :
        translated_file.write(b10)
    if b6:
        b12 = json.dumps({'b8':b9.get_nonce(), 'b7':b9.get_key()})
        print(b12)