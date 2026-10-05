'''
Simple implementation of the Diffie-Hellman key exchange algorithm.
Author: Mateus-n00b
Date: September 2016
Version: 1.0
License: GPL
Note: Execute this script first!
'''
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
parameters = {'p': p, 'base': g}
conn, addr = tcp.accept()
while True:
    msg = conn.recv(1024)
    if b"NEGOTIATION" in msg:
        conn.send(json.dumps(parameters).encode())
        print("Sending base and prime number...")
        break
A = pow(g, a, p)
msg = conn.recv(1024)
params_received = json.loads(msg.decode())
B = params_received['B']
s = pow(B, a, p)
print("Sending my g^a mod p")
conn.send(json.dumps({'A': A}).encode())
print("The secret is %d" % s)