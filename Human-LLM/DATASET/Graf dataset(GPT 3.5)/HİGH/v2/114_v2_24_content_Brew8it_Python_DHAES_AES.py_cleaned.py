from base64 import b64decode, b64encode
from Crypto import Random
from Crypto.Cipher import AES
a1 = 16
def fonk1(s):
    b1 = a1 - len(s) % a1
    return s + b1 * chr(b1)
def fonk2(s):
    return s[:-ord(s[len(s) - 1:])]
class class1:
    def fonk3(self, b2):
        self.b2 = b2.encode('utf-8')
    def fonk4(self, b3):
        b3 = fonk1(b3)
        b4 = Random.new().read(AES.block_size)
        b5 = AES.new(self.b2, AES.MODE_CBC, b4)
        return b64encode(b4 + b5.fonk4(b3))
    def fonk5(self, b6):
        b6 = b64decode(b6)
        b4 = b6[:AES.block_size]
        b5 = AES.new(self.b2, AES.MODE_CBC, b4)
        return fonk2(b5.fonk5(b6[AES.block_size:])).decode('utf-8')
if b7 = = "__main__":
    b2 = 'password'
    b8 = 'Hello, World!'
    b5 = class1(b2)
    b9 = b5.fonk4(b8)
    b10 = b5.fonk5(b9)
    print("Original b8:", b8)
    print("Encrypted:", b9)
    print("Decrypted b8:", b10)