from base64 import b64decode
from base64 import b64encode
from Crypto import Random
from Crypto.Cipher import AES
a1 = 16
b1 = lambda s: s + (a1 - len(s) % a1) * \
                chr(a1 - len(s) % a1)
b2 = lambda s: s[:-ord(s[len(s) - 1:])]
class class1:
    def fonk1(self, b3):
        self.b3 = b3
    def fonk2(self, b4):
        b4 = b1(b4)
        b5 = Random.new().read(AES.block_size)
        b6 = AES.new(self.b3, AES.MODE_CBC, b5)
        return b64encode(b5 + b6.fonk2(b4))
    def fonk3(self, b7):
        b7 = b64decode(b7)
        b5 = b7[:16]
        b6 = AES.new(self.b3, AES.MODE_CBC, b5)
        return b2(b6.fonk3(b7[16:])).decode('utf8')