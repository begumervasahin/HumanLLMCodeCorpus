
from Crypto.Cipher import AES
from Crypto import Random
__author__ = "spec"
__license__ = "MIT"
__version__ = "0.1"
__status__ = "Development"
class Message:
    def __init__(self, key, plaintext=None, ciphertext=None):
        self.key = key
        if plaintext:
            self.plaintext = plaintext
            self.ciphertext, self.iv = self.encrypt()
        elif ciphertext:
            self.ciphertext = ciphertext
            self.plaintext, self.iv = self.decrypt()
        else:
            raise InvalidMessage("Either plaintext or cipher-text must be declared")
    def encrypt(self):
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        pt_len = len(self.plaintext)
        buffer_size = AES.block_size - pt_len % AES.block_size
        return cipher.encrypt(self.plaintext + " " * buffer_size), iv
    def decrypt(self):
        iv = self.ciphertext[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return cipher.decrypt(self.ciphertext)[AES.block_size:].rstrip().decode("utf-8"), iv
    def pack(self):
        return self.iv + self.ciphertext
class InvalidMessage(Exception):
    def __init__(self, msg):
        self.msg = msg