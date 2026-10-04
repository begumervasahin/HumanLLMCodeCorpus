import socket
from binascii import hexlify
import DiffieHellman
import nacl.secret
def initialize_server(server_address=('localhost', 5555)):
    server = DiffieHellman.D_H()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(server_address)
    sock.listen(1)
    return server, sock
def handle_client_connection(connection, server):
    echo_string = "I have received | "
    client_pubkey = connection.recv(9000)
    connection.sendall(str(server.pubKey).encode())
    server.genKey(int(client_pubkey.decode()))
    secret_key = server.getKey()
    print("Secret key:", hexlify(secret_key).decode())
    box = nacl.secret.SecretBox(secret_key)
    while True:
        msg = connection.recv(9000)
        if msg:
            decrypted_msg = box.decrypt(msg).decode()
            print(f'Received "{decrypted_msg}", echoing back to client.')
            response_msg = echo_string + decrypted_msg
            connection.sendall(box.encrypt(response_msg.encode()))
        else:
            break
    print('Closing socket.')
    connection.close()
def main():
    while True:
        server, sock = initialize_server()
        print('Server is waiting for a connection...')
        connection, client_address = sock.accept()
        print('Connection from IP:', client_address)
        handle_client_connection(connection, server)
if __name__ == "__main__":
    main()