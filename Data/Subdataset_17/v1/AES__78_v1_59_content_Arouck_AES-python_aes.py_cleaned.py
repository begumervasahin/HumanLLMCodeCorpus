import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
class AES:
    def __init__(self, password, message):
        self.salt = os.urandom(16)
        self.iv = os.urandom(16)
        self.key = self.generate_key(password, self.salt)
        self.password = password
        self.message = message
    def generate_key(self, password, salt):
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        return kdf.derive(password.encode())
    def encrypt(self):
        backend = default_backend()
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(self.iv), backend=backend)
        encryptor = cipher.encryptor()
        padding = 16 - len(self.message) % 16
        padded_message = self.message + (chr(padding) * padding)
        ct = encryptor.update(padded_message.encode('utf-8')) + encryptor.finalize()
        self.message = base64.b64encode(ct).decode('utf-8')
        self.iv = base64.b64encode(self.iv).decode('utf-8')
        self.salt = base64.b64encode(self.salt).decode('utf-8')
    def decrypt(self, encrypted_message):
        backend = default_backend()
        iv = base64.b64decode(self.iv)
        salt = base64.b64decode(self.salt)
        key = self.generate_key(self.password, salt)
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
        decryptor = cipher.decryptor()
        ct = base64.b64decode(encrypted_message)
        padded_message = decryptor.update(ct) + decryptor.finalize()
        padding = padded_message[-1]
        self.message = padded_message[:-padding].decode('utf-8')
if __name__ == "__main__":
    password = "12345678"
    message = "Aqui temos uma palavras com um num de caracteres multiplos de 16, para funcionar o algoritmo AES"
    aes = AES(password, message)
    print("Original message:", aes.message)
    aes.encrypt()
    print("Encrypted message:", aes.message)
    print("IV:", aes.iv)
    print("Salt:", aes.salt)
    encrypted_message = aes.message
    aes.decrypt(encrypted_message)
    print("Decrypted message:", aes.message)