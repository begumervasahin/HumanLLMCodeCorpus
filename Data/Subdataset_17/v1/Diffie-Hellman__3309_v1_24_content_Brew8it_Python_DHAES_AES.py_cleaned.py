from base64 import b64decode, b64encode
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
BLOCK_SIZE = 16
def pad(s):
    padding = (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
    return s + padding
def unpad(s):
    return s[:-ord(s[-1])]
class AESCipher:
    def __init__(self, key):
        self.key = key.encode('utf8')
    def encrypt(self, raw):
        raw_padded = pad(raw)
        iv = get_random_bytes(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        encrypted = cipher.encrypt(raw_padded.encode('utf8'))
        return b64encode(iv + encrypted).decode('utf8')
    def decrypt(self, enc):
        enc = b64decode(enc)
        iv = enc[:BLOCK_SIZE]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        decrypted = cipher.decrypt(enc[BLOCK_SIZE:])
        return unpad(decrypted).decode('utf8')
if __name__ == "__main__":
    key = 'password'
    message = 'This is a secret message.'
    cipher = AESCipher(key)
    encrypted_message = cipher.encrypt(message)
    print(f'Encrypted: {encrypted_message}')
    decrypted_message = cipher.decrypt(encrypted_message)
    print(f'Decrypted: {decrypted_message}')