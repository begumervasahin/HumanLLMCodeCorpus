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
b6 = {'b4': b4, 'base': b5}
conn, b7 = b1.accept()
if b"NEGOTIATION" in conn.recv(1024):
    conn.send(json.dumps(b6).encode())
    print("Sending base and prime number...")
b8 = pow(b5, b3, b4)
b9 = conn.recv(1024)
b10 = json.loads(b9.decode())
b11 = b10['b11']
b12 = pow(b11, b3, b4)
print("Sending my b5^b3 mod b4")
conn.send(json.dumps({'b8': b8}).encode())
print("The secret is %d " % b12)