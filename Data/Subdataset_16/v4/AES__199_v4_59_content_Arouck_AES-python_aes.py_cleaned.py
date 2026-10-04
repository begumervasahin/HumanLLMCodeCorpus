import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
class class1:
    def fonk1(self):
        self.b1 = ""
        self.b2 = ""
        self.b3 = os.urandom(32)
        self.b4 = ""
        self.b5 = ""
    def fonk2(self, b5):
        self.b1 = os.urandom(16)
        self.b2 = os.urandom(16)
        b6 = default_backend()
        b7 = Cipher(algorithms.class1(self.b3), modes.CBC(self.b2), b6=b6)
        b8 = b7.b8()
        b9 = 16 - len(b5) % 16
        b10 = b5 + chr(b9) * b9
        b11 = b8.update(b10.encode('utf-8')) + b8.finalize()
        self.b5 = b11
        b12 = Cipher(algorithms.class1(self.b3), modes.ECB(), b6=b6)
        b13 = b12.b8()
        b14 = b13.update(self.b2) + b13.finalize()
        self.b2 = b14
    def fonk3(self, b11):
        b6 = default_backend()
        b12 = Cipher(algorithms.class1(self.b3), modes.ECB(), b6=b6)
        b15 = b12.b16()
        self.b2 = b15.update(self.b2) + b15.finalize()
        b7 = Cipher(algorithms.class1(self.b3), modes.CBC(self.b2), b6=b6)
        b16 = b7.b16()
        b10 = b16.update(b11) + b16.finalize()
        b9 = b10[-1]
        self.b5 = b10[:-b9].decode('utf-8')
if b17 = = "__main__":
    b18 = class1()
    b18.b4 = "12345678"
    b19 = "Aqui temos uma palavras com um num de caracteres multiplos de 16, para funcionar o algoritmo class1"
    print("Original b5:", b19)
    b18.fonk2(b19)
    b20 = b18.b5
    print("Encrypted b5:", b20)
    print("IV:", b18.b2)
    b18.fonk3(b20)
    b21 = b18.b5
    print("Decrypted b5:", b21)