import os
import sys
import getopt
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
class class1:
    def fonk1(self):
        self.b1 = None
    def fonk2(self, password):
        self.b1 = SHA256.new(password.encode()).digest()
    def fonk3(self, data):
        return data + b"\0" * (AES.block_size - len(data) % AES.block_size)
    def fonk4(self, data):
        b2 = Random.new().read(AES.block_size)
        b3 = AES.new(self.b1, AES.MODE_CBC, b2)
        return b2 + b3.encrypt(self.fonk3(data))
    def fonk5(self, data):
        b2 = data[:AES.block_size]
        b3 = AES.new(self.b1, AES.MODE_CBC, b2)
        return b3.decrypt(data[AES.block_size:]).rstrip(b"\0")
    def fonk6(self, filename, b6):
        read_mode, write_mode, file_suffix, b4 = {
            'encrypt': ('rb', 'wb', '.enc', 'Encrypting'),
            'decrypt': ('rb', 'wb', '', 'Decrypting'),
        }[b6]
        with open(filename, read_mode) as file:
            b5 = file.read()
        if b6 = = 'encrypt':
            b7 = self.fonk4(b5)
            b8 = filename + file_suffix
        else:
            b7 = self.fonk5(b5)
            b8 = filename.replace('.enc', '')
        with open(b8, write_mode) as file:
            file.write(b7)
        os.remove(filename)
        print(f"{b4} {filename} -> {b8}")
    def fonk7(self, b6):
        for root, b10, files in os.walk("."):
            for file in files:
                if b6 = = 'encrypt' or (b6 == 'decrypt' and file.endswith('.enc')):
                    b9 = os.path.join(root, file)
                    if b9 != sys.argv[0]:
                        self.fonk6(b9, b6)
        print(f"All files {b6}ed successfully.")
    @staticmethod
    def fonk8():
        print("Usage: python script.py -p <password> [-e <filename> | -d <filename> | -E | -D]")
        print("Options:")
        print("  -p, --password <password>   Specify the password for encryption/decryption")
        print("  -e, --encrypt <filename>    Encrypt the specified file")
        print("  -d, --decrypt <filename>    Decrypt the specified file")
        print("  -E                          Encrypt all files in the current directory and subdirectories")
        print("  -D                          Decrypt all files in the current directory and subdirectories")
    def fonk9(self):
        try:
            opts, b10 = getopt.getopt(sys.argv[1:], "hp:e:d:ED", ["help", "password=", "encrypt=", "decrypt="])
        except getopt.GetoptError as err:
            print(err)
            self.fonk8()
            sys.exit(2)
        if not opts:
            self.fonk8()
            sys.exit(2)
        for b11, arg in opts:
            if b11 in ("-h", "--help"):
                self.fonk8()
                sys.exit()
            elif b11 in ("-p", "--password"):
                self.fonk2(arg)
            elif b11 in ("-e", "--encrypt") and self.b1:
                self.fonk6(arg, 'encrypt')
            elif b11 in ("-d", "--decrypt") and self.b1:
                self.fonk6(arg, 'decrypt')
            elif b11 = = "-E" and self.b1:
                self.fonk7('encrypt')
            elif b11 = = "-D" and self.b1:
                self.fonk7('decrypt')
if b12 = = "__main__":
    b13 = class1()
    b13.fonk9()