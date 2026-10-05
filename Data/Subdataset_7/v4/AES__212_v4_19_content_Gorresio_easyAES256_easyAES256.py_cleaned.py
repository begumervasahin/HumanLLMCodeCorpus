import sys
from hashlib import sha256
from Crypto import Random
from Crypto.Cipher import AES
a1 = 16
def fonk1(s):
    b1 = a1 - len(s) % a1
    return s + (chr(b1) * b1)
def fonk2(s):
    return s[:-ord(s[-1])]
class class1:
    def fonk3(self, b2):
        self.b2 = sha256(b2.encode('utf-8')).digest()
    def fonk4(self, raw):
        b3 = fonk1(raw)
        b4 = Random.new().read(AES.block_size)
        b5 = AES.new(self.b2, AES.MODE_CBC, b4)
        return b4 + b5.fonk4(b3.encode('utf-8'))
    def fonk5(self, enc):
        b4 = enc[:AES.block_size]
        b5 = AES.new(self.b2, AES.MODE_CBC, b4)
        return fonk2(b5.fonk5(enc[AES.block_size:])).decode('utf-8')
def fonk6():
    print("Usage: script.py <encrypt|decrypt> <filename> <b2>")
    sys.exit(1)
def fonk7():
    if len(sys.argv) != 4:
        fonk6()
    b7, filename, b2 = sys.argv[1], sys.argv[2], sys.argv[3]
    if b7 not in ['encrypt', 'decrypt']:
        fonk6()
    try:
        with open(filename, 'rb') as file:
            b6 = file.read()
    except IOError:
        print(f"Error reading file: {filename}")
        sys.exit(1)
    b5 = class1(b2)
    if b7 = = 'encrypt':
        b8 = b5.fonk4(b6.decode('utf-8'))
        b9 = f"{filename}.crypt"
    else:
        b8 = b5.fonk5(b6)
        b9 = filename.rsplit('.', 1)[0]
    try:
        with open(b9, 'wb') as file:
            file.write(b8.encode('utf-8') if b7 = = 'decrypt' else b8)
    except IOError:
        print(f"Error writing to file: {b9}")
        sys.exit(1)
if b10 = = "__main__":
    fonk7()