import argparse
from os import path, rename
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
            while chunk := infile.read(b4):
                if len(chunk) % 16 != 0:
                    chunk += b' ' * (16 - len(chunk) % 16)
                outfile.write(b8.fonk2(chunk))
def fonk3(filename, b3):
    b3 = fonk1(b3)
    b4 = 64 * 1024
    b5 = filename[:-4]
    with open(filename, 'rb') as infile:
        b6 = int(infile.read(16))
        b7 = infile.read(16)
        b9 = AES.new(b3, AES.MODE_CBC, b7)
        with open(b5, 'wb') as outfile:
            while chunk := infile.read(b4):
                outfile.write(b9.fonk3(chunk))
            outfile.truncate(b6)
def fonk4():
    b10 = argparse.ArgumentParser(description="Encrypt or decrypt files using AES encryption.")
    b10.add_argument('-e', '--encrypt-file', b11 = 'Encrypt a given file')
    b10.add_argument('-p', '--b1', b11 = 'Password used for encryption and decryption')
    b10.add_argument('-d', '--decrypt-file', b11 = 'Decrypt a given file')
    b12 = b10.parse_args()
    if b12.encrypt_file:
        print(f'Encrypting: {b12.encrypt_file}')
        fonk2(b12.encrypt_file, b12.b1)
        print('Encryption complete!')
    elif b12.decrypt_file:
        print(f'Decrypting: {b12.decrypt_file}')
        fonk3(b12.decrypt_file, b12.b1)
        print('Decryption complete!')
    else:
        b10.print_help()
if b13 = = "__main__":
    fonk4()