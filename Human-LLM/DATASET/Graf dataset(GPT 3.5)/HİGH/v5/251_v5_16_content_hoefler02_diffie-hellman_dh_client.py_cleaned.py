from Crypto.Util.number import getPrime
from Crypto.Cipher import AES
from random import randint
class class1:
    def fonk1(self, b1, b2, b3):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = randint(1, b3)
        self.b5 = pow(self.b2, self.b4, self.b3)
    def fonk2(self, received_public_key):
        b6 = hex(pow(received_public_key, self.b4, self.b3))[2:]
        while len(b6) not in (32, 48, 64):
            if len(b6) > 32:
                b6 = b6[1:]
            else:
                b6 = '0' + b6
        self.b7 = bytes.fromhex(b6)
        return int.from_bytes(self.b7, b8 = 'big')
    def fonk3(self, msg):
        b9 = AES.new(self.b7)
        b10 = ''.join([hex(ord(c))[2:].zfill(2) for c in msg])
        while len(b10) % 32 != 0:
            b10 += '0'
        b11 = bytes.fromhex(b10)
        b12 = b9.encrypt(b11)
        return int.from_bytes(b12, b8 = 'big')