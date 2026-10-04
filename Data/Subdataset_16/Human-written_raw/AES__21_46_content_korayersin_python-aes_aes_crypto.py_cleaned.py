from Crypto import Random
from Crypto.Cipher import AES
import base64
class class1:
    def fonk1(self, b2, b1):
        self.b1 = b1[-6:]
        self.b2 = self.fonk2(b2)
        self.a1 = 16
    def fonk2(self, b2):
        def fonk3(name, b3, rate):
            while len(name) - 1 < b3:
                b3 = b3 - len(name)
            b4 = name[:b3]
            b5 = ""
            for iw in range(rate):
                b5 += name[b3]
            b4 = b4 + b5 + name[b3:]
            return b4
        for i in range(3):
            b6 = self.b1[i * 2:i * 2 + 2]
            b7 = int(b6[:1])
            b8 = int(b6[1:])
            b2 = fonk3(b2, b7, b8)
        b9 = len(b2)
        if b9 > 16:
            b2 = b2[:16]
        elif b9 < 16:
            for i in range(16 - b9):
                b2 = b2 + "_"
        return b2
    def fonk4(self, data):
        return data + (self.a1 - len(data) % self.a1) * chr(
            self.a1 - len(data) % self.a1)
    def fonk5(self, data):
        return data[:-ord(data[len(data) - 1:])]
    def fonk6(self, b10):
        b10 = self.fonk4(b10)
        b11 = Random.new().read(AES.block_size)
        b12 = AES.new(self.b2, AES.MODE_CBC, b11)
        return base64.b64encode(b11 + b12.fonk6(b10))
    def fonk7(self, b14):
        b13 = self.b2.encode("utf-8")
        b14 = base64.b64decode(b14)
        b15 = b14[:self.a1]
        b16 = AES.new(b13, AES.MODE_CBC, b15)
        return self.fonk5(b16.fonk7(b14[self.a1:])).decode("utf-8")