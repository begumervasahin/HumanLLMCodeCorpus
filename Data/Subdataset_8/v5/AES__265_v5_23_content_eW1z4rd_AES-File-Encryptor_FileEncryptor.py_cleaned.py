import os
import sys
import getopt
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
class FileEncryptor:
    def __init__(self):
        self.key = None
    def set_encryption_key(self, password):
        hash_of_password = SHA256.new(password.encode()).digest()
        self.key = hash_of_password
    def encrypt_data(self, data):
        initialization_vector = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, initialization_vector)
        padded_data = self._pad(data)
        encrypted_data = cipher.encrypt(padded_data)
        return initialization_vector + encrypted_data
    def decrypt_data(self, encrypted_data):
        initialization_vector = encrypted_data[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, initialization_vector)
        decrypted_padded_data = cipher.decrypt(encrypted_data[AES.block_size:])
        return self._unpad(decrypted_padded_data)
    def _pad(self, data):
        padding_length = AES.block_size - len(data) % AES.block_size
        padding = bytes([padding_length]) * padding_length
        return data + padding
    def _unpad(self, data):
        padding_length = data[-1]
        return data[:-padding_length]
    def encrypt_file(self, filepath):
        with open(filepath, 'rb') as file:
            plaintext = file.read()
        encrypted_data = self.encrypt_data(plaintext)
        with open(filepath + ".enc", 'wb') as file:
            file.write(encrypted_data)
        os.remove(filepath)
        print(f"Encrypted {filepath}")
    def decrypt_file(self, filepath):
        with open(filepath, 'rb') as file:
            encrypted_data = file.read()
        plaintext = self.decrypt_data(encrypted_data)
        original_filepath = filepath[:-4]
        with open(original_filepath, 'wb') as file:
            file.write(plaintext)
        os.remove(filepath)
        print(f"Decrypted {filepath} to {original_filepath}")
    def process_directory(self, action):
        for root, _, filenames in os.walk("."):
            for filename in filenames:
                if filename != sys.argv[0]:
                    filepath = os.path.join(root, filename)
                    if action == "encrypt":
                        self.encrypt_file(filepath)
                    elif action == "decrypt" and filepath.endswith('.enc'):
                        self.decrypt_file(filepath)
    def display_help_message(self):
        usage_text =
        print(usage_text.strip())
    def run(self):
        try:
            options, _ = getopt.getopt(sys.argv[1:], "hp:e:d:ED", ["help", "password=", "encrypt=", "decrypt="])
        except getopt.GetoptError as error:
            print(error)
            self.display_help_message()
            sys.exit(2)
        for option, argument in options:
            if option in ("-h", "--help"):
                self.display_help_message()
                sys.exit()
            elif option in ("-p", "--password"):
                self.set_encryption_key(argument)
            elif option in ("-e", "--encrypt"):
                self.encrypt_file(argument)
            elif option in ("-d", "--decrypt"):
                self.decrypt_file(argument)
            elif option == "-E":
                self.process_directory("encrypt")
            elif option == "-D":
                self.process_directory("decrypt")
if __name__ == "__main__":
    encryptor = FileEncryptor()
    encryptor.run()