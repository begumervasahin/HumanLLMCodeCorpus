import socket
import DiffieHellman
import nacl.secret
import nacl.utils
from binascii import hexlify
b1 = DiffieHellman.D_H()
b2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
b3 = ('localhost', 5555)
b2.connect(b3)
print("Connected to %s on port %s" % b3)
b2.sendall(str(b1.pubKey))
b4 = b2.recv(9000)
b1.genKey(int(b4))
print("Secret key:", hexlify(b1.getKey()))
b5 = nacl.secret.SecretBox(b1.getKey())
while True:
    print 'Enter a msg or "exit" to close the program'
    b6 = raw_input()
    if b6 != 'exit':
        b2.sendall(b5.encrypt(b6))
        b4 = b2.recv(9000)
        b4 = b5.decrypt(b4)
        print 'Recived b4: "%s"' % b4
    else:
        print 'Closing socket.'
        b2.close()
        break