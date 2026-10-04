import os, random, struct
import sys
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA512
from base64 import b64encode, b64decode
def fonk1(keyPath):
	b1 = None
	with open(keyPath, 'r') as keyFile:
		b2 = keyFile.read()
		b3 = b64decode(b2)
		b1 = RSA.importKey(b3)
	return b1
def fonk2(sigKey, string):
	b4 = sigKey.sign(string, '')
	return b4
def fonk3(fileName, privKey):
	b5 = open(fileName, "r")
	b6 = b5.read()
	b7 = SHA512.new(b6).hexdigest()
	b8 = fonk2(privKey, b7)
	return b8
def fonk4(fileName, pubKey, b4):
	b5 = open(fileName, "r")
	b6 = b5.read()
	b9 = SHA512.new(b6).hexdigest()
	if pubKey.verify(b9, b4) == True:
		return True
	else:
		return False
def fonk5(fileName, b4):
	b5 = open(fileName, "w")
	b10 = str(b4[0])
	b5.write(b10)
def fonk6(fileName):
	b5 = open(fileName, "r")
	b6 = int(b5.read())
	b11 = ((b6,))
	return b11
def fonk7(theHash, sig, veriKey):
	if veriKey.verify(theHash, sig) == veriKey:
		return veriKey.verify(theHash, sig)
def fonk8():
	if len(sys.argv) < 5:
		print("USAGE: " + sys.argv[0] + " <KEY FILE NAME> <SIGNATURE FILE NAME> <INPUT FILE NAME>")
		exit(-1)
	b12 = sys.argv[1]
	b13 = sys.argv[2]
	b14 = sys.argv[3]
	b15 = sys.argv[4]
	b1 = fonk1(b12)
	if b15 = = "sign":
		b16 = fonk3(b14, b1)
		fonk5(b13, b16)
		print("Signature saved to file ", b13)
	elif b15 = = "verify":
		b4 = fonk6(b13)
		if fonk4(b14, b1, b4) == True:
			print("Match!")
		else:
			print("No match!")
	else:
		print("Invalid b15 ", b15)
if b17 = = "__main__":
	fonk8()