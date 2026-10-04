import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends.interfaces import PBKDF2HMACBackend
import base64
class AES:
    salt = ""
    iv = ""
    key = os.urandom(32)
    password = ""
    message = ""
    def encrypt(self, message):
        self.salt = os.urandom(16)
        backend = default_backend()
        self.iv = os.urandom(16)
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(
            self.iv), backend=backend)
        iv_cipher = Cipher(algorithms.AES(self.key), modes.ECB(), backend=backend)
        iv_encryptor = iv_cipher.encryptor()
        encryptor = cipher.encryptor()
        ctiv = iv_encryptor.update(bytes(self.iv)) + iv_encryptor.finalize()
        ct = encryptor.update(bytes(message, 'utf8')) + encryptor.finalize()
        decryptor = cipher.decryptor()
        msg = decryptor.update(ct) + decryptor.finalize()
        self.message = ct
        self.iv = ctiv
    def decrypt(self, ct):
        backend = default_backend()
        iv_cipher = Cipher(algorithms.AES(self.key), modes.ECB(), backend=backend)
        decryptor_iv = iv_cipher.decryptor()
        self.iv = decryptor_iv.update(self.iv) + decryptor_iv.finalize()
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(
            self.iv), backend=backend)
        decryptor = cipher.decryptor()
        msg = decryptor.update(ct) + decryptor.finalize()
        self.message = str(msg)[2:-1]
aes = AES()
aes.message = "Aqui temos uma palavras com um num de caracteres multiplos de 16, para funcionar o algoritmo AES"
aes.password = "12345678"
aes.encrypt(aes.message)
print(str(aes.message)[2:-1])
aes.decrypt(aes.message)
print(aes.message)