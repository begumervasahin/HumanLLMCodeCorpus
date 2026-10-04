
from Crypto.Cipher import AES
from Crypto import Random
b1 = "spec"
b2 = "MIT"
b3 = "0.1"
b4 = "Development"
class class1(Exception):
    def fonk1(self, msg):
        super().fonk2(msg)
class class2:
    def fonk2(self, b6, b5 = None, b8=None):
        self.b6 = b6
        if b5:
            self.b5 = b5
            self.b8, self.b7 = self.fonk3()
        elif b8:
            self.b8 = b8
            self.b5, self.b7 = self.fonk4()
        else:
            raise class1("Either b5 or b8 must be provided")
    def fonk3(self):
        b7 = Random.new().read(AES.block_size)
        b9 = AES.new(self.b6, AES.MODE_CBC, b7)
        b10 = AES.block_size - len(self.b5) % AES.block_size
        b11 = self.b5 + " " * b10
        b12 = b9.encrypt(b11.encode('utf-8'))
        return b12, b7
    def fonk4(self):
        b7 = self.b8[:AES.block_size]
        b9 = AES.new(self.b6, AES.MODE_CBC, b7)
        b13 = b9.decrypt(self.b8[AES.block_size:]).decode('utf-8').rstrip()
        return b13, b7
    def fonk5(self):
        return self.b7 + self.b8
if b14 = = "__main__":
    b6 = b'Sixteen byte b6'
    b5 = "This is a secret message."
    b12 = class2(b6, b5=b5)
    b15 = b12.fonk5()
    print(f"Packed class2: {b15.hex()}")
    b13 = class2(b6, b8=b15)
    print(f"Decrypted class2: {b13.b5}")