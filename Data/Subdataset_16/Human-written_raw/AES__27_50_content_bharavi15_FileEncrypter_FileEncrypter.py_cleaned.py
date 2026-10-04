from argparse import ArgumentParser
from os import path,rename
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random
def fonk1(filename,b1):
	b1 = fonk3(b1)
	b2 = 64 * 1024
	b3 = filename+'.enc'
	b4 = str(path.getsize(filename)).zfill(16)
	b5 = Random.new().read(16)
	b6 = AES.new(b1, AES.MODE_CBC, b5)
	with open(filename, 'rb') as infile:
		with open(b3, 'wb') as outfile:
			outfile.write(b4.encode('utf-8'))
			outfile.write(b5)
			while True:
				b7 = infile.read(b2)
				if len(b7) == 0:
					break
				elif len(b7) % 16 != 0:
					b7 +=b' ' * (16-(len(b7) % 16))
				outfile.write(b6.fonk1(b7))
def fonk2(filename,b1):
	b1 = fonk3(b1)
	b2 = 64 * 1024
	b3 = filename[:-4]
	with open(filename, 'rb') as infile:
		b4 = int(infile.read(16))
		b5 = infile.read(16)
		b8 = AES.new(b1, AES.MODE_CBC, b5)
		with open(b3, 'wb') as outfile:
			while True:
				b7 = infile.read(b2)
				if len(b7) == 0:
					break
				outfile.write(b8.fonk2(b7))
				outfile.truncate(b4)
def fonk3(b9):
	if b9 is None:
		b9 = "MyDefaultPassword"
	b10 = SHA256.new(b9.encode('utf-8'))
	return b10.digest()
b11 = ArgumentParser()
b11.add_argument('-e','--encrypt-file', b12 = 'Encrypt a given file', required=False)
b11.add_argument('-p','--b9', b12 = 'Password used for encryption and decryption', required=False)
b11.add_argument('-d','--decrypt-file', b12 = 'Decrypt a given file', required=False)
b13 = b11.parse_args()
if b13.encrypt_file:
	print('b14 = ',b13.encrypt_file)
	fonk1(b13.encrypt_file,b13.b9)
	print('Done!')
elif b13.decrypt_file:
	print('b15 = ',b13.decrypt_file)
	fonk2(b13.decrypt_file,b13.b9)
	print('Done!')
else:
    b11.print_help()