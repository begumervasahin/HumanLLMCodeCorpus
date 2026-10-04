import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.b6.pbkdf2 import PBKDF2HMAC
import base64
class class1:
    def fonk1(self, b4, b5):
        self.b1 = os.urandom(16)
        self.b2 = os.urandom(16)
        self.b3 = self.fonk2(b4, self.b1)
        self.b4 = b4
        self.b5 = b5
    def fonk2(self, b4, b1):
        b6 = PBKDF2HMAC(
            b7 = hashes.SHA256(),
            b8 = 32,
            b1 = b1,
            b9 = 100000,
            b10 = default_backend()
        )
        return b6.derive(b4.encode())
    def fonk3(self):
        b10 = default_backend()
        b11 = Cipher(algorithms.class1(self.b3), modes.CBC(self.b2), b10=b10)
        b12 = b11.b12()
        b13 = 16 - len(self.b5) % 16
        b14 = self.b5 + (chr(b13) * b13)
        b15 = b12.update(b14.encode('utf-8')) + b12.finalize()
        self.b5 = base64.b64encode(b15).decode('utf-8')
        self.b2 = base64.b64encode(self.b2).decode('utf-8')
        self.b1 = base64.b64encode(self.b1).decode('utf-8')
    def fonk4(self, b19):
        b10 = default_backend()
        b2 = base64.b64decode(self.b2)
        b1 = base64.b64decode(self.b1)
        b3 = self.fonk2(self.b4, b1)
        b11 = Cipher(algorithms.class1(b3), modes.CBC(b2), b10=b10)
        b16 = b11.b16()
        b15 = base64.b64decode(b19)
        b14 = b16.update(b15) + b16.finalize()
        b13 = b14[-1]
        self.b5 = b14[:-b13].decode('utf-8')
if b17 = = "__main__":
    b4 = "12345678"
    b5 = "Aqui temos uma palavras com um num de caracteres multiplos de 16, para funcionar o algoritmo class1"
    b18 = class1(b4, b5)
    print("Original b5:", b18.b5)
    b18.fonk3()
    print("Encrypted b5:", b18.b5)
    print("IV:", b18.b2)
    print("Salt:", b18.b1)
    b19 = b18.b5
    b18.fonk4(b19)
    print("Decrypted b5:", b18.b5)