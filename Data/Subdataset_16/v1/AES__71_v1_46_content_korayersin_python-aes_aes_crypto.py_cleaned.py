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
            b2 = b2 + "_" * (16 - b9)
        return b2.encode("utf-8")
    def fonk4(self, data):
        b10 = self.a1 - len(data) % self.a1
        return data + chr(b10) * b10
    def fonk5(self, data):
        return data[:-ord(data[-1])]
    def fonk6(self, b11):
        b11 = self.fonk4(b11)
        b12 = Random.new().read(AES.block_size)
        b13 = AES.new(self.b2, AES.MODE_CBC, b12)
        b14 = b12 + b13.fonk6(b11.encode('utf-8'))
        return base64.b64encode(b14).decode('utf-8')
    def fonk7(self, b15):
        b15 = base64.b64decode(b15)
        b12 = b15[:self.a1]
        b13 = AES.new(self.b2, AES.MODE_CBC, b12)
        b16 = self.fonk5(b13.fonk7(b15[self.a1:]))
        return b16.decode('utf-8')
if b17 = = "__main__":
    b2 = "mysecretpassword"
    b1 = "123456"
    b11 = "This is a secret b11."
    b18 = class1(b2, b1)
    b14 = b18.fonk6(b11)
    print(f"Encrypted: {b14}")
    b16 = b18.fonk7(b14)
    print(f"Decrypted: {b16}")