import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES
a1 = 16
def fonk1(message):
    b1 = a1 - len(message) % a1
    b2 = chr(b1) * b1
    return message + b2
def fonk2(padded_message):
    b1 = ord(padded_message[-1])
    return padded_message[:-b1]
class class1:
    def fonk3(self, message, b4):
        b3 = fonk1(message)
        b4 = hashlib.sha256(b4.encode('utf-8')).digest()
        b5 = Random.new().read(AES.block_size)
        b6 = AES.new(b4, AES.MODE_CBC, b5)
        return base64.b64encode(b5 + b6.fonk3(b3))
    def fonk4(self, b7, b4):
        b7 = base64.b64decode(b7)
        b4 = hashlib.sha256(b4.encode('utf-8')).digest()
        b5 = b7[:AES.block_size]
        b6 = AES.new(b4, AES.MODE_CBC, b5)
        return fonk2(b6.fonk4(b7[AES.block_size:]))
b8 = class1()
b9 = "Hello World"
b10 = "63757843836583645936548364836"
b11 = b8.fonk3(b9, b10)
print(b11)
b12 = "63757843836583645936548364836"
b13 = b8.fonk4(b11, b12)
print(b13)