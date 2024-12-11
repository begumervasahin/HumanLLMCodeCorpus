import socket
from binascii import hexlify
from DiffieHellman import DiffieHellman
import nacl.secret
import nacl.utils
while True:
    b1 = DiffieHellman()
    b2 = "I have received | "
    b3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    b4 = ('localhost', 5555)
    b3.bind(b4)
    b3.listen(1)
    try:
        connection, b5 = b3.accept()
        print('Connection from IP:', b5)
        b6 = connection.recv(9000)
        connection.sendall(str(b1.public_key))
        b1.generate_key(int(b6))
        print("Secret key:", hexlify(b1.get_key()))
        b7 = nacl.secret.SecretBox(b1.get_key())
        while True:
            b8 = connection.recv(9000)
            if b8:
                b8 = b7.decrypt(b8)
                print("Received \"{}\", echoing back to client.".format(b8))
                b8 = b2 + b8
                connection.sendall(b7.encrypt(b8))
            else:
                break
    finally:
        print('Closing socket.')
        connection.close()