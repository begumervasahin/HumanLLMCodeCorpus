from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64
class SimpleAESCipher:
    def __init__(self, key):
        self.key = key.encode('utf-8')
    def encrypt(self, message):
        message_bytes = message.encode('utf-8')
        cipher = AES.new(self.key, AES.MODE_CBC)
        ciphertext_bytes = cipher.encrypt(pad(message_bytes, AES.block_size))
        iv = base64.b64encode(cipher.iv).decode('utf-8')
        ciphertext = base64.b64encode(ciphertext_bytes).decode('utf-8')
        return iv + ciphertext
    def decrypt(self, encrypted_message):
        iv = base64.b64decode(encrypted_message[:24])
        ciphertext = base64.b64decode(encrypted_message[24:])
        cipher = AES.new(self.key, AES.MODE_CBC, iv=iv)
        plaintext_bytes = unpad(cipher.decrypt(ciphertext), AES.block_size)
        return plaintext_bytes.decode('utf-8')
key = "Thats my Kung Fu"
message = "Two One Nine Two"
key = pad(key.encode(), 16)[:16]
aes_cipher = SimpleAESCipher(key)
encrypted_message = aes_cipher.encrypt(message)
print("Message:\t", message)
print("Encrypted:\t", encrypted_message)
decrypted_message = aes_cipher.decrypt(encrypted_message)
print("Decrypted:\t", decrypted_message)