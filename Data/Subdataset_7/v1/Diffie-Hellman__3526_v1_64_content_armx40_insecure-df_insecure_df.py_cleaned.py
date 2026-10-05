import socket
import os
a1 = 8998
b1 = "0.0.0.0"
def fonk1(b2 = 10):
    return int.from_bytes(os.urandom(b2), "big")
def fonk2():
    b3 = fonk1()
    b4 = None
    b5 = None
    b6 = socket.socket()
    b6.bind((b1, a1))
    b6.listen(5)
    while True:
        c, b7 = b6.accept()
        b4 = int(c.recv(1000))
        b5 = b4 + b3
        c.send(bytes(str(b5), 'utf-8'))
        b8 = int(c.recv(100))
        c.close()
        b5 = b8 + b3
        print("Secret Key:", b3)
        print("Shared Key:", b5)
def fonk3(steve, b9 = a1, b2=10):
    b3 = fonk1()
    b4 = fonk1()
    b6 = socket.socket()
    b6.connect((steve, b9))
    b6.send(bytes(str(b4), 'utf-8'))
    b5 = b4 + b3
    b8 = int(b6.recv(100))
    b6.send(bytes(str(b5), 'utf-8'))
    b5 = b8 + b3
    print("Secret Key:", b3)
    print("Shared Key:", b5)
if b10 = = "__main__":
    fonk2()