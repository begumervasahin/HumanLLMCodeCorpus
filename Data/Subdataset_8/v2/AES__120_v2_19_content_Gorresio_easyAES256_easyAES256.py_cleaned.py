import sys
from hashlib import sha256
from Crypto import Random
from Crypto.Cipher import AES
BLOCK_SIZE = 16
def pad(s):
    padding_length = BLOCK_SIZE - len(s) % BLOCK_SIZE
    return s + chr(padding_length) * padding_length
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
def print_usage_and_exit():
    print("Usage: easyAES256 <encrypt|decrypt> <filename> <key>")
    sys.exit()
def main():
    try:
        option, filename, key = sys.argv[1:4]
        if option not in ("encrypt", "decrypt"):
            raise ValueError("Invalid option")
    except (ValueError, IndexError):
        print_usage_and_exit()
    try:
        with open(filename, "rb") as file:
            data = file.read()
    except IOError:
        print(f"Error reading \"{filename}\".")
        sys.exit()
    cipher = AESCipher(key)
    if option == "encrypt":
        result = cipher.encrypt(data.decode('utf-8'))
        output_filename = f"{filename}.crypt"
    else:
        result = cipher.decrypt(data).encode('utf-8')
        output_filename = filename[:-6]
    try:
        with open(output_filename, "wb") as file:
            file.write(result)
    except IOError:
        print(f"Error writing to \"{output_filename}\".")
        sys.exit()
if __name__ == "__main__":
    main()