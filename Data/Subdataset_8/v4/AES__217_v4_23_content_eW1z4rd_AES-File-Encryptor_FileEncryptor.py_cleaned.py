import os
import sys
import getopt
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
import time
class FileEncryptor:
    def __init__(self):
        self.key = None
    def generate_key(self, password):
        self.key = SHA256.new(password.encode()).digest()
    def pad(self, s):
        return s + b'\0' * (AES.block_size - len(s) % AES.block_size)
    def encrypt(self, data):
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return iv + cipher.encrypt(self.pad(data))
    def decrypt(self, data):
        iv = data[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return cipher.decrypt(data[AES.block_size:]).rstrip(b'\0')
    def encrypt_file(self, filename):
        with open(filename, 'rb') as file:
            plaintext = file.read()
        encrypted_data = self.encrypt(plaintext)
        encrypted_filename = filename + ".enc"
        with open(encrypted_filename, 'wb') as file:
            file.write(encrypted_data)
        os.remove(filename)
        print(f"[+] Encrypted {filename} to {encrypted_filename}")
    def decrypt_file(self, filename):
        with open(filename, 'rb') as file:
            encrypted_data = file.read()
        plaintext = self.decrypt(encrypted_data)
        original_filename = filename[:-4]
        with open(original_filename, 'wb') as file:
            file.write(plaintext)
        os.remove(filename)
        print(f"[+] Decrypted {filename} to {original_filename}")
    def process_all_files(self, action):
        for root, dirs, files in os.walk("."):
            for filename in files:
                if filename != sys.argv[0]:
                    filepath = os.path.join(root, filename)
                    if action == "encrypt":
                        self.encrypt_file(filepath)
                    elif action == "decrypt" and filepath.endswith('.enc'):
                        self.decrypt_file(filepath)
    @staticmethod
    def show_usage():
        print("Usage: python FileEncryptor.py -p <password> [-e <filename> | -d <filename> | -E | -D]")
        print("Options:")
        print("  -p, --password <password>: Specify the password for encryption/decryption.")
        print("  -e, --encrypt <filename> : Encrypt the specified file.")
        print("  -d, --decrypt <filename> : Decrypt the specified file.")
        print("  -E                        : Encrypt all files in the current directory.")
        print("  -D                        : Decrypt all files in the current directory.")
    def run(self):
        try:
            opts, args = getopt.getopt(sys.argv[1:], "hp:e:d:ED", ["help", "password=", "encrypt=", "decrypt="])
        except getopt.GetoptError as err:
            print(err)
            self.show_usage()
            sys.exit(2)
        if not opts:
            self.show_usage()
            sys.exit()
        for opt, arg in opts:
            if opt in ("-h", "--help"):
                self.show_usage()
                sys.exit()
            elif opt in ("-p", "--password"):
                self.generate_key(arg)
            elif opt in ("-e", "--encrypt"):
                self.encrypt_file(arg)
            elif opt in ("-d", "--decrypt"):
                self.decrypt_file(arg)
            elif opt == "-E":
                self.process_all_files("encrypt")
            elif opt == "-D":
                self.process_all_files("decrypt")
if __name__ == "__main__":
    file_encryptor = FileEncryptor()
    file_encryptor.run()