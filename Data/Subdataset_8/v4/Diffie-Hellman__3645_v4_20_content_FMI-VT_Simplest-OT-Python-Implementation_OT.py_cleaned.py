from Crypto.Cipher import AES
import hashlib
import random
import sys
import socket
from ecc import getcurvebyname
host = "127.168.2.75"
port = 4446
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)
print("Listening for connections.. ")
client_socket, addr = server_socket.accept()
data = input("Enter data to be sent: ")
client_socket.send(data.encode())
client_socket.close()
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))
msg = client_socket.recv(1024)
print("Message from server: " + msg.strip().decode('ascii'))
client_socket.close()
curve = getcurvebyname("ed25519")
g = curve.G
a = random.randint(1, 2**255 - 19)
Alice = g * a
var = [''] * 10
for i in range(10):
    var[i] = input("Please enter something: ").ljust(32)
    print("You entered: " + str(var[i]))
b = random.randint(1, 2**255 - 19)
c = 2 if len(sys.argv) > 1 else int(sys.argv[1])
if c == 0:
    Bob = g * b
else:
    Bob = (Alice * c) + (g * b)
k = [hashlib.blake2s() for _ in range(10)]
for i in range(10):
    k[i].update(str((Bob + (Alice * (-i))).mul(a)).encode())
    k[i] = k[i].digest()
cipher = [AES.new(key, AES.MODE_ECB) for key in k]
en = [cipher[i].encrypt(var[i].encode()) for i in range(10)]
m = hashlib.blake2s()
m.update(str(Alice * b).encode())
Bob_key = m.digest()
cipher1 = AES.new(Bob_key, AES.MODE_ECB)
message = [cipher1.decrypt(en[i]).decode() for i in range(10)]
print('\nBob decrypts the messages:')
for i in range(10):
    print("message:", message[i])