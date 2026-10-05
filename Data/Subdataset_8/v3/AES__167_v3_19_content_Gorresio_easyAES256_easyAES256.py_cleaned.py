import sys
from hashlib import sha256
from Crypto import Random
from Crypto.Cipher import AES
BLOCK_SIZE = 16
def pad(text):
    padding = BLOCK_SIZE - len(text) % BLOCK_SIZE
    return text + chr(padding) * padding
def unpad(text):
    return text[:-ord(text[-1])]
class AESCipher:
    def __init__(self, key):
        self.key = sha256(key.encode()).digest()
    def encrypt(self, plaintext):
        plaintext = pad(plaintext)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return iv + cipher.encrypt(plaintext.encode())
    def decrypt(self, ciphertext):
        iv = ciphertext[:BLOCK_SIZE]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return unpad(cipher.decrypt(ciphertext[BLOCK_SIZE:])).decode()
def print_usage_and_exit():
    print("Usage: script.py <encrypt|decrypt> <filename> <key>")
    sys.exit(1)
def main():
    if len(sys.argv) != 4:
        print_usage_and_exit()
    option, filename, key = sys.argv[1:4]
    if option not in ["encrypt", "decrypt"]:
        print_usage_and_exit()
    try:
        with open(filename, "rb") as f:
            data = f.read()
    except IOError as e:
        print(f"Failed to read '{filename}': {e}")
        sys.exit(1)
    cipher = AESCipher(key)
    if option == "encrypt":
        processed_data = cipher.encrypt(data.decode())
        output_filename = f"{filename}.crypt"
    else:
        processed_data = cipher.decrypt(data).encode()
        output_filename = filename.rsplit('.', 1)[0]
    try:
        with open(output_filename, "wb") as f:
            f.write(processed_data)
    except IOError as e:
        print(f"Failed to write '{output_filename}': {e}")
        sys.exit(1)
if __name__ == "__main__":
    main()