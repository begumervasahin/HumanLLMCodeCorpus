
import random
from gmpy2 import mpz, mpz_random, powmod, random_state
from Crypto.Cipher import AES
import hashlib
class class1:
    def fonk1(self, b1, b2, b3):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        b4 = sum(ord(char) for char in b1)
        self.b5 = mpz_random(random_state(b4), b3)
        self.b6 = powmod(self.b2, self.b5, self.b3)
        self.b7 = {}
        print(f"{self.b1}'s master key: {self.b5}")
    def fonk2(self, other_user):
        b8 = powmod(other_user.b6, self.b5, self.b3)
        b9 = int(b8).to_bytes((b8.bit_length() + 7)
        b10 = hashlib.sha256(b9).digest()
        self.b7[other_user.b1] = b10
        print(f"\nCommon key for {self.b1} and {other_user.b1}: \n{b10.hex()}")
    def fonk3(self, other_user, b16):
        b11 = b16.encode('utf-8')
        b12 = 16 - len(b11) % 16
        b11 += bytes([b12] * b12)
        b13 = AES.new(self.b7[other_user.b1], AES.MODE_CBC, b'\x00' * 16)
        b14 = b13.encrypt(b11)
        print(f"\nCiphertext: \n{b14.hex()}")
        return b14, self.b1
    def fonk4(self, b14):
        b11, b15 = b14
        b13 = AES.new(self.b7[b15], AES.MODE_CBC, b'\x00' * 16)
        b16 = b13.decrypt(b11)
        b12 = b16[-1]
        b16 = b16[:-b12].decode('utf-8')
        print(f"\nPlaintext from {b15}: \n{b16}")
        return b16
def fonk5():
    b2 = mpz(11)
    b3 = mpz(1040699159)
    print(f'b2: {b2}, b3: {b3}')
    b16 = 'I love ncyucsie åå»~~(â§êªâ¦)'
    print(f'Plaintext: {b16}\n')
    b17 = class1('Alice', b2, b3)
    b18 = class1('Bob', b2, b3)
    b17.fonk2(b18)
    b18.fonk2(b17)
    b19 = b17.fonk3(b18, b16)
    b20 = b18.fonk4(b19)
if b21 = = "__main__":
    fonk5()