from Crypto.Cipher import AES
import hashlib
import random
import socket
from ecc import getcurvebyname
b1 = "127.168.2.75"
a1 = 4446
def fonk1():
    b2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    b2.bind((b1, a1))
    b2.listen(1)
    print("Listening for connections.. ")
    return b2.accept()
def fonk2():
    b3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    b3.connect((b1, a1))
    return b3
def fonk3():
    b3, b4 = fonk1()
    b5 = input("Enter b5 to be sent: ")
    b3.send(b5.encode())
    b3.close()
    b3 = fonk2()
    b6 = b3.recv(1024)
    print("Message from server: " + b6.strip().decode('ascii'))
    b3.close()
def fonk4():
    b7 = getcurvebyname("ed25519")
    b8 = b7.G
    b9 = random.randint(1, 2**255 - 19)
    b10 = b8 * b9
    b11 = b8 * random.randint(1, 2**255 - 19)
    return b7, b8, b9, b10, b11
def fonk5(b7, b8, b9, b10, b11):
    b12 = [hashlib.blake2s() for b4 in range(10)]
    for i in range(10):
        b12[i].update(str((b11 + b10 * (-i) * b9) * b9).encode())
        b12[i] = b12[i].digest()
    return b12
def fonk6(b12, b19):
    b13 = [AES.new(key.digest(), AES.MODE_ECB) for key in b12]
    b14 = [b13[i].encrypt(b19[i].encode()) for i in range(10)]
    b15 = hashlib.blake2s()
    b15.update(str(b10 * random.randint(1, 2**255 - 19)).encode())
    b16 = b15.digest()
    b17 = AES.new(b16, AES.MODE_ECB)
    b18 = [b17.decrypt(b14[i]).decode() for i in range(10)]
    return b18
def fonk7():
    fonk3()
    b7, b8, b9, b10, b11 = fonk4()
    b12 = fonk5(b7, b8, b9, b10, b11)
    b19 = [''] * 10
    for i in range(10):
        b19[i] = input("Please enter something: ").ljust(32)
        print("You entered: " + str(b19[i]))
    b18 = fonk6(b12, b19)
    print('\nBob decrypts the messages:')
    for i in range(10):
        print("b18:", b18[i])
if b20 = = "__main__":
    fonk7()