from base64 import b64decode, b64encode
from Crypto import Random
from Crypto.Cipher import AES
BLOCK_SIZE = 16
def pad(s):
    pad_length = BLOCK_SIZE - len(s) % BLOCK_SIZE
    return s + pad_length * chr(pad_length)
def unpad(s):
    return s[:-ord(s[len(s) - 1:])]
class AESCipher:
    def __init__(self, key):
        self.key = key
    def encrypt(self, raw):
        raw = pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return b64encode(iv + cipher.encrypt(raw))
    def decrypt(self, enc):
        enc = b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')