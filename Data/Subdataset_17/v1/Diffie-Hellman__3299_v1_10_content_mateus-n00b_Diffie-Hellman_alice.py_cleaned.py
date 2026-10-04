import os
import json
from socket import *
import random
def get_random_prime():
    PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    return random.choice(PRIMES)
tcp = socket(AF_INET, SOCK_STREAM)
tcp.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
tcp.bind(('', 2222))
tcp.listen(2)
a = random.randint(1, 35535)
p = get_random_prime()
g = random.randint(1, 35535)
TEMP = {'p': p, 'base': g}
conn, addr = tcp.accept()
while True:
    msg = conn.recv(1024).decode('utf-8')
    if "NEGOCIATION" in msg:
        conn.send(json.dumps(TEMP).encode('utf-8'))
        print("Sending base and prime number...")
        break
A = (g ** a) % p
msg = conn.recv(1024).decode('utf-8')
FOO = json.loads(msg)
B = FOO['B']
s = (B ** a) % p
print("Sending my g^a mod p")
TEMP = {'A': A}
conn.send(json.dumps(TEMP).encode('utf-8'))
print(f"The secret is {s}")
conn.close()
tcp.close()