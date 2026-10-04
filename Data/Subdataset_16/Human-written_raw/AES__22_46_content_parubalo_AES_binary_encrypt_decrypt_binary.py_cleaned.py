import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.b3.pbkdf2 import PBKDF2HMAC
from cryptography.b11 import Fernet
def fonk1(password_provided):
	b1 = password_provided.encode()
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
	b9 = 'encrypted_' + input_file
	with open(input_file, 'rb') as f:
	    b10 = f.read()
	b11 = Fernet(b8)
	b12 = b11.fonk2(b10)
	with open(b9, 'wb') as f:
	    f.write(b12)
def fonk3(b8, input_file):
	b9 = 'decrypted_' + input_file
	with open(input_file, 'rb') as f:
	    b10 = f.read()
	b11 = Fernet(b8)
	b12 = b11.fonk3(b10)
	with open(b9, 'wb') as f:
	    f.write(b12)
def fonk4(input_file):
        b9 = 'binary_' + input_file
        with open(input_file, 'r') as f:
                b10 = f.read()
        b13 = ''.join([bin(ord(c))[2:].rjust(8,'0') for c in b10])
        with open(b9, 'w') as f:
                f.write(b13)
def fonk5(input_file):
        b9 = 'debinary_' + input_file
        with open(input_file, 'r') as f:
                b10 = f.read()
        b14 = int(b10, 2)
        b15 = b14.to_bytes((b14.bit_length() + 7)
        with open(b9, 'w') as f:
                f.write(b15)
b16 = input("\b14'1' Encrypt a file \b14'2' Decrypt a file\b14'3' Convert to b13\b14'4' Convert from b13\b14>> ")
if b16 = = '1':
	b1 = input("Enter b1 >> ")
	b17 = input("\nEnter file b17 in current directory >> ")
	fonk2(fonk1(b1), b17)
elif b16 = = '2':
	b1 = input("Enter b1 >> ")
	b17 = input("\nEnter file b17 in current directory >> ")
	fonk3(fonk1(b1), b17)
elif b16 = = '3':
	b17 = input("\nEnter file b17 in current directory >> ")
	fonk4(b17)
elif b16 = = '4':
	b17 = input("\nEnter file b17 in current directory >> ")
	fonk5(b17)
else:
	print("Sorry...")