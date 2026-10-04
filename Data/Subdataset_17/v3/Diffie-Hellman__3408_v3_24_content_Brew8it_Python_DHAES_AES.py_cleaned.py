from base64 import b64decode, b64encode
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
BLOCK_SIZE = 16
def pad(data):
    padding_length = BLOCK_SIZE - len(data) % BLOCK_SIZE
    padding = chr(padding_length) * padding_length
    return data + padding
def unpad(data):
    padding_length = ord(data[-1])
    return data[:-padding_length]
class AESCipher:
    def __init__(self, key):
        self.key = key.encode('utf-8')
    def encrypt(self, raw):
        raw_padded = pad(raw)
        iv = get_random_bytes(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        encrypted = cipher.encrypt(raw_padded.encode('utf-8'))
        return b64encode(iv + encrypted).decode('utf-8')
    def decrypt(self, enc):
        enc_bytes = b64decode(enc)
        iv = enc_bytes[:BLOCK_SIZE]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        decrypted = cipher.decrypt(enc_bytes[BLOCK_SIZE:])
        return unpad(decrypted.decode('utf-8'))
def main():
    key = 'password'
    message = 'This is a secret message.'
    cipher = AESCipher(key)
    encrypted_message = cipher.encrypt(message)
    print(f'Encrypted: {encrypted_message}')
    decrypted_message = cipher.decrypt(encrypted_message)
    print(f'Decrypted: {decrypted_message}')
if __name__ == "__main__":
    main()