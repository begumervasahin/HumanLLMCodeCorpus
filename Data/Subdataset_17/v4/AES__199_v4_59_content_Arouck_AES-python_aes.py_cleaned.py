import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
class AES:
    def __init__(self):
        self.salt = ""
        self.iv = ""
        self.key = os.urandom(32)
        self.password = ""
        self.message = ""
    def encrypt(self, message):
        self.salt = os.urandom(16)
        self.iv = os.urandom(16)
        backend = default_backend()
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(self.iv), backend=backend)
        encryptor = cipher.encryptor()
        padding_length = 16 - len(message) % 16
        padded_message = message + chr(padding_length) * padding_length
        ct = encryptor.update(padded_message.encode('utf-8')) + encryptor.finalize()
        self.message = ct
        iv_cipher = Cipher(algorithms.AES(self.key), modes.ECB(), backend=backend)
        iv_encryptor = iv_cipher.encryptor()
        ctiv = iv_encryptor.update(self.iv) + iv_encryptor.finalize()
        self.iv = ctiv
    def decrypt(self, ct):
        backend = default_backend()
        iv_cipher = Cipher(algorithms.AES(self.key), modes.ECB(), backend=backend)
        decryptor_iv = iv_cipher.decryptor()
        self.iv = decryptor_iv.update(self.iv) + decryptor_iv.finalize()
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(self.iv), backend=backend)
        decryptor = cipher.decryptor()
        padded_message = decryptor.update(ct) + decryptor.finalize()
        padding_length = padded_message[-1]
        self.message = padded_message[:-padding_length].decode('utf-8')
if __name__ == "__main__":
    aes = AES()
    aes.password = "12345678"
    original_message = "Aqui temos uma palavras com um num de caracteres multiplos de 16, para funcionar o algoritmo AES"
    print("Original message:", original_message)
    aes.encrypt(original_message)
    encrypted_message = aes.message
    print("Encrypted message:", encrypted_message)
    print("IV:", aes.iv)
    aes.decrypt(encrypted_message)
    decrypted_message = aes.message
    print("Decrypted message:", decrypted_message)