from Crypto.Cipher import AES
import hashlib
import random
import sys
import socket
from ecc import getcurvebyname
b1 = "127.168.2.75"
a1 = 4446
def fonk1():
    b2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    b2.bind((b1, a1))
    b2.listen(1)
    print("Listening for connections.. ")
    b4, b3 = b2.accept()
    return b4
def fonk2():
    b4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    b4.connect((b1, a1))
    return b4
def fonk3(socket, data):
    socket.send(data.encode())
def fonk4(socket):
    return socket.recv(1024).strip().decode('ascii')
def fonk5(b14):
    return b14.G * random.randint(1, b14.order)
def fonk6():
    b5 = []
    for i in range(10):
        b6 = input("Please enter something: ").ljust(32)
        print("You entered: " + b6)
        b5.append(b6)
    return b5
def fonk7(b14, b17, b19, b7):
    if b7 = = 0:
        b8 = b14.G * b19
    else:
        b8 = (b17 * b7) + (b14.G * b19)
    b9 = [hashlib.blake2s() for _ in range(10)]
    for i in range(10):
        b9[i].update(str((b8 + (b17 * (-i))).mul(b16)).encode())
        b9[i] = b9[i].digest()
    return b9
def fonk8(b9, data):
    b10 = [AES.new(key, AES.MODE_ECB) for key in b9]
    b11 = [b10[i].encrypt(data[i].encode()) for i in range(10)]
    return b11
def fonk9(b17, b19):
    b12 = hashlib.blake2s()
    b12.update(str(b17 * b19).encode())
    return b12.digest()
def fonk10(b21, b11):
    b10 = AES.new(b21, AES.MODE_ECB)
    b13 = [b10.decrypt(b11[i]).decode() for i in range(10)]
    return b13
b14 = getcurvebyname("ed25519")
b15 = b14.G
b16 = random.randint(1, 2**255 - 19)
b17 = b15 * b16
b4 = fonk1()
fonk3(b4, input("Enter data to be sent: "))
b4.close()
b4 = fonk2()
b18 = fonk4(b4)
print("Message from server: " + b18)
b4.close()
b5 = fonk6()
b19 = random.randint(1, 2**255 - 19)
b7 = 2 if len(sys.argv) > 1 else int(sys.argv[1])
b20 = fonk7(b14, b17, b19, b7)
b11 = fonk8(b20, b5)
b21 = fonk9(b17, b19)
b13 = fonk10(b21, b11)
print('\nBob decrypts the messages:')
for i in range(10):
    print("message:", b13[i])