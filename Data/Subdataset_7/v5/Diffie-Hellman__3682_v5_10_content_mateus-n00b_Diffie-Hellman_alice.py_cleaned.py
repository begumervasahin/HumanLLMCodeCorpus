import os
import json
import random
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
b1 = socket(AF_INET, SOCK_STREAM)
b1.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
b1.bind(('localhost', 2222))
b1.listen(2)
b2 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
b3 = random.randint(1, 35535)
b4 = random.choice(b2)
b5 = random.randint(1, 35535)
b6 = {'p': b4, 'b5': b5}
connection, b7 = b1.accept()
while True:
    b8 = connection.recv(1024)
    if b"NEGOTIATION" in b8:
        connection.send(json.dumps(b6).encode())
        print("Sending b5 and prime number...")
        break
b9 = pow(b5, b3, b4)
b8 = connection.recv(1024)
b10 = json.loads(b8.decode())
b11 = b10['b11']
b12 = pow(b11, b3, b4)
print("Sending my g^a mod p")
connection.send(json.dumps({'b9': b9}).encode())
print("The secret is %d" % b12)