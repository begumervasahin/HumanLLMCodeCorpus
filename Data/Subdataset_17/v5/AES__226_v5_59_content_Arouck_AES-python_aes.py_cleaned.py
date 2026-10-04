import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
class AESCipher:
    def __init__(self):
        self.salt = os.urandom(16)
        self.iv = os.urandom(16)
        self.key = os.urandom(32)
        self.password = ""
        self.message = ""
    def _pad(self, message):
        padding_length = 16 - len(message) % 16
        return message + chr(padding_length) * padding_length
    def _unpad(self, padded_message):
        padding_length = padded_message[-1]
        return padded_message[:-padding_length]
    def encrypt(self, message):
        backend = default_backend()
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(self.iv), backend=backend)
        encryptor = cipher.encryptor()
        padded_message = self._pad(message)
        ct = encryptor.update(padded_message.encode('utf-8')) + encryptor.finalize()
        self.message = ct
        iv_cipher = Cipher(algorithms.AES(self.key), modes.ECB(), backend=backend)
        iv_encryptor = iv_cipher.encryptor()
        self.iv = iv_encryptor.update(self.iv) + iv_encryptor.finalize()
    def decrypt(self, ct):
        backend = default_backend()
        iv_cipher = Cipher(algorithms.AES(self.key), modes.ECB(), backend=backend)
        decryptor_iv = iv_cipher.decryptor()
        self.iv = decryptor_iv.update(self.iv) + decryptor_iv.finalize()
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(self.iv), backend=backend)
        decryptor = cipher.decryptor()
        padded_message = decryptor.update(ct) + decryptor.finalize()
        self.message = self._unpad(padded_message).decode('utf-8')
if __name__ == "__main__":
    aes_cipher = AESCipher()
    aes_cipher.password = "12345678"
    original_message = "Aqui temos uma palavras com um num de caracteres multiplos de 16, para funcionar o algoritmo AES"
    print("Original message:", original_message)
    aes_cipher.encrypt(original_message)
    encrypted_message = aes_cipher.message
    print("Encrypted message:", encrypted_message)
    print("IV:", aes_cipher.iv)
    aes_cipher.decrypt(encrypted_message)
    decrypted_message = aes_cipher.message
    print("Decrypted message:", decrypted_message)