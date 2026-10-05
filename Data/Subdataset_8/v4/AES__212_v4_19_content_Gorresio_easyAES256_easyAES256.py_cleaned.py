import sys
from hashlib import sha256
from Crypto import Random
from Crypto.Cipher import AES
BLOCK_SIZE = 16
def pad(s):
    padding_length = BLOCK_SIZE - len(s) % BLOCK_SIZE
    return s + (chr(padding_length) * padding_length)
def unpad(s):
    return s[:-ord(s[-1])]
class AESCipher:
    def __init__(self, key):
        self.key = sha256(key.encode('utf-8')).digest()
    def encrypt(self, raw):
        raw_padded = pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return iv + cipher.encrypt(raw_padded.encode('utf-8'))
    def decrypt(self, enc):
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')
def invalid_arguments():
    print("Usage: script.py <encrypt|decrypt> <filename> <key>")
    sys.exit(1)
def main():
    if len(sys.argv) != 4:
        invalid_arguments()
    action, filename, key = sys.argv[1], sys.argv[2], sys.argv[3]
    if action not in ['encrypt', 'decrypt']:
        invalid_arguments()
    try:
        with open(filename, 'rb') as file:
            data = file.read()
    except IOError:
        print(f"Error reading file: {filename}")
        sys.exit(1)
    cipher = AESCipher(key)
    if action == 'encrypt':
        processed_data = cipher.encrypt(data.decode('utf-8'))
        out_filename = f"{filename}.crypt"
    else:
        processed_data = cipher.decrypt(data)
        out_filename = filename.rsplit('.', 1)[0]
    try:
        with open(out_filename, 'wb') as file:
            file.write(processed_data.encode('utf-8') if action == 'decrypt' else processed_data)
    except IOError:
        print(f"Error writing to file: {out_filename}")
        sys.exit(1)
if __name__ == "__main__":
    main()