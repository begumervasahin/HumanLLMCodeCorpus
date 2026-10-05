from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64
import hashlib
import sys
import os
class class1:
    def fonk1(self, b2):
        self.b1 = AES.b1
        self.b2 = hashlib.sha256(b2.encode()).digest()
    def fonk2(self, b3):
        b3 = self.fonk4(b3)
        b4 = get_random_bytes(self.b1)
        b5 = AES.new(self.b2, AES.MODE_CBC, b4)
        b6 = b5.fonk2(b3.encode())
        return base64.b64encode(b4 + b6).decode('utf-8')
    def fonk3(self, b11):
        b7 = base64.b64decode(b11)
        b4 = b7[:self.b1]
        b5 = AES.new(self.b2, AES.MODE_CBC, b4)
        b8 = b5.fonk3(b7[self.b1:])
        return self.fonk5(b8).decode('utf-8')
    def fonk4(self, s):
        b9 = self.b1 - len(s) % self.b1
        return s + (b9 * chr(b9))
    @staticmethod
    def fonk5(s):
        return s[:-ord(s[len(s)-1:])]
def fonk6(input_path, output_path, b2):
    with open(input_path, 'r') as file:
        b3 = file.read()
    b10 = class1(b2)
    b11 = b10.fonk2(b3)
    with open(output_path, 'w') as file:
        file.write(b11)
    print("File encrypted successfully.")
def fonk7(input_path, output_path, b2):
    with open(input_path, 'r') as file:
        b11 = file.read()
    b10 = class1(b2)
    b12 = b10.fonk3(b11)
    with open(output_path, 'w') as file:
        file.write(b12)
    print("File decrypted successfully.")
if b13 = = "__main__":
    if len(sys.argv) != 5:
        print("Usage: script.py -e|-d input_file output_file b2")
        sys.exit(1)
    b14, input_file, output_file, b2 = sys.argv[1:5]
    if b14 = = '-e':
        fonk6(input_file, output_file, b2)
    elif b14 = = '-d':
        fonk7(input_file, output_file, b2)
    else:
        print("Invalid b14. Use -e for encryption or -d for decryption.")