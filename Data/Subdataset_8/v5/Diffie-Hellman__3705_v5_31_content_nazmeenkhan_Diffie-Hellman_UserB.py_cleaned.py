import socket
import random
def generate_public_key(alpha, X):
    return pow(alpha, X, q)
def receive_int_from_server(client_socket):
    return int(client_socket.recv(1024))
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = '127.0.0.1'
PORT = 5050
client_socket.connect((HOST, PORT))
q = receive_int_from_server(client_socket)
alpha = receive_int_from_server(client_socket)
Xb = random.randint(1, q)
Yb = generate_public_key(alpha, Xb)
print("Generated Public Key (Yb):", Yb)
Ya = receive_int_from_server(client_socket)
client_socket.send(str(Yb).encode())
Kb = pow(Ya, Xb, q)
print("Shared Symmetric Key (Kb):", Kb)
client_socket.close()