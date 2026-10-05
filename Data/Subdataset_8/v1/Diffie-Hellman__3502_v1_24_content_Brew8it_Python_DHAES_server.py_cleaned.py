import socket
from binascii import hexlify
from DiffieHellman import DiffieHellman
import nacl.secret
import nacl.utils
while True:
    server = DiffieHellman()
    echoString = "I have received | "
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 5555)
    sock.bind(server_address)
    sock.listen(1)
    try:
        connection, client_address = sock.accept()
        print('Connection from IP:', client_address)
        client_pubkey = connection.recv(9000)
        connection.sendall(str(server.public_key))
        server.generate_key(int(client_pubkey))
        print("Secret key:", hexlify(server.get_key()))
        box = nacl.secret.SecretBox(server.get_key())
        while True:
            msg = connection.recv(9000)
            if msg:
                msg = box.decrypt(msg)
                print("Received \"{}\", echoing back to client.".format(msg))
                msg = echoString + msg
                connection.sendall(box.encrypt(msg))
            else:
                break
    finally:
        print('Closing socket.')
        connection.close()