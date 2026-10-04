from Crypto import Random
from Crypto.PublicKey import RSA
b1 = Random.new().read
b2 = RSA.generate(1024,b1)
b3 = b2
b4 = b2.publickey()
b5 = Random.new().read
b6 = RSA.generate(1024,b5)
b7 = b6
b8 = b6.publickey()
b9 = open("b3.txt","w")
b10 = open("b4.txt","w")
b11 = open("b7.txt","w")
b12 = open("b8.txt","w")
b9.write(b3.exportKey())
b10.write(b4.exportKey())
b11.write(b7.exportKey())
b12.write(b8.exportKey())
b9.close()
b10.close()
b11.close()
b12.close()
print "Finish genrating key pairs"