import socket
from binascii import hexlify
import DiffieHellman
import nacl.secret
import nacl.utils
while True:
    b1 = DiffieHellman.D_H()
    b2 = "I have received | "
    b3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    b4 = ('localhost',5555)
    b3.bind(b4)
    b3.listen(1)
    connection, b5 = b3.accept()
    print('Connection from IP:', b5)
    b6 = connection.recv(9000)
    connection.sendall(str(b1.pubKey))
    b1.genKey(int(b6))
    print("Secret key:", hexlify(b1.getKey()))
    b7 = nacl.secret.SecretBox(b1.getKey())
    while True:
        b8 = connection.recv(9000)
        if b8:
            b8 = b7.decrypt(b8)
            print "Reviced \"{}\", eching back to client.".format(b8)
            b8 = b2 + b8
            connection.sendall(b7.encrypt(b8))
        else:
            break
    print 'Closing socket.'
    connection.close()