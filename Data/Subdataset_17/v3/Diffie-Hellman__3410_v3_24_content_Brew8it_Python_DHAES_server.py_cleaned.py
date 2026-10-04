import socket
from binascii import hexlify
import DiffieHellman
import nacl.secret
def initialize_server(server_address=('localhost', 5555)):
    server = DiffieHellman.D_H()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(server_address)
    sock.listen(1)
    print(f"Server is listening on {server_address[0]}:{server_address[1]}")
    return server, sock
def perform_key_exchange(connection, server):
    client_pubkey = connection.recv(9000).decode()
    connection.sendall(str(server.pubKey).encode())
    server.genKey(int(client_pubkey))
    secret_key = server.getKey()
    print("Secret key:", hexlify(secret_key).decode())
    return nacl.secret.SecretBox(secret_key)
def handle_client_communication(connection, box):
    echo_string = "I have received | "
    while True:
        msg = connection.recv(9000)
        if msg:
            decrypted_msg = box.decrypt(msg).decode()
            print(f'Received "{decrypted_msg}", echoing back to client.')
            response_msg = echo_string + decrypted_msg
            connection.sendall(box.encrypt(response_msg.encode()))
        else:
            break
    print('Closing connection.')
    connection.close()
def main():
    server, sock = initialize_server()
    print('Server is waiting for a connection...')
    while True:
        connection, client_address = sock.accept()
        print('Connection from IP:', client_address)
        box = perform_key_exchange(connection, server)
        handle_client_communication(connection, box)
if __name__ == "__main__":
    main()