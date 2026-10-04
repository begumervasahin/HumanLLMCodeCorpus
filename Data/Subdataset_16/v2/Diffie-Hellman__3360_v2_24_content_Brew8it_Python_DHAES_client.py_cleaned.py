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
    return b1, b2
def fonk2(b1, b2):
    b2.sendall(str(b1.pubKey).encode())
    b4 = int(b2.recv(9000).decode())
    b1.genKey(b4)
    b5 = b1.getKey()
    print("Secret key:", hexlify(b5).decode())
    return b5
def fonk3(b2, b10):
    while True:
        b6 = input('Enter a b6 or "exit" to close the program: ')
        if b6.lower() == 'exit':
            print('Closing socket.')
            b2.close()
            break
        b7 = b10.encrypt(b6.encode())
        b2.sendall(b7)
        b8 = b2.recv(9000)
        b9 = b10.decrypt(b8).decode()
        print(f'Received b8: "{b9}"')
def fonk4():
    b1, b2 = fonk1()
    b5 = fonk2(b1, b2)
    b10 = nacl.secret.SecretBox(b5)
    fonk3(b2, b10)
if b11 = = "__main__":
    fonk4()