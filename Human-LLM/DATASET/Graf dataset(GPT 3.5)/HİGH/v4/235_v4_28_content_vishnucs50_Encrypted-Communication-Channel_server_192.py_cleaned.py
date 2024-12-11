import random
from Crypto.Cipher import AES
import socket
from time import time
b1 = '127.0.0.1'
a1 = 56739
a2 = 4096
a3 = 253
b2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
b2.bind((b1, a1))
def fonk1():
    data, b3 = b2.recvfrom(a2)
    print("The b13 is:", data)
    return data, b3
def fonk2(b18, b16, b15):
    b4 = pow(b15, b18, b16)
    return b4
def fonk3(b18, b16, b17):
    b5 = pow(b17, b18, b16)
    return bin(b5)[2:].zfill(24)
class class1:
    def fonk4(self, b6):
        self.b6 = b6
    def fonk5(self, b13):
        if len(b13) % b7 = = 0:
            b8 = b13.encode('utf-8')
        else:
            b9 = len(b13)
            b8 = (b13 + ((b7 - b9 % b7) * str(0)))
            b8 = b8.encode('utf-8')
        b10 = AES.new(self.b6, AES.MODE_ECB)
        b11 = b10.fonk5(b8)
        return b11
    def fonk6(self, b11):
        b12 = AES.new(self.b6, AES.MODE_ECB)
        b8 = b12.fonk6(b11)
        b8 = b8.decode('utf-8')
        b8 = b8.rstrip('0')
        return b8
def fonk7():
    return random.getrandbits(32)
while True:
    data, b3 = fonk1()
    b13 = "Hey! Got your Message"
    b2.sendto(b13.encode(), b3)
    data, b3 = fonk1()
    b14 = data.decode()
    b15 = int(b14[0])
    b16 = int(b14[2:7])
    b17 = int(b14[8:12])
    b18 = random.randint(1, b16 - 1)
    b4 = fonk2(b18, b16, b15)
    b2.sendto(str(b4).encode(), b3)
    b19 = fonk3(b18, b16, b17)
    data, b3 = fonk1()
    b20 = int(class1(b19).fonk6(data))
    b21 = fonk7()
    b22 = b21 - 1
    b23 = f"{b21},{b22}"
    b24 = class1(b19).fonk5(b23)
    b2.sendto(b24, b3)
    data, b3 = fonk1()
    b25 = int(class1(b19).fonk6(data))
    if b25 = = (b21 - 1):
        b13 = "authentication successful" * 6
        b24 = class1(b19).fonk5(b13)
        b26 = time()
        print("The duration of AES 192 encryption:", b26 - start)
        b2.sendto(b24, b3)
    else:
        b13 = "Authentication failure"
        b2.sendto(b13.encode(), b3)
        break
b2.close()