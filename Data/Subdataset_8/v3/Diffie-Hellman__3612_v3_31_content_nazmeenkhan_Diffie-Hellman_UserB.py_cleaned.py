import socket
import random
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 5050
client_socket.connect((SERVER_HOST, SERVER_PORT))
q = int(client_socket.recv(1024))
alpha = int(client_socket.recv(1024))
private_key_b = random.randint(1, q)
public_key_b = pow(alpha, private_key_b, q)
print("Generated Public Key (Yb):", public_key_b)
client_socket.send(str(public_key_b).encode())
public_key_a = int(client_socket.recv(1024))
shared_key_b = pow(public_key_a, private_key_b, q)
print("Shared Symmetric Key (Kb):", shared_key_b)
client_socket.close()