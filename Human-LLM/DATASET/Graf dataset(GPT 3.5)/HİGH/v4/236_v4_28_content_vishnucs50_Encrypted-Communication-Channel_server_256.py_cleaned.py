import random
import socket
from Crypto.Cipher import AES
from time import time
b1 = '127.0.0.1'
a1 = 56739
a2 = 4096
a3 = 253
b2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
b2.bind((b1, a1))
while True:
    b5, b3 = b2.recvfrom(a2)
    print("Received message:", b5.decode())
    b4 = "Hey! Got your Message"
    b2.sendto(b4.encode(), b3)
    b5 = b2.recvfrom(a2)[0]
    print("Received Diffie-Hellman parameters:", b5.decode())
    a, q, b6 = map(int, b5.decode().split())
    b7 = (a ** a3) % q
    print("Y_bob:", b7)
    b2.sendto(str(b7).encode(), b3)
    b8 = (b6 ** a3) % q
    b9 = bin(b8)[2:].zfill(32)
    b10 = class1(b9)
    b5 = b2.recvfrom(a2)[0]
    b11 = int(b10.fonk3(b5))
    print("Initial challenge received from Alice:", b11)
    b12 = random.getrandbits(32)
    b11 -= 1
    b13 = f"{b12},{b11}"
    b14 = b10.fonk2(b13)
    print("First challenge message sent:", b12, b14)
    b2.sendto(b14, b3)
    b5 = b2.recvfrom(a2)[0]
    b15 = int(b10.fonk3(b5))
    print("Final challenge received:", b15)
    if b15 = = (b12 - 1):
        print("Authentication successful")
        b16 = "authentication successful" * 6
        b17 = b10.fonk2(b16)
        b2.sendto(b17, b3)
    else:
        print("Authentication failure")
        b18 = "Authentication failure"
        b2.sendto(b18.encode(), b3)
        break
b2.close()
class class1:
    def fonk1(self, b19):
        self.b19 = b19
    def fonk2(self, message):
        b20 = message.encode('utf-8')
        b21 = AES.new(self.b19.encode('utf-8'), AES.MODE_ECB)
        return b21.fonk2(b20)
    def fonk3(self, ciphertext):
        b21 = AES.new(self.b19.encode('utf-8'), AES.MODE_ECB)
        b20 = b21.fonk3(ciphertext)
        return b20.decode('utf-8').rstrip('\x00')