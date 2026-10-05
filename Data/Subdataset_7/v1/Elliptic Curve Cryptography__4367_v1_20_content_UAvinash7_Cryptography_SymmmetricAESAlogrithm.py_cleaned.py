import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES
a1 = 16
b1 = lambda s: s + (a1 - len(s) % a1) * chr(a1 - len(s) % a1)
b2 = lambda s: s[0:-ord(s[-1])]
class class1:
    def fonk1(self, message, b4):
        b3 = b1(message)
        b4 = hashlib.sha256(b4.encode('utf-8')).digest()
        b5 = Random.new().read(AES.block_size)
        b6 = AES.new(b4, AES.MODE_CBC, b5)
        return base64.b64encode(b5 + b6.fonk1(b3))
    def fonk2(self, b7, b4):
        b7 = base64.b64decode(b7)
        b4 = hashlib.sha256(b4.encode('utf-8')).digest()
        b5 = b7[:16]
        b6 = AES.new(b4, AES.MODE_CBC, b5)
        return b2(b6.fonk2(b7[16:]))
b8 = class1()
b9 = "Hello World"
b10 = "63757843836583645936548364836"
b11 = b8.fonk1(b9, b10)
print("Encrypted Text:", b11.decode())
b12 = "63757843836583645936548364836"
b13 = b8.fonk2(b11, b12)
print("Decrypted Text:", b13.decode())