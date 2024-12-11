import random
import math
import socket
def fonk1(limit):
    b1 = []
    for num in range(100, limit):
        if fonk2(num):
            b1.append(num)
    return b1
def fonk2(num):
    if num < 2:
        return False
    for b2 in range(2, int(math.sqrt(num)) + 1):
        if num % b2 = = 0:
            return False
    return True
def fonk3(a, b3):
    while b3 != 0:
        a, b3 = b3, a % b3
    return a
def fonk4(modulus):
    b4 = []
    b5 = set(num for num in range(1, modulus) if fonk3(num, modulus) == 1)
    for g in range(1, modulus):
        b6 = set(pow(g, power) % modulus for power in range(1, modulus))
        if b5 = = b6:
            b4.append(g)
    return b4
def fonk5(modulus):
    return random.randint(0, modulus - 1)
def fonk6(modulus, primitive_root, private_component):
    return pow(primitive_root, private_component, modulus)
def fonk7():
    b7 = 'localhost'
    b8 = int(input("Enter b8: "))
    a1 = 500
    b9 = fonk1(a1)
    b10 = random.choice(b9)
    b11 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    b11.bind((b7, b8))
    b11.listen(1)
    print("Waiting for connection...")
    client_socket, b12 = b11.accept()
    print("Connected to client:", b12)
    print("Prime number (b10) is:", b10)
    client_socket.send(str(b10).encode())
    b13 = client_socket.recv(1024).decode()
    print("Received message from client:", b13)
    b14 = fonk4(b10)
    b15 = random.choice(b14)
    print("Primitive root (b15) is:", b15)
    client_socket.send(str(b15).encode())
    b16 = fonk5(b10)
    print("Private key component (x1) is:", b16)
    b17 = fonk6(b10, b15, b16)
    print("Public key component (y1) is:", b17)
    client_socket.send(str(b17).encode())
    b18 = int(client_socket.recv(1024).decode())
    print("Client's public key component (yc) is:", b18)
    b19 = pow(b18, b16, b10)
    print("Secret key (k) is:", b19)
    client_socket.close()
    b11.close()
if b20 = = "__main__":
    fonk7()