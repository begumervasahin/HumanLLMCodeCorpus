from Crypto.Cipher import AES
import hashlib
import random
import sys
from ecc import getcurvebyname
import socket
b1 = "127.168.2.75"
a1 = 4446
b2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
b2.bind((b1, a1))
b2.listen(1)
print("Listening for connections.. ")
b5, b3 = b2.accept()
b4 = input("Enter b4 to be sent: ")
b5.send(b4.encode())
b5.close()
b5 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
b5.connect((b1, a1))
b6 = b5.recv(1024)
print("Message from server: " + b6.strip().decode('ascii'))
b5.close()
b2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
b2.connect((b1, a1))
b7 = [''] * 10
for i in range(10):
    b7[i] = input("Please enter something: ").ljust(32)
    print("You entered: " + str(b7[i]))
b8 = getcurvebyname("ed25519")
b9 = b8.G
b10 = random.randint(1, 2**255 - 19)
b11 = b9 * b10
b12 = b9 * random.randint(1, 2**255 - 19)
b13 = [hashlib.blake2s() for _ in range(10)]
for i in range(10):
    b13[i].update(str((b12 + b11 * (-i) * b10) * b10).encode())
    b13[i] = b13[i].digest()
b14 = [AES.new(key.digest(), AES.MODE_ECB) for key in b13]
b15 = [b14[i].encrypt(b7[i].encode()) for i in range(10)]
b16 = hashlib.blake2s()
b16.update(str(b11 * random.randint(1, 2**255 - 19)).encode())
b17 = b16.digest()
b18 = AES.new(b17, AES.MODE_ECB)
b19 = [b18.decrypt(b15[i]).decode() for i in range(10)]
print('\nBob decrypts the messages:')
for i in range(10):
    print("b19:", b19[i])