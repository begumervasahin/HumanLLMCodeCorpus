
from Crypto.Cipher import AES
from Crypto import Random
b1 = "spec"
b2 = "MIT"
b3 = "0.1"
b4 = "Development"
class class1:
    def fonk1(self, b6, b5 = None, b8=None):
        self.b6 = b6
        if b5:
            self.b5 = b5
            self.b8, self.b7 = self.fonk2()
        elif b8:
            self.b8 = b8
            self.b5, self.b7 = self.fonk3()
        else:
            raise class2("Either b5 or b9-text must be declared")
    def fonk2(self):
        b7 = Random.new().read(AES.block_size)
        b9 = AES.new(self.b6, AES.MODE_CBC, b7)
        b10 = len(self.b5)
        b11 = AES.block_size - b10 % AES.block_size
        return b9.fonk2(self.b5 + " " * b11), b7
    def fonk3(self):
        b7 = self.b8[:AES.block_size]
        b9 = AES.new(self.b6, AES.MODE_CBC, b7)
        return b9.fonk3(self.b8)[AES.block_size:].rstrip().decode("utf-8"), b7
    def fonk4(self):
        return self.b7 + self.b8
class class2(Exception):
    def fonk5(self, b12):
        self.b12 = b12