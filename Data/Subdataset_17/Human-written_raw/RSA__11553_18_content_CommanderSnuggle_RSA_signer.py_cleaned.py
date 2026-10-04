import os, random, struct
import sys
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA512
from base64 import b64encode, b64decode
def loadKey(keyPath):
	key = None
	with open(keyPath, 'r') as keyFile:
		keyFileContent = keyFile.read()
		decodedKey = b64decode(keyFileContent)
		key = RSA.importKey(decodedKey)
	return key
def digSig(sigKey, string):
	signature = sigKey.sign(string, '')
	return signature
def getFileSig(fileName, privKey):
	f = open(fileName, "r")
	contents = f.read()
	fileSig = SHA512.new(contents).hexdigest()
	results = digSig(privKey, fileSig)
	return results
def verifyFileSig(fileName, pubKey, signature):
	f = open(fileName, "r")
	contents = f.read()
	dataHash = SHA512.new(contents).hexdigest()
	if pubKey.verify(dataHash, signature) == True:
		return True
	else:
		return False
def saveSig(fileName, signature):
	f = open(fileName, "w")
	tuple = str(signature[0])
	f.write(tuple)
def loadSig(fileName):
	f = open(fileName, "r")
	contents = int(f.read())
	contentTuple = ((contents,))
	return contentTuple
def verifySig(theHash, sig, veriKey):
	if veriKey.verify(theHash, sig) == veriKey:
		return veriKey.verify(theHash, sig)
def main():
	if len(sys.argv) < 5:
		print("USAGE: " + sys.argv[0] + " <KEY FILE NAME> <SIGNATURE FILE NAME> <INPUT FILE NAME>")
		exit(-1)
	keyFileName = sys.argv[1]
	sigFileName = sys.argv[2]
	inputFileName = sys.argv[3]
	mode = sys.argv[4]
	key = loadKey(keyFileName)
	if mode == "sign":
		result = getFileSig(inputFileName, key)
		saveSig(sigFileName, result)
		print("Signature saved to file ", sigFileName)
	elif mode == "verify":
		signature = loadSig(sigFileName)
		if verifyFileSig(inputFileName, key, signature) == True:
			print("Match!")
		else:
			print("No match!")
	else:
		print("Invalid mode ", mode)
if __name__ == "__main__":
	main()