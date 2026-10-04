import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends.interfaces import PBKDF2HMACBackend
import base64
class class1:
    b1 = ""
    b2 = ""
    b3 = os.urandom(32)
    b4 = ""
    b5 = ""
    def fonk1(self, b5):
        self.b1 = os.urandom(16)
        b6 = default_backend()
        self.b2 = os.urandom(16)
        b7 = Cipher(algorithms.class1(self.b3), modes.CBC(
            self.b2), b6 = b6)
        b8 = Cipher(algorithms.class1(self.b3), modes.ECB(), b6=b6)
        b9 = b8.b10()
        b10 = b7.b10()
        b11 = b9.update(bytes(self.b2)) + b9.finalize()
        b12 = b10.update(bytes(b5, 'utf8')) + b10.finalize()
        b13 = b7.b13()
        b14 = b13.update(b12) + b13.finalize()
        self.b5 = b12
        self.b2 = b11
    def fonk2(self, b12):
        b6 = default_backend()
        b8 = Cipher(algorithms.class1(self.b3), modes.ECB(), b6=b6)
        b15 = b8.b13()
        self.b2 = b15.update(self.b2) + b15.finalize()
        b7 = Cipher(algorithms.class1(self.b3), modes.CBC(
            self.b2), b6 = b6)
        b13 = b7.b13()
        b14 = b13.update(b12) + b13.finalize()
        self.b5 = str(b14)[2:-1]
b16 = class1()
b16.b5 = "Aqui temos uma palavras com um num de caracteres multiplos de 16, para funcionar o algoritmo class1"
b16.b4 = "12345678"
b16.fonk1(b16.b5)
print(str(b16.b5)[2:-1])
b16.fonk2(b16.b5)
print(b16.b5)