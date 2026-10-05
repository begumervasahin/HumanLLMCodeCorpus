import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES
BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s: s[0:-ord(s[-1])]
class AESAlgorithm:
    def encrypt(self, message, symmetric_key):
        raw = pad(message)
        symmetric_key = hashlib.sha256(symmetric_key.encode('utf-8')).digest()
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(symmetric_key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw))
    def decrypt(self, enc, symmetric_key):
        enc = base64.b64decode(enc)
        symmetric_key = hashlib.sha256(symmetric_key.encode('utf-8')).digest()
        iv = enc[:16]
        cipher = AES.new(symmetric_key, AES.MODE_CBC, iv)
        return unpad(cipher.decrypt(enc[16:]))
aes_algorithm = AESAlgorithm()
plain_text = "Hello World"
sym_key1 = "63757843836583645936548364836"
encrypted_text = aes_algorithm.encrypt(plain_text, sym_key1)
print("Encrypted Text:", encrypted_text.decode())
sym_key2 = "63757843836583645936548364836"
decrypted_text = aes_algorithm.decrypt(encrypted_text, sym_key2)
print("Decrypted Text:", decrypted_text.decode())