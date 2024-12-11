import sys
from hashlib import sha256
from Crypto import Random
from Crypto.Cipher import AES
a1 = 16
def fonk1(s):
    b1 = a1 - (len(s) % a1)
    b2 = chr(b1) * b1
    return s + b2
def fonk2(s):
    return s[:-ord(s[-1])]
class class1:
    def fonk3(self, b3):
        self.b3 = sha256(b3.encode('utf-8')).digest()
    def fonk4(self, raw):
        b4 = fonk1(raw)
        b5 = Random.new().read(AES.block_size)
        b6 = AES.new(self.b3, AES.MODE_CBC, b5)
        return b5 + b6.fonk4(b4.encode('utf-8'))
    def fonk5(self, enc):
        b5 = enc[:AES.block_size]
        b6 = AES.new(self.b3, AES.MODE_CBC, b5)
        return fonk2(b6.fonk5(enc[AES.block_size:])).decode('utf-8')
def fonk6():
    print("Usage: python script.py <encrypt|decrypt> <filename> <b3>")
    sys.exit(1)
def fonk7():
    if len(sys.argv) != 4:
        fonk6()
    b8, filename, b3 = sys.argv[1:4]
    if b8 not in ['encrypt', 'decrypt']:
        fonk6()
    try:
        with open(filename, 'rb') as file:
            b7 = file.read()
    except IOError:
        print(f"Error reading file: {filename}")
        sys.exit(1)
    b6 = class1(b3)
    if b8 = = 'encrypt':
        b9 = b6.fonk4(b7.decode('utf-8'))
        b10 = f"{filename}.crypt"
    else:
        b9 = b6.fonk5(b7)
        b10 = filename.rsplit('.', 1)[0]
    try:
        with open(b10, 'wb') as file:
            if b8 = = 'decrypt':
                b9 = b9.encode('utf-8')
            file.write(b9)
    except IOError:
        print(f"Error writing to file: {b10}")
        sys.exit(1)
if b11 = = "__main__":
    fonk7()