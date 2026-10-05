import socket
import os
PORT = 8998
HOST = "0.0.0.0"
def generate_key(secret_key_size=10):
    return int.from_bytes(os.urandom(secret_key_size), "big")
def steve():
    secret_key = generate_key()
    server_socket = socket.socket()
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print("Steve's server is running...")
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection established with {client_address}")
        common_key = int(client_socket.recv(1000))
        shared_key = common_key + secret_key
        client_socket.send(bytes(str(shared_key), 'utf-8'))
        state1 = int(client_socket.recv(100))
        client_socket.close()
        shared_key_with_state = state1 + secret_key
        print("Secret Key:", secret_key)
        print("Shared Key with state:", shared_key_with_state)
def do_diffie_hellman(steve_address, steves_port=PORT, secret_key_size=10):
    secret_key = generate_key()
    common_key = generate_key()
    client_socket = socket.socket()
    client_socket.connect((steve_address, steves_port))
    client_socket.send(bytes(str(common_key), 'utf-8'))
    shared_key = common_key + secret_key
    state1 = int(client_socket.recv(100))
    client_socket.send(bytes(str(shared_key), 'utf-8'))
    client_socket.close()
    shared_key_with_state = state1 + secret_key
    print("Secret Key:", secret_key)
    print("Shared Key with state:", shared_key_with_state)
if __name__ == "__main__":
    steve()