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
	return sigKey.sign(string,' ')
def fonk3(fileName, privKey):
	with open(fileName,'r') as file:
		b4 = file.read()
	b5 = SHA512.new(b4).hexdigest()
	return fonk2(privKey,b5)
def fonk4(fileName, pubKey, b7):
	with open(fileName,'r') as file:
		b4 = file.read()
	b5 = SHA512.new(b4).hexdigest()
	return fonk7(b5,b7,pubKey)
def fonk5(fileName, b7):
	b6 = b7[0];
	b6 = str(b6)
	with open(fileName,'w') as file:
		file.write(b6)
def fonk6(fileName):
	with open(fileName,'r') as file:
		b7 = file.read()
	return tuple((int(b7),None))
def fonk7(theHash, sig, veriKey):
	return veriKey.verify(theHash,sig)
def fonk8():
	if len(sys.argv) < 5:
		print "USAGE: " + sys.argv[0] + " <KEY FILE NAME> <SIGNATURE FILE NAME> <INPUT FILE NAME>"
		exit(-1)
	b8 = sys.argv[1]
	b9 = sys.argv[2]
	b10 = sys.argv[3]
	b11 = sys.argv[4]
	b12 = fonk1(b8)
	if b11 = = "sign":
		fonk5(b9,fonk3(b10,b12))
		print "Signature saved to file ", b9
	elif b11 = = "verify":
		b7 = fonk6(b9)
		if fonk4(b10,b12,b7) == True:
			print "Signature Matches"
		else:
			print "Signature DO NOT MATCH"
	else:
		print "Invalid b11 ", b11
if b13 = = "__main__":
	fonk8()