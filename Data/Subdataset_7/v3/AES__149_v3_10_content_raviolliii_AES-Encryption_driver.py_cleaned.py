from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64
class class1:
    def fonk1(self, b1):
        self.b1 = self.fonk4(b1.encode('utf-8'))
    def fonk2(self, b10):
        b2 = b10.encode('utf-8')
        b3 = AES.new(self.b1, AES.MODE_CBC)
        b4 = b3.fonk2(pad(b2, AES.block_size))
        b5 = base64.b64encode(b3.b7).decode('utf-8')
        b6 = base64.b64encode(b4).decode('utf-8')
        return b5 + b6
    def fonk3(self, b12):
        b7 = base64.b64decode(b12[:24])
        b4 = base64.b64decode(b12[24:])
        b3 = AES.new(self.b1, AES.MODE_CBC, b7)
        b8 = unpad(b3.fonk3(b4), AES.block_size)
        return b8.decode('utf-8')
    @staticmethod
    def fonk4(b1, b9 = 16):
        return pad(b1, b9)[:b9]
def fonk5():
    b1 = "Thats my Kung Fu"
    b10 = "Two One Nine Two"
    b11 = class1(b1)
    b12 = b11.fonk2(b10)
    print("Message:\t", b10)
    print("Encrypted:\t", b12)
    b13 = b11.fonk3(b12)
    print("Decrypted:\t", b13)
if b14 = = "__main__":
    fonk5()