import socket
import DiffieHellman
import nacl.secret
import nacl.utils
from binascii import hexlify
def main():
    client = DiffieHellman.D_H()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 5555)
    sock.connect(server_address)
    print(f"Connected to {server_address[0]} on port {server_address[1]}")
    sock.sendall(str(client.pubKey).encode())
    data = sock.recv(9000)
    client.genKey(int(data.decode()))
    secret_key = client.getKey()
    print("Secret key:", hexlify(secret_key).decode())
    box = nacl.secret.SecretBox(secret_key)
    while True:
        message = input('Enter a message or "exit" to close the program: ')
        if message.lower() != 'exit':
            encrypted_message = box.encrypt(message.encode())
            sock.sendall(encrypted_message)
            data = sock.recv(9000)
            decrypted_message = box.decrypt(data).decode()
            print(f'Received data: "{decrypted_message}"')
        else:
            print('Closing socket.')
            sock.close()
            break
if __name__ == "__main__":
    main()