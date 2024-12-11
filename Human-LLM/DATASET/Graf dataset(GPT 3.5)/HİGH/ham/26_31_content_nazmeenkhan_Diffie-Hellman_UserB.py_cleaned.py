import socket
import math
import random
b1 = socket.socket()
b2 = '127.0.0.1'
a1 = 5050
b1.connect((b2, a1))
b3 = int(b1.recv(1024))
b4 = int(b1.recv(1024))
b5 = random.randint(1,b3)
b6 = pow(b4,b5,b3)
print("b6: ", b6)
b7 = int(b1.recv(1024))
b1.send(str(b6).encode())
b8 = pow(b7,b5,b3)
print("Symmetric Key: ",b8)
b1.close()
'''b5 = int(input("Enter b5: "))
print("b5 :",b5)
b3 = int(input("Enter a prime number: "))
a2 = 0
b9 = []
for each in range(1, b3):
	a2 += 1
	b10 = []
	for i in range(1, b3):
		b11 = (a2 ** i) % b3
		b10.append(b11)
		b12 = set(b10)
		if len(b12) == len(range(1,b3)):
			b9.append(a2)
print ("Primitive roots of %d are:" % b3)
print ("Primitive roots of %d are:" % b3)
print (b9)
b4 = b9[0]
if b5<b3 :
	b6 = (str((b4**b5)%b3)).encode()
b7 = int(b1.recv(1024))
print(b7)
b1.send(b6)
b8 = (b7**b5)%b3
print(b8)'''