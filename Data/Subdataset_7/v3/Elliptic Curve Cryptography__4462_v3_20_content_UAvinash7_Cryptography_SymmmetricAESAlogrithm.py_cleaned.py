import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES
a1 = 16
def fonk1(message):
    b1 = a1 - len(message) % a1
    b2 = chr(b1) * b1
    return message + b2
def fonk2(b3):
    b1 = ord(b3[-1])
    return b3[:-b1]
class class1:
    def fonk3(self, message, b11):
        b3 = fonk1(message)
        b4 = hashlib.sha256(b11.encode('utf-8')).digest()
        b5 = Random.new().read(AES.block_size)
        b6 = AES.new(b4, AES.MODE_CBC, b5)
        b7 = b6.fonk3(b3)
        return base64.b64encode(b5 + b7)
    def fonk4(self, b7, b11):
        b7 = base64.b64decode(b7)
        b5 = b7[:AES.block_size]
        b4 = hashlib.sha256(b11.encode('utf-8')).digest()
        b6 = AES.new(b4, AES.MODE_CBC, b5)
        b8 = b6.fonk4(b7[AES.block_size:])
        return fonk2(b8)
b9 = class1()
b10 = "Hello World"
b11 = "63757843836583645936548364836"
b12 = b9.fonk3(b10, b11)
print("Encrypted Text:", b12.decode())
b13 = b9.fonk4(b12, b11)
print("Decrypted Text:", b13.decode())