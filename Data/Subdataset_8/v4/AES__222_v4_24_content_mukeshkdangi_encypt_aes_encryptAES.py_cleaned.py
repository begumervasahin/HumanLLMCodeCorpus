from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64
import hashlib
import sys
import os
class AESCipher:
    def __init__(self, key):
        self.block_size = AES.block_size
        self.key = hashlib.sha256(key.encode()).digest()
    def encrypt(self, plaintext):
        plaintext = self._pad(plaintext)
        iv = get_random_bytes(self.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        encrypted_bytes = cipher.encrypt(plaintext.encode())
        return base64.b64encode(iv + encrypted_bytes).decode('utf-8')
    def decrypt(self, encrypted_text):
        encrypted_data = base64.b64decode(encrypted_text)
        iv = encrypted_data[:self.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        decrypted_bytes = cipher.decrypt(encrypted_data[self.block_size:])
        return self._unpad(decrypted_bytes).decode('utf-8')
    def _pad(self, s):
        padding_length = self.block_size - len(s) % self.block_size
        return s + (padding_length * chr(padding_length))
    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]
def encrypt_file(input_path, output_path, key):
    with open(input_path, 'r') as file:
        plaintext = file.read()
    aes = AESCipher(key)
    encrypted_text = aes.encrypt(plaintext)
    with open(output_path, 'w') as file:
        file.write(encrypted_text)
    print("File encrypted successfully.")
def decrypt_file(input_path, output_path, key):
    with open(input_path, 'r') as file:
        encrypted_text = file.read()
    aes = AESCipher(key)
    decrypted_text = aes.decrypt(encrypted_text)
    with open(output_path, 'w') as file:
        file.write(decrypted_text)
    print("File decrypted successfully.")
if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: script.py -e|-d input_file output_file key")
        sys.exit(1)
    mode, input_file, output_file, key = sys.argv[1:5]
    if mode == '-e':
        encrypt_file(input_file, output_file, key)
    elif mode == '-d':
        decrypt_file(input_file, output_file, key)
    else:
        print("Invalid mode. Use -e for encryption or -d for decryption.")