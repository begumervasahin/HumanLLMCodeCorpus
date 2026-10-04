import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
class class1:
    def fonk1(self):
        self.b1 = os.urandom(16)
        self.b2 = os.urandom(16)
        self.b3 = os.urandom(32)
        self.b4 = ""
        self.b5 = ""
    def fonk2(self, b5):
        b6 = 16 - len(b5) % 16
        return b5 + chr(b6) * b6
    def fonk3(self, b10):
        b6 = b10[-1]
        return b10[:-b6]
    def fonk4(self, b5):
        b7 = default_backend()
        b8 = Cipher(algorithms.AES(self.b3), modes.CBC(self.b2), b7=b7)
        b9 = b8.b9()
        b10 = self.fonk2(b5)
        b11 = b9.update(b10.encode('utf-8')) + b9.finalize()
        self.b5 = b11
        b12 = Cipher(algorithms.AES(self.b3), modes.ECB(), b7=b7)
        b13 = b12.b9()
        self.b2 = b13.update(self.b2) + b13.finalize()
    def fonk5(self, b11):
        b7 = default_backend()
        b12 = Cipher(algorithms.AES(self.b3), modes.ECB(), b7=b7)
        b14 = b12.b15()
        self.b2 = b14.update(self.b2) + b14.finalize()
        b8 = Cipher(algorithms.AES(self.b3), modes.CBC(self.b2), b7=b7)
        b15 = b8.b15()
        b10 = b15.update(b11) + b15.finalize()
        self.b5 = self.fonk3(b10).decode('utf-8')
if b16 = = "__main__":
    b17 = class1()
    b17.b4 = "12345678"
    b18 = "Aqui temos uma palavras com um num de caracteres multiplos de 16, para funcionar o algoritmo AES"
    print("Original b5:", b18)
    b17.fonk4(b18)
    b19 = b17.b5
    print("Encrypted b5:", b19)
    print("IV:", b17.b2)
    b17.fonk5(b19)
    b20 = b17.b5
    print("Decrypted b5:", b20)