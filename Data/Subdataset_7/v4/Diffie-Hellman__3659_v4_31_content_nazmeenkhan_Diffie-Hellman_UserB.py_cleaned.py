import socket
import random
b1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
b2 = '127.0.0.1'
a1 = 5050
b1.connect((b2, a1))
b3 = int(b1.recv(1024))
b4 = int(b1.recv(1024))
b5 = random.randint(1, b3)
b6 = pow(b4, b5, b3)
print("Generated Public Key (b6):", b6)
b7 = int(b1.recv(1024))
b1.send(str(b6).encode())
b8 = pow(b7, b5, b3)
print("Shared Symmetric Key (b8):", b8)
b1.close()