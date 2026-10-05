import random
import math
import socket
def fonk1(limit):
    b1 = []
    for num in range(100, limit):
        b2 = True
        for b3 in range(2, int(math.sqrt(num)) + 1):
            if num % b3 = = 0:
                b2 = False
                break
        if b2:
            b1.append(num)
    return b1
def fonk2(a, b4):
    while b4 != 0:
        a, b4 = b4, a % b4
    return a
def fonk3(modulus):
    b5 = []
    b6 = set(num for num in range(1, modulus) if fonk2(num, modulus) == 1)
    for g in range(1, modulus):
        b7 = set(pow(g, power) % modulus for power in range(1, modulus))
        if b6 = = b7:
            b5.append(g)
    return b5
def fonk4(modulus):
    return random.randint(0, modulus - 1)
def fonk5(modulus, primitive_root, private_component):
    return pow(primitive_root, private_component, modulus)
def fonk6():
    b8 = 'localhost'
    b9 = int(input("Enter b9: "))
    a1 = 500
    b10 = fonk1(a1)
    b11 = random.choice(b10)
    b12 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    b12.bind((b8, b9))
    b12.listen(1)
    print("Waiting for connection...")
    client_socket, b13 = b12.accept()
    print("Connected to client:", b13)
    print("Prime number (b11) is:", b11)
    client_socket.send(str(b11).encode())
    b14 = client_socket.recv(1024).decode()
    print("Received message from client:", b14)
    b15 = fonk3(b11)
    b16 = random.choice(b15)
    print("Primitive root (b16) is:", b16)
    client_socket.send(str(b16).encode())
    b17 = fonk4(b11)
    print("Private key component (x1) is:", b17)
    b18 = fonk5(b11, b16, b17)
    print("Public key component (y1) is:", b18)
    client_socket.send(str(b18).encode())
    b19 = int(client_socket.recv(1024).decode())
    print("Client's public key component (yc) is:", b19)
    b20 = pow(b19, b17, b11)
    print("Secret key (k) is:", b20)
    client_socket.close()
    b12.close()
if b21 = = "__main__":
    fonk6()