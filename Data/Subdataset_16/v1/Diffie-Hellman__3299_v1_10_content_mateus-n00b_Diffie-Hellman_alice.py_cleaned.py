import os
import json
from socket import *
import random
def fonk1():
    b1 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    return random.choice(b1)
b2 = socket(AF_INET, SOCK_STREAM)
b2.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
b2.bind(('', 2222))
b2.listen(2)
b3 = random.randint(1, 35535)
b4 = fonk1()
b5 = random.randint(1, 35535)
b6 = {'b4': b4, 'base': b5}
conn, b7 = b2.accept()
while True:
    b8 = conn.recv(1024).decode('utf-8')
    if "NEGOCIATION" in b8:
        conn.send(json.dumps(b6).encode('utf-8'))
        print("Sending base and prime number...")
        break
b9 = (b5 ** b3) % b4
b8 = conn.recv(1024).decode('utf-8')
b10 = json.loads(b8)
b11 = b10['b11']
b12 = (b11 ** b3) % b4
print("Sending my b5^b3 mod b4")
b6 = {'b9': b9}
conn.send(json.dumps(b6).encode('utf-8'))
print(f"The secret is {b12}")
conn.close()
b2.close()