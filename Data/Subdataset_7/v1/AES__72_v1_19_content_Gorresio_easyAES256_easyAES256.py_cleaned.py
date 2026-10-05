from hashlib import sha256
from Crypto import Random
from Crypto.Cipher import AES
import sys
a1 = 16
b1 = lambda s: s + (a1 - len(s) % a1) * chr(a1 - len(s) % a1)
b2 = lambda s: s[:-ord(s[-1])]
class class1:
    def fonk1(self, b3):
        self.b3 = sha256(b3.encode('utf-8')).digest()
    def fonk2(self, b4):
        b4 = b1(b4)
        b5 = Random.new().read(AES.block_size)
        b6 = AES.new(self.b3, AES.MODE_CBC, b5)
        return b5 + b6.fonk2(b4.encode('utf-8'))
    def fonk3(self, enc):
        b5 = enc[:AES.block_size]
        b6 = AES.new(self.b3, AES.MODE_CBC, b5)
        return b2(b6.fonk3(enc[AES.block_size:])).decode('utf-8')
def fonk4():
    print("Usage: easyAES256 <encrypt|decrypt> <b8> <b3>")
    exit()
try:
    b7 = sys.argv[1]
    b8 = sys.argv[2]
    b3 = sys.argv[3]
    if b7 not in ("encrypt", "decrypt"):
        fonk4()
except:
    fonk4()
try:
    with open(b8, "rb") as fp:
        b9 = fp.read()
except IOError:
    print(f"Error IO on \"{b8}\"")
    exit()
b10 = class1(b3)
if b7 = = "encrypt":
    b11 = b10.fonk2(b9.decode('utf-8'))
    b8 += ".crypt"
    b9 = b11
elif b7 = = "decrypt":
    b12 = b10.fonk3(b9)
    if not b12:
        print("Bad b3 or corrupted file.")
        exit()
    b8 = b8[:-6]
    b9 = b12.encode('utf-8')
try:
    with open(b8, "wb") as fp:
        fp.write(b9)
except IOError:
    print(f"Error IO on \"{b8}\"")
    exit()