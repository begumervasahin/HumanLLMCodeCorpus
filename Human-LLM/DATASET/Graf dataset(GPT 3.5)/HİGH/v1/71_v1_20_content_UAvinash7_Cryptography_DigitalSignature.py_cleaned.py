from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto import Random
b1 = Random.new().read
b2 = RSA.generate(1024, b1)
b3 = b2.publickey()
b4 = "Hello World"
b5 = SHA256.new(b4.encode()).digest()
b6 = b2.sign(b5, "")
print("Hash A:", repr(b5), "\n")
print("Digital Signature:", repr(b6), "\n")
b7 = SHA256.new(b4.encode()).digest()
print("Hash B:", repr(b7), "\n")
if b3.verify(b7, b6):
    print("Match")
else:
    print("No Match")