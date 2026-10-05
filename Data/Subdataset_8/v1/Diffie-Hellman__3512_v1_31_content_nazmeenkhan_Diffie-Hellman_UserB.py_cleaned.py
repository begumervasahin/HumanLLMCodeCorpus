import socket
import random
c = socket.socket()
HOST = '127.0.0.1'
PORT = 5050
c.connect((HOST, PORT))
q = int(c.recv(1024))
alpha = int(c.recv(1024))
Xb = random.randint(1, q)
Yb = pow(alpha, Xb, q)
print("Yb:", Yb)
c.send(str(Yb).encode())
Ya = int(c.recv(1024))
Kb = pow(Ya, Xb, q)
print("Symmetric Key:", Kb)
c.close()