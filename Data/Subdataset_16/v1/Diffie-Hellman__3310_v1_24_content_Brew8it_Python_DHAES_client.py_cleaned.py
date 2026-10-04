import socket
import DiffieHellman
import nacl.secret
import nacl.utils
from binascii import hexlify
def fonk1():
    b1 = DiffieHellman.D_H()
    b2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    b3 = ('localhost', 5555)
    b2.connect(b3)
    print(f"Connected to {b3[0]} on port {b3[1]}")
    b2.sendall(str(b1.pubKey).encode())
    b4 = b2.recv(9000)
    b1.genKey(int(b4.decode()))
    b5 = b1.getKey()
    print("Secret key:", hexlify(b5).decode())
    b6 = nacl.secret.SecretBox(b5)
    while True:
        b7 = input('Enter a b7 or "exit" to close the program: ')
        if b7.lower() != 'exit':
            b8 = b6.encrypt(b7.encode())
            b2.sendall(b8)
            b4 = b2.recv(9000)
            b9 = b6.decrypt(b4).decode()
            print(f'Received b4: "{b9}"')
        else:
            print('Closing socket.')
            b2.close()
            break
if b10 = = "__main__":
    fonk1()