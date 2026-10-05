import os
import json
import random
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
tcp = socket(AF_INET, SOCK_STREAM)
tcp.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
tcp.bind(('localhost', 2222))
tcp.listen(2)
PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
a = random.randint(1, 35535)
p = random.choice(PRIMES)
g = random.randint(1, 35535)
params = {'p': p, 'base': g}
conn, addr = tcp.accept()
if b"NEGOTIATION" in conn.recv(1024):
    conn.send(json.dumps(params).encode())
    print("Sending base and prime number...")
A = pow(g, a, p)
msg = conn.recv(1024)
params_received = json.loads(msg.decode())
B = params_received['B']
s = pow(B, a, p)
print("Sending my g^a mod p")
conn.send(json.dumps({'A': A}).encode())
print("The secret is %d " % s)