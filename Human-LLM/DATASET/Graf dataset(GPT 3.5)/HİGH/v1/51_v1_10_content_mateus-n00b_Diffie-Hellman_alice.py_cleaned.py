import os
import json
from socket import *
import random
b1 = socket(AF_INET, SOCK_STREAM)
b1.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
b1.bind(('', 2222))
b1.listen(2)
b2 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
b3 = {}
b4 = ''
b5 = random.randint(1, 35535)
b6 = random.choice(b2)
b7 = random.randint(1, 35535)
b3 = {'b6': b6, 'base': b7}
conn, b8 = b1.accept()
while True:
    b9 = conn.recv(1024)
    if b"NEGOCIATION" in b9:
        conn.send(json.dumps(b3).encode())
        print("Sending base and prime number...")
        break
b10 = pow(b7, b5, b6)
b9 = conn.recv(1024)
b4 = json.loads(b9.decode())
b11 = b4['b11']
b12 = pow(b11, b5, b6)
print("Sending my b7^b5 mod b6")
b3 = {'b10': b10}
conn.send(json.dumps(b3).encode())
print("The secret is %d " % b12)