import socket
from binascii import hexlify
import DiffieHellman
import nacl.secret
def fonk1(b1 = ('localhost', 5555)):
    b2 = DiffieHellman.D_H()
    b3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    b3.bind(b1)
    b3.listen(1)
    print(f"Server is listening on {b1[0]}:{b1[1]}")
    return b2, b3
def fonk2(connection, b2):
    b4 = connection.recv(9000).decode()
    connection.sendall(str(b2.pubKey).encode())
    b2.genKey(int(b4))
    b5 = b2.getKey()
    print("Secret key:", hexlify(b5).decode())
    return nacl.secret.SecretBox(b5)
def fonk3(connection, b11):
    b6 = "I have received | "
    while True:
        b7 = connection.recv(9000)
        if b7:
            b8 = b11.decrypt(b7).decode()
            print(f'Received "{b8}", echoing back to client.')
            b9 = b6 + b8
            connection.sendall(b11.encrypt(b9.encode()))
        else:
            break
    print('Closing connection.')
    connection.close()
def fonk4():
    b2, b3 = fonk1()
    print('Server is waiting for a connection...')
    while True:
        connection, b10 = b3.accept()
        print('Connection from IP:', b10)
        b11 = fonk2(connection, b2)
        fonk3(connection, b11)
if b12 = = "__main__":
    fonk4()