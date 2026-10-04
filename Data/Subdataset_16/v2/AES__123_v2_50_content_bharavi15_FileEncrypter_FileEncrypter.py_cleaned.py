import argparse
from os import path
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random
def fonk1(b1):
    if b1 is None:
        b1 = "MyDefaultPassword"
    b2 = SHA256.new(b1.encode('utf-8'))
    return b2.digest()
def fonk2(filename, b3):
    b3 = fonk1(b3)
    b4 = 64 * 1024
    b5 = f"{filename}.enc"
    b6 = str(path.getsize(filename)).zfill(16)
    b7 = Random.new().read(16)
    b8 = AES.new(b3, AES.MODE_CBC, b7)
    with open(filename, 'rb') as infile:
        with open(b5, 'wb') as outfile:
            outfile.write(b6.encode('utf-8'))
            outfile.write(b7)
            while True:
                b9 = infile.read(b4)
                if len(b9) == 0:
                    break
                elif len(b9) % 16 != 0:
                    b9 += b' ' * (16 - len(b9) % 16)
                outfile.write(b8.fonk2(b9))
def fonk3(filename, b3):
    b3 = fonk1(b3)
    b4 = 64 * 1024
    b5 = filename[:-4]
    with open(filename, 'rb') as infile:
        b6 = int(infile.read(16))
        b7 = infile.read(16)
        b10 = AES.new(b3, AES.MODE_CBC, b7)
        with open(b5, 'wb') as outfile:
            while True:
                b9 = infile.read(b4)
                if len(b9) == 0:
                    break
                outfile.write(b10.fonk3(b9))
            outfile.truncate(b6)
def fonk4():
    b11 = argparse.ArgumentParser(description="Encrypt or decrypt files using AES encryption.")
    b11.add_argument('-e', '--encrypt-file', b12 = 'Encrypt a given file')
    b11.add_argument('-p', '--b1', b12 = 'Password used for encryption and decryption')
    b11.add_argument('-d', '--decrypt-file', b12 = 'Decrypt a given file')
    b13 = b11.parse_args()
    if b13.encrypt_file:
        print(f'Encrypting: {b13.encrypt_file}')
        fonk2(b13.encrypt_file, b13.b1)
        print('Encryption complete!')
    elif b13.decrypt_file:
        print(f'Decrypting: {b13.decrypt_file}')
        fonk3(b13.decrypt_file, b13.b1)
        print('Decryption complete!')
    else:
        b11.print_help()
if b14 = = "__main__":
    fonk4()