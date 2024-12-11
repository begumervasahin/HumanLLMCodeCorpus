from Crypto.Util.number import getPrime
from Crypto.Cipher import AES
from random import randint
class class1:
    def fonk1(self, b1, b12, b11):
        self.b1 = b1
        self.b2 = b12
        self.b3 = b11
        self.b4 = randint(1, b11)
        self.b5 = pow(self.b2, self.b4, self.b3)
    def fonk2(self, received_public_key):
        self.b6 = hex(pow(received_public_key, self.b4, self.b3))[2:]
        while True:
            if len(self.b6) in (32, 48, 64):
                break
            elif len(self.b6) > 32:
                self.b6 = self.b6[1:]
            else:
                self.b6 = '0' + self.b6
        self.b6 = bytes.fromhex(self.b6)
        return int(self.b6.hex(), 16)
    def fonk3(self, b8):
        b7 = AES.new(self.b6)
        b8 = ''.join([hex(ord(c))[2:] for c in b8])
        while len(b8) % 32 != 0:
            b8 = '0' + b8
        b8 = bytes.fromhex(b8)
        b9 = b7.encrypt(b8)
        return int(b9.hex(), 16)
if b10 = = "__main__":
    b11 = getPrime(256)
    b12 = randint(2, b11 - 1)
    b13 = class1("Alice", b12, b11)
    b14 = class1("Bob", b12, b11)
    b15 = b13.fonk2(b14.b5)
    b16 = b14.fonk2(b13.b5)
    print("Alice's shared secret:", b15)
    print("Bob's shared secret:", b16)