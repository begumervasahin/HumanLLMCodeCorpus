import os
import sys
import getopt
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
class FileEncryptor:
    def __init__(self):
        self.key = None
    def create_key(self, password):
        hasher = SHA256.new(password.encode())
        self.key = hasher.digest()
    def encrypt_data(self, data):
        def pad(s):
            return s + b"\0" * (AES.block_size - len(s) % AES.block_size)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return iv + cipher.encrypt(pad(data))
    def decrypt_data(self, data):
        iv = data[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        plaintext = cipher.decrypt(data[AES.block_size:])
        return plaintext.rstrip(b"\0")
    def process_file(self, filename, mode='encrypt'):
        file_operation = {
            'encrypt': (self.encrypt_data, ".enc", "Encrypted", "adding"),
            'decrypt': (self.decrypt_data, "", "Decrypted", "removing")
        }
        func, ext, action, operation = file_operation[mode]
        with open(filename, 'rb') as file:
            file_data = file.read()
        processed_data = func(file_data)
        if mode == 'encrypt':
            new_filename = filename + ext
        else:
            new_filename = filename.replace('.enc', '')
        with open(new_filename, 'wb') as file:
            file.write(processed_data)
        os.remove(filename)
        print(f"[+] {action} {filename} --> {new_filename} by {operation} extension.")
    def process_directory(self, mode='encrypt'):
        for root, dirs, files in os.walk("."):
            for file in files:
                if mode == 'encrypt' or (mode == 'decrypt' and file.endswith('.enc')):
                    filepath = os.path.join(root, file)
                    if filepath != sys.argv[0]:
                        self.process_file(filepath, mode)
        print(f"[+] All files {mode}ed successfully.")
    @staticmethod
    def show_usage():
        print("Usage: python FileEncryptor.py -p <password> [-e <filename> | -d <filename> | -E | -D]")
        print("-p, --password <password> : Specify the password for encryption/decryption.")
        print("-e, --encrypt <filename>  : Encrypt the specified file.")
        print("-d, --decrypt <filename>  : Decrypt the specified file.")
        print("-E                        : Encrypt all files within the current directory.")
        print("-D                        : Decrypt all files within the current directory.")
    def run(self):
        try:
            opts, _ = getopt.getopt(sys.argv[1:], "hp:e:d:ED", ["help", "password=", "encrypt=", "decrypt="])
        except getopt.GetoptError as err:
            print(err)
            self.show_usage()
            sys.exit(2)
        if not opts:
            self.show_usage()
            sys.exit(2)
        for opt, arg in opts:
            if opt in ("-h", "--help"):
                self.show_usage()
                sys.exit()
            elif opt in ("-p", "--password"):
                self.create_key(arg)
            elif opt in ("-e", "--encrypt") and self.key:
                self.process_file(arg, 'encrypt')
            elif opt in ("-d", "--decrypt") and self.key:
                self.process_file(arg, 'decrypt')
            elif opt == "-E" and self.key:
                self.process_directory('encrypt')
            elif opt == "-D" and self.key:
                self.process_directory('decrypt')
if __name__ == "__main__":
    fe = FileEncryptor()
    fe.run()