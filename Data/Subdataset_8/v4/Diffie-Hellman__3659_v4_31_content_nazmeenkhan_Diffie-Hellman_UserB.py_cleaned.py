import socket
import random
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = '127.0.0.1'
PORT = 5050
client_socket.connect((HOST, PORT))
q = int(client_socket.recv(1024))
alpha = int(client_socket.recv(1024))
Xb = random.randint(1, q)
Yb = pow(alpha, Xb, q)
print("Generated Public Key (Yb):", Yb)
Ya = int(client_socket.recv(1024))
client_socket.send(str(Yb).encode())
Kb = pow(Ya, Xb, q)
print("Shared Symmetric Key (Kb):", Kb)
client_socket.close()