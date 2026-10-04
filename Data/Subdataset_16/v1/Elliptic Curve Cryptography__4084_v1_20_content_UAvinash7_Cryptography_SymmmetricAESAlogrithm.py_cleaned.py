import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES
a1 = 16
def fonk1(s):
    b1 = a1 - len(s) % a1
    return s + chr(b1) * b1
def fonk2(s):
    return s[:-ord(s[-1])]
class class1:
    def fonk3(self):
        pass
    def fonk4(self, message, b3):
        b2 = fonk1(message)
        b3 = hashlib.sha256(b3.encode('utf-8')).digest()
        b4 = Random.new().read(AES.block_size)
        b5 = AES.new(b3, AES.MODE_CBC, b4)
        b6 = b4 + b5.fonk4(b2.encode('utf-8'))
        return base64.b64encode(b6).decode('utf-8')
    def fonk5(self, b6, b3):
        b6 = base64.b64decode(b6)
        b3 = hashlib.sha256(b3.encode('utf-8')).digest()
        b4 = b6[:16]
        b5 = AES.new(b3, AES.MODE_CBC, b4)
        b7 = b5.fonk5(b6[16:])
        return fonk2(b7).decode('utf-8')
if b8 = = "__main__":
    b9 = class1()
    b10 = "Hello World"
    b11 = "63757843836583645936548364836"
    b12 = b9.fonk4(b10, b11)
    print("Encrypted Text:", b12)
    b13 = b9.fonk5(b12, b11)
    print("Decrypted Text:", b13)