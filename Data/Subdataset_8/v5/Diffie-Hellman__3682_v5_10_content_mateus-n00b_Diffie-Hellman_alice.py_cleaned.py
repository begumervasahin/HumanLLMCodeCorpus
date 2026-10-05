import os
import json
import random
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
tcp_socket = socket(AF_INET, SOCK_STREAM)
tcp_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
tcp_socket.bind(('localhost', 2222))
tcp_socket.listen(2)
PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
private_key = random.randint(1, 35535)
prime_number = random.choice(PRIMES)
base = random.randint(1, 35535)
parameters = {'p': prime_number, 'base': base}
connection, address = tcp_socket.accept()
while True:
    message = connection.recv(1024)
    if b"NEGOTIATION" in message:
        connection.send(json.dumps(parameters).encode())
        print("Sending base and prime number...")
        break
A = pow(base, private_key, prime_number)
message = connection.recv(1024)
params_received = json.loads(message.decode())
B = params_received['B']
s = pow(B, private_key, prime_number)
print("Sending my g^a mod p")
connection.send(json.dumps({'A': A}).encode())
print("The secret is %d" % s)