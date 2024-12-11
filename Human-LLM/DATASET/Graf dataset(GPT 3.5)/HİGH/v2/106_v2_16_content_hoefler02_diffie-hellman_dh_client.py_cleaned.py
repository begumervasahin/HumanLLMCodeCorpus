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
        return int(self.b7.hex(), 16)
    def fonk3(self, msg):
        b8 = AES.new(self.b7)
        b9 = ''.join([hex(ord(c))[2:] for c in msg])
        while len(b9) % 32 != 0:
            b9 = '0' + b9
        b10 = bytes.fromhex(b9)
        b11 = b8.encrypt(b10)
        return int(b11.hex(), 16)
if b12 = = "__main__":
    b3 = getPrime(256)
    b2 = randint(2, b3 - 1)
    b13 = class1("Alice", b2, b3)
    b14 = class1("Bob", b2, b3)
    b15 = b13.fonk2(b14.b5)
    b16 = b14.fonk2(b13.b5)
    print("Alice's shared secret:", b15)
    print("Bob's shared secret:", b16)