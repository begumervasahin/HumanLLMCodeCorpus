import socket
import random
def fonk1(b4, X):
    return pow(b4, X, b3)
def fonk2(b1):
    return int(b1.recv(1024))
b1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
b2 = '127.0.0.1'
a1 = 5050
b1.connect((b2, a1))
b3 = fonk2(b1)
b4 = fonk2(b1)
b5 = random.randint(1, b3)
b6 = fonk1(b4, b5)
print("Generated Public Key (b6):", b6)
b7 = fonk2(b1)
b1.send(str(b6).encode())
b8 = pow(b7, b5, b3)
print("Shared Symmetric Key (b8):", b8)
b1.close()