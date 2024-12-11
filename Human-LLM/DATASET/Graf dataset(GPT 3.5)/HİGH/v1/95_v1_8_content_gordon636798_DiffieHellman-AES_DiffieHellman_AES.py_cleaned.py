import random
from Crypto.Cipher import AES
import hashlib
from gmpy2 import mpz, mpz_random, powmod, random_state
class class1:
    def fonk1(self, b1, b2, b3):
        self.b1 = b1
        self.b2 = mpz(b2)
        self.b3 = mpz(b3)
        b4 = sum([ord(i) for i in b1])
        self.b5 = mpz_random(random_state(b4), b3)
        self.b6 = powmod(self.b2, self.b5, self.b3)
        self.b7 = {}
        print(self.b1 + '\'s master b8:', self.b5)
    def fonk2(self, other_user, Yb):
        b8 = powmod(Yb, self.b5, self.b3)
        b8 = int(b8).to_bytes(len(b8)
        b8 = hashlib.sha256(b8).digest()
        print('\nCommon b8 for ' + self.b1 + ' and ' + other_user.b1 + ':\n' + b8.hex())
        self.b7[other_user.b1] = b8
    def fonk3(self, other_user, b9):
        b9 = b9.encode('utf-8')
        b10 = 16 - len(b9) % 16
        if b10 = = 0:
            b10 = 16
        b11 = bytes([b10])
        b9 += b10 * b11
        b12 = AES.new(self.b7[other_user.b1], AES.MODE_CBC, 16 * b'\x00')
        b13 = b12.encrypt(b9)
        print('\nCipher:\n' + b13.hex())
        return [b13, self.b1]
    def fonk4(self, b13):
        b9, b1 = b13[0], b13[1]
        b12 = AES.new(self.b7[b1], AES.MODE_CBC, 16 * b'\x00')
        b14 = b12.decrypt(b9)
        b14 = b14[:-(b14[-1])]
        b14 = b14.decode('utf-8')
        print('\nPlain from ' + b1 + ':\n' + b14)
        return b14
b2 = 11
b3 = 1040699159
b9 = 'I love ncyucsie åå»~~(â§êªâ¦)'
b15 = class1('b15', b2, b3)
b16 = class1('b16', b2, b3)
b15.fonk2(b16, b16.b6)
b16.fonk2(b15, b15.b6)
b13 = b15.fonk3(b16, b9)
b14 = b16.fonk4(b13)