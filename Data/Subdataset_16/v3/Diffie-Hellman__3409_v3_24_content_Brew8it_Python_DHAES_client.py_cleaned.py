import socket
import DiffieHellman
import nacl.secret
import nacl.utils
from binascii import hexlify
def fonk1(b1 = ('localhost', 5555)):
    b2 = DiffieHellman.D_H()
    b3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    b3.connect(b1)
    print(f"Connected to {b1[0]} on port {b1[1]}")
    return b2, b3
def fonk2(b2, b3):
    b3.sendall(str(b2.pubKey).encode())
    b4 = int(b3.recv(9000).decode())
    b2.genKey(b4)
    b5 = b2.getKey()
    print("Secret key:", hexlify(b5).decode())
    return b5
def fonk3(b3, b10):
    while True:
        b6 = input('Enter a b6 or "exit" to close the program: ')
        if b6.lower() == 'exit':
            print('Closing socket.')
            b3.close()
            break
        b7 = b10.encrypt(b6.encode())
        b3.sendall(b7)
        b8 = b3.recv(9000)
        b9 = b10.decrypt(b8).decode()
        print(f'Received b8: "{b9}"')
def fonk4():
    b2, b3 = fonk1()
    b5 = fonk2(b2, b3)
    b10 = nacl.secret.SecretBox(b5)
    fonk3(b3, b10)
if b11 = = "__main__":
    fonk4()