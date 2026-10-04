import socket
import DiffieHellman
import nacl.secret
import nacl.utils
from binascii import hexlify
def initialize_client():
    client = DiffieHellman.D_H()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 5555)
    sock.connect(server_address)
    print(f"Connected to {server_address[0]} on port {server_address[1]}")
    return client, sock
def exchange_keys(client, sock):
    sock.sendall(str(client.pubKey).encode())
    server_pub_key = int(sock.recv(9000).decode())
    client.genKey(server_pub_key)
    secret_key = client.getKey()
    print("Secret key:", hexlify(secret_key).decode())
    return secret_key
def communicate(sock, box):
    while True:
        message = input('Enter a message or "exit" to close the program: ')
        if message.lower() == 'exit':
            print('Closing socket.')
            sock.close()
            break
        encrypted_message = box.encrypt(message.encode())
        sock.sendall(encrypted_message)
        data = sock.recv(9000)
        decrypted_message = box.decrypt(data).decode()
        print(f'Received data: "{decrypted_message}"')
def main():
    client, sock = initialize_client()
    secret_key = exchange_keys(client, sock)
    box = nacl.secret.SecretBox(secret_key)
    communicate(sock, box)
if __name__ == "__main__":
    main()