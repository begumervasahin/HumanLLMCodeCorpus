import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES
BLOCK_SIZE = 16
def pad(message):
    padding_length = BLOCK_SIZE - len(message) % BLOCK_SIZE
    padding = chr(padding_length) * padding_length
    return message + padding
def unpad(padded_message):
    padding_length = ord(padded_message[-1])
    return padded_message[:-padding_length]
class AESAlgorithm:
    def encrypt(self, message, symmetric_key):
        raw = pad(message)
        symmetric_key = hashlib.sha256(symmetric_key.encode('utf-8')).digest()
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(symmetric_key, AES.MODE_CBC, iv)
        encrypted_message = cipher.encrypt(raw)
        return base64.b64encode(iv + encrypted_message)
    def decrypt(self, encrypted_message, symmetric_key):
        encrypted_message = base64.b64decode(encrypted_message)
        symmetric_key = hashlib.sha256(symmetric_key.encode('utf-8')).digest()
        iv = encrypted_message[:AES.block_size]
        cipher = AES.new(symmetric_key, AES.MODE_CBC, iv)
        decrypted_message = cipher.decrypt(encrypted_message[AES.block_size:])
        return unpad(decrypted_message.decode('utf-8'))
aes_algorithm = AESAlgorithm()
plain_text = "Hello World"
symmetric_key = "63757843836583645936548364836"
encrypted_text = aes_algorithm.encrypt(plain_text, symmetric_key)
print("Encrypted Text:", encrypted_text)
decrypted_text = aes_algorithm.decrypt(encrypted_text, symmetric_key)
print("Decrypted Text:", decrypted_text)