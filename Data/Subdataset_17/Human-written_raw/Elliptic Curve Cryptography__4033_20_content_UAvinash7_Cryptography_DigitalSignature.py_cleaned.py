from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto import Random
random_generator = Random.new().read
keyPair = RSA.generate(1024, random_generator)
pubKey = keyPair.publickey()
plainText = "Hello World"
hashA = SHA256.new(plainText).digest()
digitalSignature = keyPair.sign(hashA, "")
print ("Hash A: " + repr(hashA) + "\n")
print ("Digital Signature: " + repr(digitalSignature) + "\n")
hashB = SHA256.new(plainText).digest()
print("Hash B: " + repr(hashB) + "\n")
if (pubKey.verify(hashB, digitalSignature)):
	print ("Match")
else:
	print ("No Match")