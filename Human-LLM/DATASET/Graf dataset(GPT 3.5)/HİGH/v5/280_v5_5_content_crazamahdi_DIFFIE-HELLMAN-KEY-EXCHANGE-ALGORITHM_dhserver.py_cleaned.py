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
    b2 = [num for num in range(100, limit) if fonk1(num)]
    return b2
def fonk3(modulo):
    b3 = {num for num in range(1, modulo) if math.gcd(num, modulo) == 1}
    b4 = [g for g in range(1, modulo) if set(pow(g, power, modulo) for power in range(1, modulo)) == b3]
    return b4
def fonk4(modulo):
    return random.randint(0, modulo - 1)
def fonk5(modulo, primitive_root, private_component):
    return pow(primitive_root, private_component, modulo)
def fonk6():
    b5 = 'localhost'
    b6 = int(input("Enter b6: "))
    b7 = fonk2(500)
    b8 = random.choice(b7)
    b9 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    b9.bind((b5, b6))
    b9.listen(1)
    print("Waiting for connection...")
    client_socket, b10 = b9.accept()
    print("Connected to client:", b10)
    print("Prime number (b8) is:", b8)
    client_socket.send(str(b8).encode())
    b11 = client_socket.recv(1024).decode()
    print("Received message from client:", b11)
    b12 = fonk3(b8)
    b13 = random.choice(b12)
    print("Primitive root (b13) is:", b13)
    client_socket.send(str(b13).encode())
    b14 = fonk4(b8)
    print("Private key component (b14) is:", b14)
    b15 = fonk5(b8, b13, b14)
    print("Public key component (b15) is:", b15)
    client_socket.send(str(b15).encode())
    b16 = int(client_socket.recv(1024).decode())
    print("Client's public key component (b16) is:", b16)
    b17 = pow(b16, b14, b8)
    print("Secret key (b17) is:", b17)
    client_socket.close()
    b9.close()
if b18 = = "__main__":
    fonk6()