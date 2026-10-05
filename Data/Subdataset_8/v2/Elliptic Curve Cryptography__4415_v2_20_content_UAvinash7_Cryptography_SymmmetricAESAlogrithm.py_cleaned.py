import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES
BLOCK_SIZE = 16
def pad_message(message):
    padding_length = BLOCK_SIZE - len(message) % BLOCK_SIZE
    padding = chr(padding_length) * padding_length
    return message + padding
def unpad_message(padded_message):
    padding_length = ord(padded_message[-1])
    return padded_message[:-padding_length]
class AESAlgorithm:
    def __init__(self):
        pass
    def encrypt(self, message, symmetric_key):
        padded_message = pad_message(message)
        hashed_key = hashlib.sha256(symmetric_key.encode('utf-8')).digest()
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(hashed_key, AES.MODE_CBC, iv)
        encrypted_message = cipher.encrypt(padded_message)
        return base64.b64encode(iv + encrypted_message)
    def decrypt(self, encrypted_message, symmetric_key):
        encrypted_message = base64.b64decode(encrypted_message)
        iv = encrypted_message[:AES.block_size]
        hashed_key = hashlib.sha256(symmetric_key.encode('utf-8')).digest()
        cipher = AES.new(hashed_key, AES.MODE_CBC, iv)
        decrypted_message = cipher.decrypt(encrypted_message[AES.block_size:])
        return unpad_message(decrypted_message)
aes_algorithm = AESAlgorithm()
plain_text = "Hello World"
symmetric_key = "63757843836583645936548364836"
encrypted_text = aes_algorithm.encrypt(plain_text, symmetric_key)
print("Encrypted Text:", encrypted_text.decode())
decrypted_text = aes_algorithm.decrypt(encrypted_text, symmetric_key)
print("Decrypted Text:", decrypted_text.decode())