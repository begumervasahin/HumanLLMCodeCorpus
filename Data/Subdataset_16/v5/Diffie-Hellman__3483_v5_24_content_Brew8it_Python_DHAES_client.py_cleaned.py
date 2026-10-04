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
    b4 = str(b2.pubKey).encode()
    b3.sendall(b4)
    b5 = int(b3.recv(9000).decode())
    b2.genKey(b5)
    b6 = b2.getKey()
    print("Secret key:", hexlify(b6).decode())
    return b6
def fonk3(b3, b11):
    while True:
        b7 = input('Enter a b7 or "exit" to close the program: ')
        if b7.lower() == 'exit':
            print('Closing socket.')
            b3.close()
            break
        b8 = b11.encrypt(b7.encode())
        b3.sendall(b8)
        b9 = b3.recv(9000)
        b10 = b11.decrypt(b9).decode()
        print(f'Received b9: "{b10}"')
def fonk4():
    b2, b3 = fonk1()
    b6 = fonk2(b2, b3)
    b11 = nacl.secret.SecretBox(b6)
    fonk3(b3, b11)
if b12 = = "__main__":
    fonk4()