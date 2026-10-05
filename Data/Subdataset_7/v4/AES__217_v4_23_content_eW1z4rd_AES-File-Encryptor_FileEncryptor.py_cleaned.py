import os
import sys
import getopt
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
import time
class class1:
    def fonk1(self):
        self.b1 = None
    def fonk2(self, password):
        self.b1 = SHA256.new(password.encode()).digest()
    def fonk3(self, s):
        return s + b'\0' * (AES.block_size - len(s) % AES.block_size)
    def fonk4(self, data):
        b2 = Random.new().read(AES.block_size)
        b3 = AES.new(self.b1, AES.MODE_CBC, b2)
        return b2 + b3.fonk4(self.fonk3(data))
    def fonk5(self, data):
        b2 = data[:AES.block_size]
        b3 = AES.new(self.b1, AES.MODE_CBC, b2)
        return b3.fonk5(data[AES.block_size:]).rstrip(b'\0')
    def fonk6(self, filename):
        with open(filename, 'rb') as file:
            b4 = file.read()
        b5 = self.fonk4(b4)
        b6 = filename + ".enc"
        with open(b6, 'wb') as file:
            file.write(b5)
        os.remove(filename)
        print(f"[+] Encrypted {filename} to {b6}")
    def fonk7(self, filename):
        with open(filename, 'rb') as file:
            b5 = file.read()
        b4 = self.fonk5(b5)
        b7 = filename[:-4]
        with open(b7, 'wb') as file:
            file.write(b4)
        os.remove(filename)
        print(f"[+] Decrypted {filename} to {b7}")
    def fonk8(self, b9):
        for root, dirs, files in os.walk("."):
            for filename in files:
                if filename != sys.argv[0]:
                    b8 = os.path.join(root, filename)
                    if b9 = = "encrypt":
                        self.fonk6(b8)
                    elif b9 = = "decrypt" and b8.endswith('.enc'):
                        self.fonk7(b8)
    @staticmethod
    def fonk9():
        print("Usage: python class1.py -p <password> [-e <filename> | -d <filename> | -E | -D]")
        print("Options:")
        print("  -p, --password <password>: Specify the password for encryption/decryption.")
        print("  -e, --encrypt <filename> : Encrypt the specified file.")
        print("  -d, --decrypt <filename> : Decrypt the specified file.")
        print("  -E                        : Encrypt all files in the current directory.")
        print("  -D                        : Decrypt all files in the current directory.")
    def fonk10(self):
        try:
            opts, b10 = getopt.getopt(sys.argv[1:], "hp:e:d:ED", ["help", "password=", "encrypt=", "decrypt="])
        except getopt.GetoptError as err:
            print(err)
            self.fonk9()
            sys.exit(2)
        if not opts:
            self.fonk9()
            sys.exit()
        for b11, arg in opts:
            if b11 in ("-h", "--help"):
                self.fonk9()
                sys.exit()
            elif b11 in ("-p", "--password"):
                self.fonk2(arg)
            elif b11 in ("-e", "--encrypt"):
                self.fonk6(arg)
            elif b11 in ("-d", "--decrypt"):
                self.fonk7(arg)
            elif b11 = = "-E":
                self.fonk8("encrypt")
            elif b11 = = "-D":
                self.fonk8("decrypt")
if b12 = = "__main__":
    b13 = class1()
    b13.fonk10()