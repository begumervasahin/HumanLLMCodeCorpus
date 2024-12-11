import random
import math
import socket
def fonk1(num):
    if num < 2:
        return False
    for b1 in range(2, int(math.sqrt(num)) + 1):
        if num % b1 = = 0:
            return False
    return True
def fonk2(limit):
    b2 = []
    for num in range(100, limit):
        if fonk1(num):
            b2.append(num)
    return b2
def fonk3(modulo):
    b3 = []
    b4 = set(num for num in range(1, modulo) if math.gcd(num, modulo) == 1)
    for g in range(1, modulo):
        b5 = set(pow(g, power) % modulo for power in range(1, modulo))
        if b4 = = b5:
            b3.append(g)
    return b3
def fonk4(modulo):
    return random.randint(0, modulo - 1)
def fonk5(modulo, primitive_root, private_component):
    return pow(primitive_root, private_component, modulo)
def fonk6():
    b6 = 'localhost'
    b7 = int(input("Enter b7: "))
    b8 = fonk2(500)
    b9 = random.choice(b8)
    b10 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    b10.bind((b6, b7))
    b10.listen(1)
    print("Waiting for connection...")
    client_socket, b11 = b10.accept()
    print("Connected to client:", b11)
    print("Prime number (b9) is:", b9)
    client_socket.send(str(b9).encode())
    b12 = client_socket.recv(1024).decode()
    print("Received message from client:", b12)
    b13 = fonk3(b9)
    b14 = random.choice(b13)
    print("Primitive root (b14) is:", b14)
    client_socket.send(str(b14).encode())
    b15 = fonk4(b9)
    print("Private key component (b15) is:", b15)
    b16 = fonk5(b9, b14, b15)
    print("Public key component (b16) is:", b16)
    client_socket.send(str(b16).encode())
    b17 = int(client_socket.recv(1024).decode())
    print("Client's public key component (b17) is:", b17)
    b18 = pow(b17, b15, b9)
    print("Secret key (b18) is:", b18)
    client_socket.close()
    b10.close()
if b19 = = "__main__":
    fonk6()