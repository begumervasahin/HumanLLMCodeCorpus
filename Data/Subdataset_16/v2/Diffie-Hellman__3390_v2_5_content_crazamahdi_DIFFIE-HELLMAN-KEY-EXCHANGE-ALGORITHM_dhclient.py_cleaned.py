import random
import socket
def fonk1(b3):
    return random.randint(1, b3 - 1)
def fonk2(b4, b5, b3):
    return pow(b4, b5, b3)
def fonk3():
    b1 = 'localhost'
    b2 = int(input("Enter b2: "))
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((b1, b2))
        b3 = int(s.recv(1024).decode())
        print("Prime:", b3)
        s.send(b"Send primitive root")
        b4 = int(s.recv(1024).decode())
        print("Primitive root:", b4)
        b5 = fonk1(b3)
        print("Private component:", b5)
        b6 = fonk2(b4, b5, b3)
        print("Public component:", b6)
        s.send(str(b6).encode())
        b7 = int(s.recv(1024).decode())
        print("Server public component:", b7)
        b8 = pow(b7, b5, b3)
        print("Secret key is", b8)
if b9 = = "__main__":
    fonk3()