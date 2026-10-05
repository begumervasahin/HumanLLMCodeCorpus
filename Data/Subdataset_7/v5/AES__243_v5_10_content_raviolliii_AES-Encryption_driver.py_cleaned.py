from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
class class1:
    def fonk1(self, b1):
        self.b1 = pad(b1.encode(), AES.block_size)
    def fonk2(self, plaintext):
        b2 = AES.new(self.b1, AES.MODE_CBC)
        b3 = b2.b3
        b4 = b2.fonk2(pad(plaintext.encode(), AES.block_size))
        return b3 + b4
def fonk3():
    b1 = "Thats my Kung Fu"
    b5 = "Two One Nine Two"
    b6 = class1(b1)
    b7 = b6.fonk2(b5)
    print("Message:\t", b5)
    print("Encrypted:\t", b7.hex())
if b8 = = "__main__":
    fonk3()