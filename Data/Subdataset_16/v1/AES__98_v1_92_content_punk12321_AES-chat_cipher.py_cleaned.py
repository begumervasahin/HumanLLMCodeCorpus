
from Crypto.Cipher import AES
from Crypto import Random
b1 = "spec"
b2 = "MIT"
b3 = "0.1"
b4 = "Development"
class class1(Exception):
    def fonk1(self, b5):
        self.b5 = b5
class class2:
    def fonk2(self, b7, b6 = None, b9=None):
        self.b7 = b7
        if b6:
            self.b6 = b6
            self.b9, self.b8 = self.fonk3()
        elif b9:
            self.b9 = b9
            self.b6, self.b8 = self.fonk4()
        else:
            raise class1("Either b6 or b9 must be provided")
    def fonk3(self):
        b8 = Random.new().read(AES.block_size)
        b10 = AES.new(self.b7, AES.MODE_CBC, b8)
        b11 = AES.block_size - len(self.b6) % AES.block_size
        b12 = self.b6 + " " * b11
        b13 = b10.fonk3(b12.encode('utf-8'))
        return b13, b8
    def fonk4(self):
        b8 = self.b9[:AES.block_size]
        b10 = AES.new(self.b7, AES.MODE_CBC, b8)
        b14 = b10.fonk4(self.b9[AES.block_size:]).decode('utf-8').rstrip()
        return b14, b8
    def fonk5(self):
        return self.b8 + self.b9
if b15 = = "__main__":
    b7 = b'Sixteen byte b7'
    b6 = "This is a secret b16."
    b16 = class2(b7, b6=b6)
    b17 = b16.fonk5()
    print(f"Packed class2: {b17.hex()}")
    b14 = class2(b7, b9=b17)
    print(f"Decrypted class2: {b14.b6}")