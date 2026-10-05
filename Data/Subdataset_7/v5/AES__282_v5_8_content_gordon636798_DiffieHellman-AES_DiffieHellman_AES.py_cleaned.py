import random
from gmpy2 import mpz, mpz_random, powmod, random_state
from Crypto.Cipher import AES
import hashlib
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
        b6 = sum(ord(char) for char in self.b1)
        self.b7 = mpz_random(random_state(b6), self.b3)
    def fonk3(self, other_user, Yb):
        b8 = powmod(Yb, self.b7, self.b3)
        b9 = b8.to_bytes((b8.bit_length() + 7)
        b10 = hashlib.sha256(b9).digest()
        print(f"\nCommon b8 for {self.b1} and {other_user.b1}:\n{b10.hex()}")
        self.b5[other_user.b1] = b10
    def fonk4(self, other_user, b17):
        b11 = b17.encode('utf-8')
        b12 = 16 - len(b11) % 16
        b12 = b12 if b12 != 0 else 16
        b13 = bytes([b12])
        b11 += b12 * b13
        b14 = AES.new(self.b5[other_user.b1], AES.MODE_CBC, 16 * b'\x00')
        b15 = b14.encrypt(b11)
        print('\nCipher text:\n' + b15.hex())
        return [b15, self.b1]
    def fonk5(self, b15):
        b17, b1 = b15[0], b15[1]
        b14 = AES.new(self.b5[b1], AES.MODE_CBC, 16 * b'\x00')
        b16 = b14.decrypt(b17)
        b16 = b16[:-(b16[-1])]
        b16 = b16.decode('utf-8')
        print(f'\nPlain text from {b1}:\n{b16}')
        return b16
b2 = 11
b3 = 1040699159
b17 = 'I love ncyucsie åå»~~(â§êªâ¦)'
b18 = class1('b18', b2, b3)
b19 = class1('b19', b2, b3)
b18.fonk3(b19, b19.b4)
b19.fonk3(b18, b18.b4)
b15 = b18.fonk4(b19, b17)
b16 = b19.fonk5(b15)