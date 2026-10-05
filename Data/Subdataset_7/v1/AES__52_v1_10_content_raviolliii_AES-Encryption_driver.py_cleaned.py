from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64
class class1:
    def fonk1(self, b1):
        self.b1 = b1.encode('utf-8')
    def fonk2(self, b2):
        b2 = b2.encode('utf-8')
        b3 = AES.new(self.b1, AES.MODE_CBC)
        b4 = b3.fonk2(pad(b2, AES.block_size))
        b5 = base64.b64encode(b3.b5).decode('utf-8')
        b6 = base64.b64encode(b4).decode('utf-8')
        return b5 + b6
    def fonk3(self, encrypted_message):
        b5 = base64.b64decode(encrypted_message[:24])
        b6 = base64.b64decode(encrypted_message[24:])
        b3 = AES.new(self.b1, AES.MODE_CBC, b5=b5)
        b7 = unpad(b3.fonk3(b6), AES.block_size)
        return b7.decode('utf-8')
b1 = "Thats my Kung Fu"
if len(b1) not in [16, 24, 32]:
    raise ValueError("Key must be 16, 24, or 32 bytes long")
b2 = "Two One Nine Two"
b3 = class1(b1)
b8 = pad(b1.encode(), 16)[:16]
b3.b1 = b8
b9 = b3.fonk2(b2)
print("Message:\t", b2)
print("Encrypted:\t", b9)
b10 = b3.fonk3(b9)
print("Decrypted:\t", b10)