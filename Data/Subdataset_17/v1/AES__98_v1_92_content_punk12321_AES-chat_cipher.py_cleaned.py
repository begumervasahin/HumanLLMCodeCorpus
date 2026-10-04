
from Crypto.Cipher import AES
from Crypto import Random
__author__ = "spec"
__license__ = "MIT"
__version__ = "0.1"
__status__ = "Development"
class InvalidMessage(Exception):
    def __init__(self, msg):
        self.msg = msg
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
            raise InvalidMessage("Either plaintext or ciphertext must be provided")
    def encrypt(self):
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        buffer_size = AES.block_size - len(self.plaintext) % AES.block_size
        padded_plaintext = self.plaintext + " " * buffer_size
        encrypted_message = cipher.encrypt(padded_plaintext.encode('utf-8'))
        return encrypted_message, iv
    def decrypt(self):
        iv = self.ciphertext[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        decrypted_message = cipher.decrypt(self.ciphertext[AES.block_size:]).decode('utf-8').rstrip()
        return decrypted_message, iv
    def pack(self):
        return self.iv + self.ciphertext
if __name__ == "__main__":
    key = b'Sixteen byte key'
    plaintext = "This is a secret message."
    message = Message(key, plaintext=plaintext)
    packed_message = message.pack()
    print(f"Packed Message: {packed_message.hex()}")
    decrypted_message = Message(key, ciphertext=packed_message)
    print(f"Decrypted Message: {decrypted_message.plaintext}")