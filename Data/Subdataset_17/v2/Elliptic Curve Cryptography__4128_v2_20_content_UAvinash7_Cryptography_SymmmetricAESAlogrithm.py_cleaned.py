import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES
BS = 16
def pad(message):
    padding = BS - len(message) % BS
    return message + chr(padding) * padding
def unpad(padded_message):
    return padded_message[:-ord(padded_message[-1])]
class AESAlgorithm:
    def encrypt(self, message, symmetric_key):
        raw = pad(message)
        symmetric_key = hashlib.sha256(symmetric_key.encode('utf-8')).digest()
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(symmetric_key, AES.MODE_CBC, iv)
        encrypted_message = iv + cipher.encrypt(raw.encode('utf-8'))
        return base64.b64encode(encrypted_message).decode('utf-8')
    def decrypt(self, encrypted_message, symmetric_key):
        encrypted_message = base64.b64decode(encrypted_message)
        symmetric_key = hashlib.sha256(symmetric_key.encode('utf-8')).digest()
        iv = encrypted_message[:16]
        cipher = AES.new(symmetric_key, AES.MODE_CBC, iv)
        decrypted_message = cipher.decrypt(encrypted_message[16:])
        return unpad(decrypted_message).decode('utf-8')
if __name__ == "__main__":
    aes_algorithm = AESAlgorithm()
    plain_text = "Hello World"
    sym_key = "63757843836583645936548364836"
    encrypted_text = aes_algorithm.encrypt(plain_text, sym_key)
    print("Encrypted Text:", encrypted_text)
    decrypted_text = aes_algorithm.decrypt(encrypted_text, sym_key)
    print("Decrypted Text:", decrypted_text)