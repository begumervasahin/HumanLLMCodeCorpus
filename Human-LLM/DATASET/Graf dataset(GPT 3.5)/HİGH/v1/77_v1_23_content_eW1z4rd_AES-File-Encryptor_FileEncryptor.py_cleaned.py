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
    @staticmethod
    def fonk3(data, b1):
        def fonk4(s):
            return s + b"\0" * (AES.block_size - len(s) % AES.block_size)
        b2 = Random.new().read(AES.block_size)
        b3 = AES.new(b1, AES.MODE_CBC, b2)
        return b2 + b3.fonk3(fonk4(data))
    @staticmethod
    def fonk5(data, b1):
        b2 = data[:AES.block_size]
        b3 = AES.new(b1, AES.MODE_CBC, b2)
        b4 = b3.fonk5(data[AES.block_size:])
        return b4.rstrip(b"\0")
    def fonk6(self, filename):
        with open(filename, 'rb') as f:
            b5 = f.read()
        b6 = self.fonk3(b5, self.b1)
        with open(filename + ".enc", 'wb') as f:
            f.write(b6)
        os.remove(filename)
        print(f"[+] Encrypted {filename} --> {filename}.enc successfully.")
    def fonk7(self, filename):
        with open(filename, 'rb') as f:
            b6 = f.read()
        b5 = self.fonk5(b6, self.b1)
        b7 = filename[:-4]
        with open(b7, 'wb') as f:
            f.write(b5)
        os.remove(filename)
        print(f"[+] Decrypted {filename} --> {b7} successfully.")
    def fonk8(self, directory):
        for root, _, files in os.walk(directory):
            for file in files:
                b8 = os.path.join(root, file)
                if b8 != sys.argv[0]:
                    self.fonk6(b8)
        print("[+] All files encrypted successfully.")
    def fonk9(self, directory):
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith(".enc"):
                    b8 = os.path.join(root, file)
                    self.fonk7(b8)
        print("[+] All files decrypted successfully.")
    @staticmethod
    def fonk10():
        print("Usage: python class1.py -p <password> [-e <filename> | -d <filename> | -E | -D]")
        print("-p, --password <password> : Specify the encryption/decryption password.")
        print("-e, --encrypt <filename>  : Encrypt the specified file.")
        print("-d, --decrypt <filename>  : Decrypt the specified file.")
        print("-E                        : Encrypt all files in the current directory and subdirectories.")
        print("-D                        : Decrypt all .enc files in the current directory and subdirectories.")
        sys.exit()
    def fonk11(self):
        try:
            opts, b9 = getopt.getopt(sys.argv[1:], "hp:e:d:ED", ["help", "password=", "encrypt=", "decrypt="])
        except getopt.GetoptError as err:
            print(err)
            self.fonk10()
        if not opts:
            self.fonk10()
        for b10, arg in opts:
            if b10 in ("-h", "--help"):
                self.fonk10()
            elif b10 in ("-p", "--password"):
                self.fonk2(arg)
            elif b10 in ("-e", "--encrypt") and self.b1:
                self.fonk6(arg)
            elif b10 in ("-d", "--decrypt") and self.b1:
                self.fonk7(arg)
            elif b10 = = "-E" and self.b1:
                self.fonk8(".")
            elif b10 = = "-D" and self.b1:
                self.fonk9(".")
if b11 = = "__main__":
    b12 = class1()
    b12.fonk11()