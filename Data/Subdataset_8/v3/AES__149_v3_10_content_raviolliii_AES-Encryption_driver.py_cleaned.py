from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64
class AESCipher:
    def __init__(self, key):
        self.key = self._ensure_key_length(key.encode('utf-8'))
    def encrypt(self, message):
        message_bytes = message.encode('utf-8')
        cipher = AES.new(self.key, AES.MODE_CBC)
        encrypted_bytes = cipher.encrypt(pad(message_bytes, AES.block_size))
        iv_encoded = base64.b64encode(cipher.iv).decode('utf-8')
        encrypted_encoded = base64.b64encode(encrypted_bytes).decode('utf-8')
        return iv_encoded + encrypted_encoded
    def decrypt(self, encrypted_message):
        iv = base64.b64decode(encrypted_message[:24])
        encrypted_bytes = base64.b64decode(encrypted_message[24:])
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        decrypted_bytes = unpad(cipher.decrypt(encrypted_bytes), AES.block_size)
        return decrypted_bytes.decode('utf-8')
    @staticmethod
    def _ensure_key_length(key, desired_length=16):
        return pad(key, desired_length)[:desired_length]
def main():
    key = "Thats my Kung Fu"
    message = "Two One Nine Two"
    aes_cipher = AESCipher(key)
    encrypted_message = aes_cipher.encrypt(message)
    print("Message:\t", message)
    print("Encrypted:\t", encrypted_message)
    decrypted_message = aes_cipher.decrypt(encrypted_message)
    print("Decrypted:\t", decrypted_message)
if __name__ == "__main__":
    main()