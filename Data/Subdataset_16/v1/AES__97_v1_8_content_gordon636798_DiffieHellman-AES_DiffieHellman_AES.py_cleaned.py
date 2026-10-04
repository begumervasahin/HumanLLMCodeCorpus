import random
from gmpy2 import mpz, mpz_random, powmod, random_state
from Crypto.Cipher import AES
import hashlib
class class1:
    def fonk1(self, b1, b2, b3):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        b4 = sum([ord(i) for i in b1])
        self.b5 = mpz_random(random_state(b4), b3)
        self.b6 = powmod(self.b2, self.b5, self.b3)
        self.b7 = {}
        print(f"{self.b1}'s master b8: {self.b5}")
    def fonk2(self, other_user, Yb):
        b8 = powmod(Yb, self.b5, self.b3)
        b8 = int(b8).to_bytes((b8.bit_length() + 7)
        b8 = hashlib.sha256(b8).digest()
        print(f"\nCommon b8 for {self.b1} and {other_user.b1}: \n{b8.hex()}")
        self.b7[other_user.b1] = b8
    def fonk3(self, other_user, b9):
        b9 = b9.encode('utf-8')
        b10 = 16 - len(b9) % 16
        b9 += bytes([b10] * b10)
        b11 = AES.new(self.b7[other_user.b1], AES.MODE_CBC, b'\x00' * 16)
        b12 = b11.encrypt(b9)
        print(f"\ncipher: \n{b12.hex()}")
        return [b12, self.b1]
    def fonk4(self, b12):
        b9, b1 = b12
        b11 = AES.new(self.b7[b1], AES.MODE_CBC, b'\x00' * 16)
        b13 = b11.decrypt(b9)
        b13 = b13[:-b13[-1]]
        b13 = b13.decode('utf-8')
        print(f"\nplain from {b1}: \n{b13}")
        return b13
def fonk5():
    b2 = mpz(11)
    b3 = mpz(1040699159)
    print(f'b2: {b2}, b3: {b3}')
    b9 = 'I love ncyucsie åå»~~(â§êªâ¦)'
    print(f'Plain: {b9}\n')
    b14 = class1('Alice', b2, b3)
    b15 = class1('Bob', b2, b3)
    b14.fonk2(b15, b15.b6)
    b15.fonk2(b14, b14.b6)
    b16 = b14.fonk3(b15, b9)
    b17 = b15.fonk4(b16)
if b18 = = "__main__":
    fonk5()