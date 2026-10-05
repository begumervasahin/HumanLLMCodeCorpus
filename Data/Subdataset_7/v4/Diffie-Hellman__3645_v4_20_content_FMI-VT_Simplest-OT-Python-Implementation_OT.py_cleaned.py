from Crypto.Cipher import AES
import hashlib
import random
import sys
import socket
from ecc import getcurvebyname
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
b7 = getcurvebyname("ed25519")
b8 = b7.G
b9 = random.randint(1, 2**255 - 19)
b10 = b8 * b9
b11 = [''] * 10
for i in range(10):
    b11[i] = input("Please enter something: ").ljust(32)
    print("You entered: " + str(b11[i]))
b12 = random.randint(1, 2**255 - 19)
b13 = 2 if len(sys.argv) > 1 else int(sys.argv[1])
if b13 = = 0:
    b14 = b8 * b12
else:
    b14 = (b10 * b13) + (b8 * b12)
b15 = [hashlib.blake2s() for _ in range(10)]
for i in range(10):
    b15[i].update(str((b14 + (b10 * (-i))).mul(b9)).encode())
    b15[i] = b15[i].digest()
b16 = [AES.new(key, AES.MODE_ECB) for key in b15]
b17 = [b16[i].encrypt(b11[i].encode()) for i in range(10)]
b18 = hashlib.blake2s()
b18.update(str(b10 * b12).encode())
b19 = b18.digest()
b20 = AES.new(b19, AES.MODE_ECB)
b21 = [b20.decrypt(b17[i]).decode() for i in range(10)]
print('\nBob decrypts the messages:')
for i in range(10):
    print("b21:", b21[i])