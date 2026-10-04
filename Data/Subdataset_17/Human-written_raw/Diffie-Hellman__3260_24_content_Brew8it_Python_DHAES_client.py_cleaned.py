import socket
import DiffieHellman
import nacl.secret
import nacl.utils
from binascii import hexlify
client = DiffieHellman.D_H()
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 5555)
sock.connect(server_address)
print("Connected to %s on port %s" % server_address)
sock.sendall(str(client.pubKey))
data = sock.recv(9000)
client.genKey(int(data))
print("Secret key:", hexlify(client.getKey()))
box = nacl.secret.SecretBox(client.getKey())
while True:
    print 'Enter a msg or "exit" to close the program'
    message = raw_input()
    if message != 'exit':
        sock.sendall(box.encrypt(message))
        data = sock.recv(9000)
        data = box.decrypt(data)
        print 'Recived data: "%s"' % data
    else:
        print 'Closing socket.'
        sock.close()
        break