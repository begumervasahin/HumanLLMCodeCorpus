from base64 import b64decode, b64encode
from Crypto import Random
from Crypto.Cipher import AES
class AESCipher:
    def __init__(self, key):
        self.key = key.encode('utf-8')
    def encrypt(self, plaintext):
        padded_plaintext = self._pad(plaintext)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        ciphertext = cipher.encrypt(padded_plaintext)
        return b64encode(iv + ciphertext)
    def decrypt(self, ciphertext):
        decoded_ciphertext = b64decode(ciphertext)
        iv = decoded_ciphertext[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        decrypted_plaintext = cipher.decrypt(decoded_ciphertext[AES.block_size:])
        return self._unpad(decrypted_plaintext).decode('utf-8')
    @staticmethod
    def _pad(s):
        pad_length = AES.block_size - len(s) % AES.block_size
        return s + pad_length * chr(pad_length)
    @staticmethod
    def _unpad(s):
        return s[:-s[-1]]