from Crypto import Random
from Crypto.Cipher import AES
import base64
class AESCrypto:
    def __init__(self, key, value_of):
        self.value_of = value_of[-6:]
        self.key = self._generate_key(key)
        self.BLOCK_SIZE = 16
    def _generate_key(self, key):
        def change_name(name, index, rate):
            index %= len(name)
            prefix = name[:index]
            insertion = name[index] * rate
            suffix = name[index:]
            return prefix + insertion + suffix
        for i in range(3):
            segment = self.value_of[i * 2:i * 2 + 2]
            index = int(segment[0])
            rate = int(segment[1])
            key = change_name(key, index, rate)
        return key[:16].ljust(16, '_').encode('utf-8')
    def _pad(self, data):
        pad_length = self.BLOCK_SIZE - len(data) % self.BLOCK_SIZE
        return data + chr(pad_length) * pad_length
    def _unpad(self, data):
        return data[:-ord(data[-1])]
    def encrypt(self, message):
        padded_message = self._pad(message)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        encrypted_message = iv + cipher.encrypt(padded_message.encode('utf-8'))
        return base64.b64encode(encrypted_message).decode('utf-8')
    def decrypt(self, encrypted):
        encrypted_bytes = base64.b64decode(encrypted)
        iv = encrypted_bytes[:self.BLOCK_SIZE]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        decrypted_message = self._unpad(cipher.decrypt(encrypted_bytes[self.BLOCK_SIZE:]))
        return decrypted_message.decode('utf-8')
if __name__ == "__main__":
    key = "mysecretpassword"
    value_of = "123456"
    message = "This is a secret message."
    aes_crypto = AESCrypto(key, value_of)
    encrypted_message = aes_crypto.encrypt(message)
    print(f"Encrypted: {encrypted_message}")
    decrypted_message = aes_crypto.decrypt(encrypted_message)
    print(f"Decrypted: {decrypted_message}")