from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64
class class1:
    def fonk1(self, b1):
        self.b1 = b1.encode('utf-8')
    def fonk2(self, b8):
        b2 = b8.encode('utf-8')
        b3 = AES.new(self.b1, AES.MODE_CBC)
        b4 = b3.fonk2(pad(b2, AES.block_size))
        b5 = base64.b64encode(b3.b5).decode('utf-8')
        b6 = base64.b64encode(b4).decode('utf-8')
        return b5 + b6
    def fonk3(self, b10):
        b5 = base64.b64decode(b10[:24])
        b6 = base64.b64decode(b10[24:])
        b3 = AES.new(self.b1, AES.MODE_CBC, b5=b5)
        b7 = unpad(b3.fonk3(b6), AES.block_size)
        return b7.decode('utf-8')
b1 = "Thats my Kung Fu"
b8 = "Two One Nine Two"
b1 = pad(b1.encode(), 16)[:16]
b9 = class1(b1)
b10 = b9.fonk2(b8)
print("Message:\t", b8)
print("Encrypted:\t", b10)
b11 = b9.fonk3(b10)
print("Decrypted:\t", b11)