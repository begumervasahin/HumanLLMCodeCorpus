import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.b3.pbkdf2 import PBKDF2HMAC
from cryptography.b11 import Fernet
def fonk1(b18):
    b1 = b18.encode()
    b2 = b'salt_'
    b3 = PBKDF2HMAC(
        b4 = hashes.SHA256(),
        b5 = 32,
        b2 = b2,
        b6 = 100000,
        b7 = default_backend()
    )
    b8 = base64.urlsafe_b64encode(b3.derive(b1))
    return b8
def fonk2(b8, input_file):
    b9 = f'encrypted_{input_file}'
    with open(input_file, 'rb') as file:
        b10 = file.read()
    b11 = Fernet(b8)
    b12 = b11.encrypt(b10)
    with open(b9, 'wb') as file:
        file.write(b12)
def fonk3(b8, input_file):
    b9 = f'decrypted_{input_file}'
    with open(input_file, 'rb') as file:
        b10 = file.read()
    b11 = Fernet(b8)
    b13 = b11.decrypt(b10)
    with open(b9, 'wb') as file:
        file.write(b13)
def fonk4(input_file):
    b9 = f'binary_{input_file}'
    with open(input_file, 'r') as file:
        b10 = file.read()
    b14 = ''.join([bin(ord(c))[2:].zfill(8) for c in b10])
    with open(b9, 'w') as file:
        file.write(b14)
def fonk5(input_file):
    b9 = f'debinary_{input_file}'
    with open(input_file, 'r') as file:
        b10 = file.read()
    b15 = int(b10, 2)
    b16 = b15.to_bytes((b15.bit_length() + 7)
    with open(b9, 'w') as file:
        file.write(b16)
def fonk6():
    b17 = input("\b15'1' Encrypt a file \b15'2' Decrypt a file\b15'3' Convert to binary\b15'4' Convert from binary\b15>> ")
    if b17 = = '1':
        b18 = input("Enter b18 >> ")
        b19 = input("Enter file name in current directory >> ")
        b8 = fonk1(b18)
        fonk2(b8, b19)
    elif b17 = = '2':
        b18 = input("Enter b18 >> ")
        b19 = input("Enter file name in current directory >> ")
        b8 = fonk1(b18)
        fonk3(b8, b19)
    elif b17 = = '3':
        b19 = input("Enter file name in current directory >> ")
        fonk4(b19)
    elif b17 = = '4':
        b19 = input("Enter file name in current directory >> ")
        fonk5(b19)
    else:
        print("Invalid b17. Please try again.")
if b20 = = "__main__":
    fonk6()