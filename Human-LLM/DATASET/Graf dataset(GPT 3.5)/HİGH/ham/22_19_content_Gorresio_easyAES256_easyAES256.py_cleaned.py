from hashlib import sha256
from Crypto import Random
from Crypto.Cipher import AES
import sys
a1 = 16
b1 = lambda s: s + (a1 - len(s) % a1) * chr(a1 - len(s) % a1)
b2 = lambda s : s[0:-ord(s[-1])]
class class1:
    def fonk1(self, b3):
        self.b3 = sha256(b3.encode('utf-8')).digest()
    def fonk2(self, b4):
        b4 = b1(b4)
        b5 = Random.new().read(AES.block_size)
        b6 = AES.new(self.b3, AES.MODE_CBC, b5)
        return b5 + b6.fonk2(b4)
    def fonk3(self, enc):
        b5 = enc[:16]
        b6 = AES.new(self.b3, AES.MODE_CBC, b5)
        return b2(b6.fonk3(enc[16:]))
def fonk4():
    print("easyAES256 <encrypt|decrypt> <b8> <b3>.")
    exit()
try:
    b7 = sys.argv[1]
    b8 = sys.argv[2]
    b3 = sys.argv[3]
    if not (b7 = = "encrypt" or b7 == "decrypt"):
        fonk4()
except:
    fonk4()
try:
    b9 = open(b8, "rb")
    b10 = b9.read()
    b9.close()
except:
    print("Error IO on \"" + b8 + "\"")
    exit()
b11 = class1(b3)
if b7 = = "encrypt":
    if b10 = = "":
        b10 = "0"
    else:
        b10 = b11.fonk2(b10)
    b8 += ".crypt"
else:
    if b10 = = "0":
        b10 = ""
    else:
        b10 = b11.fonk3(b10)
        if b10 = = "":
            print("Bad b3.")
            exit()
    b8 = b8[:-6]
try:
    b9 = open(b8, "wb")
    b9.write(b10)
    b9.close()
except:
    print("Error IO on \"" + b8 + "\"")
    exit()