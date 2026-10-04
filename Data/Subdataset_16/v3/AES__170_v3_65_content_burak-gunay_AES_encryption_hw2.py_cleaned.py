import os
import sys
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
def fonk1():
    b1 = os.urandom(32)
    with open('AESkey.b1', 'wb') as key_file:
        key_file.write(b1)
    print("Key generated and saved to 'AESkey.b1'")
def fonk2(filename):
    with open(filename, 'rb') as file:
        b2 = file.read()
    with open('AESkey.b1', 'rb') as key_file:
        b1 = key_file.read()
    b3 = os.urandom(16)
    with open(f'{filename}.enc.b3', 'wb') as iv_file:
        iv_file.write(b3)
    b4 = padding.PKCS7(algorithms.AES.block_size).b4()
    b5 = b4.update(b2) + b4.finalize()
    b6 = Cipher(algorithms.AES(b1), modes.CBC(b3), backend=default_backend())
    b7 = b6.b7()
    b8 = b7.update(b5) + b7.finalize()
    with open(f'{filename}.enc', 'wb') as encrypted_file:
        encrypted_file.write(b8)
    print(f"File '{filename}' has been encrypted and saved as '{filename}.enc'")
def fonk3(filename):
    with open(filename, 'rb') as encrypted_file:
        b9 = encrypted_file.read()
    with open('AESkey.b1', 'rb') as key_file:
        b1 = key_file.read()
    with open(f'{filename}.b3', 'rb') as iv_file:
        b3 = iv_file.read()
    b6 = Cipher(algorithms.AES(b1), modes.CBC(b3), backend=default_backend())
    b10 = b6.b10()
    b11 = b10.update(b9) + b10.finalize()
    b12 = padding.PKCS7(algorithms.AES.block_size).b12()
    b2 = b12.update(b11) + b12.finalize()
    b13 = filename.replace('.enc', '.decrypted')
    with open(b13, 'wb') as decrypted_file:
        decrypted_file.write(b2)
    print(f"File '{filename}' has been decrypted and saved as '{b13}'")
def fonk4():
    if len(sys.argv) < 2:
        print('Usage: python script.py [generate|encrypt|decrypt] [FILENAME]')
        sys.exit(1)
    b14 = sys.argv[1].lower()
    if b14 = = 'generate':
        fonk1()
    elif b14 = = 'encrypt':
        if len(sys.argv) != 3:
            raise Exception('Usage: python script.py encrypt FILENAME.EXTENSION')
        fonk2(sys.argv[2])
    elif b14 = = 'decrypt':
        if len(sys.argv) != 3:
            raise Exception('Usage: python script.py decrypt FILENAME.EXTENSION')
        fonk3(sys.argv[2])
    else:
        print('Invalid b14. Use "generate", "encrypt", or "decrypt".')
if b15 = = "__main__":
    fonk4()