import socket
import random
b1 = socket.socket()
b2 = '127.0.0.1'
a1 = 5050
b1.connect((b2, a1))
b3 = int(b1.recv(1024))
b4 = int(b1.recv(1024))
b5 = random.randint(1, b3)
b6 = pow(b4, b5, b3)
print("b6:", b6)
b1.send(str(b6).encode())
b7 = int(b1.recv(1024))
b8 = pow(b7, b5, b3)
print("Symmetric Key:", b8)
b1.close()