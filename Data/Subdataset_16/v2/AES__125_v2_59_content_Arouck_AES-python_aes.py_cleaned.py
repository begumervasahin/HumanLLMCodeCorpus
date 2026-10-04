import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.b6.pbkdf2 import PBKDF2HMAC
import base64
class class1:
    def fonk1(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
        self.b3 = os.urandom(16)
        self.b4 = os.urandom(16)
        self.b5 = self.fonk2(b1, self.b3)
    def fonk2(self, b1, b3):
        b6 = PBKDF2HMAC(
            b7 = hashes.SHA256(),
            b8 = 32,
            b3 = b3,
            b9 = 100000,
            b10 = default_backend()
        )
        return b6.derive(b1.encode())
    def fonk3(self):
        b11 = Cipher(algorithms.AES(self.b5), modes.CBC(self.b4), b10=default_backend())
        b12 = b11.b12()
        b13 = 16 - len(self.b2) % 16
        b14 = self.b2 + chr(b13) * b13
        b15 = b12.update(b14.encode('utf-8')) + b12.finalize()
        self.b2 = base64.b64encode(b15).decode('utf-8')
        self.b4 = base64.b64encode(self.b4).decode('utf-8')
        self.b3 = base64.b64encode(self.b3).decode('utf-8')
    def fonk4(self, b19):
        b4 = base64.b64decode(self.b4)
        b3 = base64.b64decode(self.b3)
        b5 = self.fonk2(self.b1, b3)
        b11 = Cipher(algorithms.AES(b5), modes.CBC(b4), b10=default_backend())
        b16 = b11.b16()
        b15 = base64.b64decode(b19)
        b14 = b16.update(b15) + b16.finalize()
        b13 = b14[-1]
        self.b2 = b14[:-b13].decode('utf-8')
if b17 = = "__main__":
    b1 = "12345678"
    b2 = "Aqui temos uma palavras com um num de caracteres multiplos de 16, para funcionar o algoritmo AES"
    b18 = class1(b1, b2)
    print("Original b2:", b18.b2)
    b18.fonk3()
    print("Encrypted b2:", b18.b2)
    print("IV:", b18.b4)
    print("Salt:", b18.b3)
    b19 = b18.b2
    b18.fonk4(b19)
    print("Decrypted b2:", b18.b2)