from Crypto.Cipher import AES
import hashlib
import random
import sys
import Crypto
from ecc import getcurvebyname
from array import array
import socket
from socket import *
b1 = "127.168.2.75"
a1 = 4446
b2 = socket(AF_INET, SOCK_STREAM)
b2.bind((b1,a1))
b2.listen(1)
print( "Listening for connections.. ")
q,b3 = b2.accept()
b4 = raw_input("Enter b4 to be send:  ")
q.send(b4)
b2.close()
b1 = "127.168.2.75"
a1 = 4446
b2 = socket(AF_INET, SOCK_STREAM)
b2.connect((b1,a1))
b5 = b2.recv(1024)
print ("Message from server : " + b5.strip().decode('ascii'))
b2.close()
b6 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
b7 = [1]*10
a2 = 0
for a2 in range(10):
        b7[a2] = input("Please enter something: ").ljust(32)
        print("You entered " + str(b7[a2]))
b8 = getcurvebyname("ed25519")
print (str(b8))
print("b8 b9 = ",b8.curve_order)
print ("b10 = ",b8.b10)
b11 = b8.b10
b12 = (int(b8.b10.x),int(b8.b10.y))
print ("point with int x and y b12 = ",b12)
b13 = random.randint(1,2**255-19)
b14 = random.randint(1,2**255-19)
b15 = (b11.__mul__(b13))
a3 = 2
if (len(sys.argv)>1):
	a3 = int(sys.argv[1])
print ('b11: ',b11)
print ('b15 value: ',b15)
print ('b13 (b15 random): ',b13)
print ('b14 (b16 random): ',b14)
if (a3 = =0):
	b16 = (b11.__mul__(b14))
else:
	b16 = (b15.__mul__(a3)).__add__(b11.__mul__(b14))
print ("b15 = ", b15)
print ("b16 = ", b16)
b17 = [1]*10
for a2 in range (10):
        b17[a2]=hashlib.blake2s()
        b17[a2].update(str((b16.__add__(b15.__neg__().__mul__(a2))).__mul__(b13)).encode())
        b17[a2]=b17[a2].digest()
b18 = [1]*10
for a2 in range (10):
        b18[a2]= AES.new(b17[a2], AES.MODE_ECB)
print ('\nAlice calculates these keys')
b19 = [1]*10
for a2 in range (10):
 b19[a2]=b18[a2].encrypt(b7[a2])
print ('\nBob calculates this key:')
b20 = hashlib.blake2s()
b20.update(str(b15.__mul__(b14)).encode())
b21 = b20.digest()
print ('b16 key: ',b21)
b22 = AES.new(b21, AES.MODE_ECB)
b23 = [1]*10
for a2 in range (10):
        b23[a2]=b22.decrypt(b19[a2])
print ('\nBob decrypts the messages:')
for a2 in range (10):
        print ("b23:", b23 [a2])