from base64 import b64decode, b64encode
from Crypto import Random
from Crypto.Cipher import AES
class class1:
    def fonk1(self, b1):
        self.b1 = b1.encode('utf-8')
    def fonk2(self, plaintext):
        b2 = self.fonk4(plaintext)
        b3 = Random.new().read(AES.block_size)
        b4 = AES.new(self.b1, AES.MODE_CBC, b3)
        b5 = b4.fonk2(b2)
        return b64encode(b3 + b5)
    def fonk3(self, b5):
        b6 = b64decode(b5)
        b3 = b6[:AES.block_size]
        b4 = AES.new(self.b1, AES.MODE_CBC, b3)
        b7 = b4.fonk3(b6[AES.block_size:])
        return self.fonk5(b7).decode('utf-8')
    @staticmethod
    def fonk4(s):
        b8 = AES.block_size - len(s) % AES.block_size
        return s + b8 * chr(b8)
    @staticmethod
    def fonk5(s):
        return s[:-s[-1]]