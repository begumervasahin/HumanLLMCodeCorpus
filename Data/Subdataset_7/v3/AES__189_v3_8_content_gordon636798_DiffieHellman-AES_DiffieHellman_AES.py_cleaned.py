import random
from Crypto.Cipher import AES
import hashlib
from gmpy2 import mpz, mpz_random, powmod, random_state
class class1:
    def fonk1(self, b1, b2, b3):
        self.b1 = b1
        self.b2 = mpz(b2)
        self.b3 = mpz(b3)
        self.fonk2()
        self.b4 = powmod(self.b2, self.b7, self.b3)
        self.b5 = {}
        print(f"{self.b1}'s master b8:", self.b7)
    def fonk2(self):
        b6 = sum([ord(i) for i in self.b1])
        self.b7 = mpz_random(random_state(b6), self.b3)
    def fonk3(self, other_user, Yb):
        b8 = powmod(Yb, self.b7, self.b3)
        b9 = b8.to_bytes((b8.bit_length() + 7)
        b10 = hashlib.sha256(b9).digest()
        print(f"\nCommon b8 for {self.b1} and {other_user.b1}:\n{b10.hex()}")
        self.b5[other_user.b1] = b10
    def fonk4(self, other_user, b18):
        b11 = self.fonk6(b18)
        b12 = AES.new(self.b5[other_user.b1], AES.MODE_CBC, 16 * b'\x00')
        b13 = b12.encrypt(b11)
        print('\nCipher text:\n' + b13.hex())
        return [b13, self.b1]
    def fonk5(self, b13):
        b18, b1 = b13[0], b13[1]
        b12 = AES.new(self.b5[b1], AES.MODE_CBC, 16 * b'\x00')
        b14 = b12.decrypt(b18)
        b14 = self.fonk7(b14)
        print(f'\nPlain text from {b1}:\n{b14}')
        return b14.decode('utf-8')
    def fonk6(self, b18):
        b15 = b18.encode('utf-8')
        b16 = 16 - len(b15) % 16
        return b15 + bytes([b16] * b16)
    def fonk7(self, b18):
        b17 = b18[-1]
        return b18[:-b17]
b2 = 11
b3 = 1040699159
b18 = 'I love ncyucsie åå»~~(â§êªâ¦)'
b19 = class1('b19', b2, b3)
b20 = class1('b20', b2, b3)
b19.fonk3(b20, b20.b4)
b20.fonk3(b19, b19.b4)
b13 = b19.fonk4(b20, b18)
b14 = b20.fonk5(b13)