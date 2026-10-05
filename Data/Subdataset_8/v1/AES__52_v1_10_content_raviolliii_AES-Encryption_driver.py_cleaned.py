from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64
class AESCipher:
    def __init__(self, key):
        self.key = key.encode('utf-8')
    def encrypt(self, message):
        message = message.encode('utf-8')
        cipher = AES.new(self.key, AES.MODE_CBC)
        ct_bytes = cipher.encrypt(pad(message, AES.block_size))
        iv = base64.b64encode(cipher.iv).decode('utf-8')
        ct = base64.b64encode(ct_bytes).decode('utf-8')
        return iv + ct
    def decrypt(self, encrypted_message):
        iv = base64.b64decode(encrypted_message[:24])
        ct = base64.b64decode(encrypted_message[24:])
        cipher = AES.new(self.key, AES.MODE_CBC, iv=iv)
        pt = unpad(cipher.decrypt(ct), AES.block_size)
        return pt.decode('utf-8')
key = "Thats my Kung Fu"
if len(key) not in [16, 24, 32]:
    raise ValueError("Key must be 16, 24, or 32 bytes long")
message = "Two One Nine Two"
cipher = AESCipher(key)
correct_length_key = pad(key.encode(), 16)[:16]
cipher.key = correct_length_key
enc = cipher.encrypt(message)
print("Message:\t", message)
print("Encrypted:\t", enc)
dec = cipher.decrypt(enc)
print("Decrypted:\t", dec)