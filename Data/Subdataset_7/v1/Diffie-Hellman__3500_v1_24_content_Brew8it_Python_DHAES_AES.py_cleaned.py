from base64 import b64decode, b64encode
from Crypto import Random
from Crypto.Cipher import AES
a1 = 16
b1 = lambda s: s + (a1 - len(s) % a1) * chr(a1 - len(s) % a1)
b2 = lambda s: s[:-ord(s[len(s) - 1:])]
class class1:
    def fonk1(self, b3):
        self.b3 = b3.encode('utf-8')
    def fonk2(self, b4):
        b4 = b1(b4)
        b5 = Random.new().read(AES.block_size)
        b6 = AES.new(self.b3, AES.MODE_CBC, b5)
        return b64encode(b5 + b6.fonk2(b4))
    def fonk3(self, b7):
        b7 = b64decode(b7)
        b5 = b7[:AES.block_size]
        b6 = AES.new(self.b3, AES.MODE_CBC, b5)
        return b2(b6.fonk3(b7[AES.block_size:])).decode('utf-8')
if b8 = = "__main__":
    b3 = 'password'
    b9 = 'Hello, World!'
    b6 = class1(b3)
    b10 = b6.fonk2(b9)
    b11 = b6.fonk3(b10)
    print("Original b9:", b9)
    print("Encrypted:", b10)
    print("Decrypted b9:", b11)