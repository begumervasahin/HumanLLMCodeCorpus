import random
import math
import socket
b1 = []
b2 = []
b3 = []
a1 = 0
a2 = 0
b4 = 'localhost'
b5 = int(input("Enter b5\n"))
def fonk1(n):
    for a3 in range(100,n):
        b6 = True
        for b7 in range(2,int(math.sqrt(a3)) + 1):
            if a3 % b7 = = 0:
                b6 = False
                break
        if b6:
            b1.append(a3)
fonk1(500)
b8 = random.choice(b1)
b9 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
b9.bind((b4,b5))
b9.listen(1)
c,b10 = b9.accept()
print("Prime is:",b8)
c.send(str(b8).encode())
b11 = c.recv(1024)
print(b11.decode())
print("Client Is",str(b10))
def fonk2(b16,b12):
    while b12 != 0:
        b16, b12 = b12, b16 % b12
    return b16
def fonk3(modulo):
    b13 = []
    b14 = set(num for num in range (1, modulo) if fonk2(num, modulo) == 1)
    for g in range(1, modulo):
        b15 = set(pow(g, powers) % modulo for powers in range (1, modulo))
        if b14 = = b15:
            b13.append(g)
    return b13
b2 = fonk3(b8)
b16 = random.choice(b2)
print("Primitive root is:",b16)
c.send(str(b16).encode())
def fonk4(b8):
    a3 = 0
    a4 = 0
    for a3 in range(b8):
        b3.append(a3)
    a4 = random.choice(b3)
    return a4
b17 = fonk4(b8)
print("private component:",b17)
def fonk5(b8,b16,b17):
    a5 = 0
    a5 = ((b16**b17)%b8)
    return a5
b18 = fonk5(b8,b16,b17)
print("public component:",b18)
a2 = int(c.recv(1024).decode())
c.send(str(b18).encode())
print("client:",a2)
a1 = ((a2**b17)%b8)
print("Secret key is",a1)
c.close()