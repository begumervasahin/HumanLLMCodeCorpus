import random
import math
import socket
def fonk1(n):
    b1 = []
    for i in range(100, n):
        b2 = True
        for b3 in range(2, int(math.sqrt(i)) + 1):
            if i % b3 = = 0:
                b2 = False
                break
        if b2:
            b1.append(i)
    return b1
def fonk2(b15, b4):
    while b4 != 0:
        b15, b4 = b4, b15 % b4
    return b15
def fonk3(modulo):
    b5 = []
    b6 = set(num for num in range(1, modulo) if fonk2(num, modulo) == 1)
    for g in range(1, modulo):
        b7 = set(pow(g, powers) % modulo for powers in range(1, modulo))
        if b6 = = b7:
            b5.append(g)
    return b5
def fonk4(b10):
    return random.randint(0, b10 - 1)
def fonk5(b10, b15, x):
    return pow(b15, x, b10)
def fonk6():
    b8 = 'localhost'
    b9 = int(input("Enter b9: "))
    b1 = fonk1(500)
    b10 = random.choice(b1)
    b11 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    b11.bind((b8, b9))
    b11.listen(1)
    print("Waiting for connection...")
    c, b12 = b11.accept()
    print("Connected to client:", b12)
    print("Prime is:", b10)
    c.send(str(b10).encode())
    b13 = c.recv(1024).decode()
    print("Received message from client:", b13)
    b14 = fonk3(b10)
    b15 = random.choice(b14)
    print("Primitive root is:", b15)
    c.send(str(b15).encode())
    b16 = fonk4(b10)
    print("Private component:", b16)
    b17 = fonk5(b10, b15, b16)
    print("Public component:", b17)
    c.send(str(b17).encode())
    b18 = int(c.recv(1024).decode())
    print("Client'b11 public component:", b18)
    b19 = pow(b18, b16, b10)
    print("Secret key is:", b19)
    c.close()
    b11.close()
if b20 = = "__main__":
    fonk6()