import socket
import os
a1 = 8998
b1 = "0.0.0.0"
def fonk1(b2 = 10):
    return int.from_bytes(os.urandom(b2), "big")
def fonk2():
    b3 = fonk1()
    b4 = socket.socket()
    b4.bind((b1, a1))
    b4.listen(5)
    print("Steve's server is running...")
    while True:
        b11, b5 = b4.accept()
        print(f"Connection established with {b5}")
        b6 = int(b11.recv(1000))
        b7 = b6 + b3
        b11.send(bytes(str(b7), 'utf-8'))
        b8 = int(b11.recv(100))
        b11.close()
        b9 = b8 + b3
        print("Secret Key:", b3)
        print("Shared Key with state:", b9)
def fonk3(steve_address, b10 = a1, b2=10):
    b3 = fonk1()
    b6 = fonk1()
    b11 = socket.socket()
    b11.connect((steve_address, b10))
    b11.send(bytes(str(b6), 'utf-8'))
    b7 = b6 + b3
    b8 = int(b11.recv(100))
    b11.send(bytes(str(b7), 'utf-8'))
    b11.close()
    b9 = b8 + b3
    print("Secret Key:", b3)
    print("Shared Key with state:", b9)
if b12 = = "__main__":
    fonk2()