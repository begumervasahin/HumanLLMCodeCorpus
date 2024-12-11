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
        print(f"{self.b1}'s master b8:", self.b5)
    def fonk2(self, other_user, Yb):
        b8 = powmod(Yb, self.b5, self.b3)
        b9 = b8.to_bytes((b8.bit_length() + 7)
        b10 = hashlib.sha256(b9).digest()
        print(f"\nCommon b8 for {self.b1} and {other_user.b1}:\n{b10.hex()}")
        self.b7[other_user.b1] = b10
    def fonk3(self, other_user, b11):
        b11 = b11.encode('utf-8')
        b12 = 16 - len(b11) % 16
        if b12 = = 0:
            b12 = 16
        b13 = bytes([b12])
        b11 += b12 * b13
        b14 = AES.new(self.b7[other_user.b1], AES.MODE_CBC, 16 * b'\x00')
        b15 = b14.encrypt(b11)
        print('\nCipher text:\n' + b15.hex())
        return [b15, self.b1]
    def fonk4(self, b15):
        b11, b1 = b15[0], b15[1]
        b14 = AES.new(self.b7[b1], AES.MODE_CBC, 16 * b'\x00')
        b16 = b14.decrypt(b11)
        b16 = b16[:-(b16[-1])]
        b16 = b16.decode('utf-8')
        print(f'\nPlain text from {b1}:\n{b16}')
        return b16
b2 = 11
b3 = 1040699159
b11 = 'I love ncyucsie åå»~~(â§êªâ¦)'
b17 = class1('b17', b2, b3)
b18 = class1('b18', b2, b3)
b17.fonk2(b18, b18.b6)
b18.fonk2(b17, b17.b6)
b15 = b17.fonk3(b18, b11)
b16 = b18.fonk4(b15)