from Crypto import Random
from Crypto.Cipher import AES
import base64
class class1:
    def fonk1(self, b2, b1):
        self.b1 = b1[-6:]
        self.b2 = self.fonk2(b2)
        self.a1 = 16
    def fonk2(self, b2):
        def fonk3(name, index, rate):
            index %= len(name)
            b3 = name[:index]
            b4 = name[index] * rate
            b5 = name[index:]
            return b3 + b4 + b5
        for i in range(3):
            b6 = self.b1[i * 2:i * 2 + 2]
            b7 = int(b6[0])
            b8 = int(b6[1])
            b2 = fonk3(b2, b7, b8)
        b2 = (b2[:16] if len(b2) > 16 else b2.ljust(16, '_'))
        return b2.encode('utf-8')
    def fonk4(self, data):
        b9 = self.a1 - len(data) % self.a1
        return data + chr(b9) * b9
    def fonk5(self, data):
        return data[:-ord(data[-1])]
    def fonk6(self, b10):
        b10 = self.fonk4(b10)
        b11 = Random.new().read(AES.block_size)
        b12 = AES.new(self.b2, AES.MODE_CBC, b11)
        b13 = b11 + b12.fonk6(b10.encode('utf-8'))
        return base64.b64encode(b13).decode('utf-8')
    def fonk7(self, b14):
        b14 = base64.b64decode(b14)
        b11 = b14[:self.a1]
        b12 = AES.new(self.b2, AES.MODE_CBC, b11)
        b15 = self.fonk5(b12.fonk7(b14[self.a1:]))
        return b15.decode('utf-8')
if b16 = = "__main__":
    b2 = "mysecretpassword"
    b1 = "123456"
    b10 = "This is a secret b10."
    b17 = class1(b2, b1)
    b13 = b17.fonk6(b10)
    print(f"Encrypted: {b13}")
    b15 = b17.fonk7(b13)
    print(f"Decrypted: {b15}")