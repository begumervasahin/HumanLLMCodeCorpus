import socket
from binascii import hexlify
from DiffieHellman import DiffieHellman
import nacl.secret
import nacl.utils
while True:
    server = DiffieHellman()
    echo_string = "I have received | "
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 5555)
    sock.bind(server_address)
    sock.listen(1)
    try:
        connection, client_address = sock.accept()
        print('Connection from IP:', client_address)
        client_pubkey = connection.recv(9000)
        connection.sendall(str(server.pubKey))
        server.genKey(int(client_pubkey))
        print("Secret key:", hexlify(server.getKey()))
        box = nacl.secret.SecretBox(server.getKey())
        while True:
            msg = connection.recv(9000)
            if msg:
                msg = box.decrypt(msg)
                print("Received \"{}\", echoing back to client.".format(msg))
                msg = echo_string + msg
                connection.sendall(box.encrypt(msg))
            else:
                break
    finally:
        print('Closing socket.')
        connection.close()