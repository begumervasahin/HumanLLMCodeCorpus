import random
import math
import socket
b1 = []
b2 = []
b3 = []
a1 = 0
a2 = 0
a3 = 0
a4 = 0
b4 = 'localhost'
b5 = int(input("Enter b5\n"))
b6 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
b6.connect((b4,b5))
a2 = int(b6.recv(1024).decode())
print("Prime :",a2)
b6.send(b"Send primitive root")
a3 = int(b6.recv(1024).decode())
print("Primitive root:",a3)
def fonk1(a2):
    a5 = 0
    a6 = 0
    for a5 in range(a2):
        b3.append(a5)
    a6 = random.choice(b3)
    return a6
b7 = fonk1(a2)
print("private component:",b7)
def fonk2(a2,a3,b7):
    a7 = 0
    a7 = ((a3**b7)%a2)
    return a7
b8 = fonk2(a2,a3,b7)
print("public component:",b8)
b6.send(str(b8).encode())
a4 = int(b6.recv(1024).decode())
print("Server:",a4)
a1 = ((a4**b7)%a2)
print("Secret key is",a1)
b6.close()