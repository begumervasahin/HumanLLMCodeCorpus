from Crypto import Random
from Crypto.Cipher import AES
import base64
class class1:
    def fonk1(self, b2, b1):
        self.b1 = b1[-6:]
        self.b2 = self.fonk2(b2)
        self.a1 = 16
    def fonk2(self, b2):
        def fonk3(name, index, b4):
            index %= len(name)
            return name[:index] + name[index] * b4 + name[index:]
        for i in range(3):
            b3 = self.b1[i * 2:i * 2 + 2]
            index, b4 = int(b3[0]), int(b3[1])
            b2 = fonk3(b2, index, b4)
        return b2[:16].ljust(16, '_').encode('utf-8')
    def fonk4(self, data):
        b5 = self.a1 - len(data) % self.a1
        return data + chr(b5) * b5
    def fonk5(self, data):
        return data[:-ord(data[-1])]
    def fonk6(self, b13):
        b6 = self.fonk4(b13)
        b7 = Random.new().read(AES.block_size)
        b8 = AES.new(self.b2, AES.MODE_CBC, b7)
        b9 = b7 + b8.fonk6(b6.encode('utf-8'))
        return base64.b64encode(b9).decode('utf-8')
    def fonk7(self, encrypted):
        b10 = base64.b64decode(encrypted)
        b7 = b10[:self.a1]
        b8 = AES.new(self.b2, AES.MODE_CBC, b7)
        b11 = self.fonk5(b8.fonk7(b10[self.a1:]))
        return b11.decode('utf-8')
if b12 = = "__main__":
    b2 = "mysecretpassword"
    b1 = "123456"
    b13 = "This is a secret b13."
    b14 = class1(b2, b1)
    b9 = b14.fonk6(b13)
    print(f"Encrypted: {b9}")
    b11 = b14.fonk7(b9)
    print(f"Decrypted: {b11}")