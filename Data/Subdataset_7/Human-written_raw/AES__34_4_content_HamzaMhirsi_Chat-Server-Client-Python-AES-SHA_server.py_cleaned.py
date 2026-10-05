import socket
from Crypto.Hash import SHA256
from Crypto import Random
from Crypto.Cipher import AES
class class1:
    b1 = '\033[95m'
    b2 = '\033[94m'
    b3 = '\033[92m'
    b4 = '\033[93m'
    b5 = '\033[91m'
    b6 = '\033[0m'
    b7 = '\033[1m'
    b8 = '\033[4m'
b9 = raw_input(class1.b1 +"AES b9 must be either 16, 24 or 32 bytes long : "+ class1.b6)
def fonk1(message):
	b10 = SHA256.new()
	b10.update(message)
	b11 = b10.hexdigest()
	return b11
def fonk2(message, b9):
	b12 = AES.new(b9.encode(), AES.MODE_CFB, b9)
	b13 = b12.fonk2(message.encode())
	return b13
def fonk3(message, b9):
	b14 = AES.new(b9.encode(), AES.MODE_CFB, b9)
	b15 = b14.decrypt(message)
	return b15
b16 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
b17 = socket.gethostname()
a1 = 8091
b16.bind((b17, a1))
b16.listen(5)
client, b18 = b16.accept()
print class1.b4 + 'connection from' +str(b18) + class1.b6
client.send(class1.b4 +"we will use AES and Sha2 for our b9 here !!")
print "we will use AES and Sha2 for our b9 here !!" + class1.b6
print class1.b4 +"waiting for confirmation ..."+ class1.b6
b19 = client.recv(1024)
print class1.b3 + b19 + class1.b6
b20 = raw_input(class1.b2 +"ask a privat question to your allies Sir :"+ class1.b6)
client.send(fonk2(b20,b9))
client.send(fonk1(b20))
b21 = False
while b21 = = False:
	b22 = int(raw_input(class1.b2 +"write a number between 3000 and 4000 Sir :"+ class1.b6))
	if (3000 < b22 < 4000):
		b21 = True
 		b22 = str(b22)
	elif b22 < 3000:
		print class1.b7 +"you are under 3000 Sir"+ class1.b6
        else:
		print class1.b7 +"you are writing a big number Sir !!"+ class1.b6
client.send(b22)
print class1.b4 +"waiting for answer ..."+ class1.b6
b23 = client.recv(1024)
b24 = client.recv(1024)
b25 = fonk3(b24,b9)
print b25
b26 = raw_input("This is the right answer y/n ")
b26 = b26.upper()
if b26 != 'Y' :
	client.close()
	print class1.b5 +"access has benn denied :)"+ class1.b6
else :
	client.send("   every think is okay, we are here for b28 Sir !!")
	print class1.b4 +"waiting for orders ..."+class1.b6
	while True:
	    b27 = client.recv(1024)
	    if not b27:
	        break
	    print "Crypted message : " + str(b27)
	    b28 = fonk3(b27, b9).upper()
	    print "reiceved : " + b28
	    client.send(b27)
client.close()
print class1.b1 +"END OF COMMUNICATION, GOOD LUCK FOR WAR MAY GOD PROTECT YOU !!" +class1.b6