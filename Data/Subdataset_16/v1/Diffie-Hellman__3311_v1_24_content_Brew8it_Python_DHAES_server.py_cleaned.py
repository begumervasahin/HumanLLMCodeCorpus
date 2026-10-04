import socket
from binascii import hexlify
import DiffieHellman
import nacl.secret
def fonk1(b1 = ('localhost', 5555)):
    b2 = DiffieHellman.D_H()
    b3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    b3.bind(b1)
    b3.listen(1)
    return b2, b3
def fonk2(connection, b2):
    b4 = "I have received | "
    b5 = connection.recv(9000)
    connection.sendall(str(b2.pubKey).encode())
    b2.genKey(int(b5.decode()))
    b6 = b2.getKey()
    print("Secret key:", hexlify(b6).decode())
    b7 = nacl.secret.SecretBox(b6)
    while True:
        b8 = connection.recv(9000)
        if b8:
            b9 = b7.decrypt(b8).decode()
            print(f'Received "{b9}", echoing back to client.')
            b10 = b4 + b9
            connection.sendall(b7.encrypt(b10.encode()))
        else:
            break
    print('Closing socket.')
    connection.close()
def fonk3():
    while True:
        b2, b3 = fonk1()
        print('Server is waiting for a connection...')
        connection, b11 = b3.accept()
        print('Connection from IP:', b11)
        fonk2(connection, b2)
if b12 = = "__main__":
    fonk3()