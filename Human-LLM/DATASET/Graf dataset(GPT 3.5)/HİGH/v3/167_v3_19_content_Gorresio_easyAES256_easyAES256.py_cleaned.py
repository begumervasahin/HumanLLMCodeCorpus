import sys
from hashlib import sha256
from Crypto import Random
from Crypto.Cipher import AES
a1 = 16
def fonk1(text):
    b1 = a1 - len(text) % a1
    return text + chr(b1) * b1
def fonk2(text):
    return text[:-ord(text[-1])]
class class1:
    def fonk3(self, b2):
        self.b2 = sha256(b2.encode()).digest()
    def fonk4(self, b3):
        b3 = fonk1(b3)
        b4 = Random.new().read(AES.block_size)
        b5 = AES.new(self.b2, AES.MODE_CBC, b4)
        return b4 + b5.fonk4(b3.encode())
    def fonk5(self, ciphertext):
        b4 = ciphertext[:a1]
        b5 = AES.new(self.b2, AES.MODE_CBC, b4)
        return fonk2(b5.fonk5(ciphertext[a1:])).decode()
def fonk6():
    print("Usage: script.py <encrypt|decrypt> <filename> <b2>")
    sys.exit(1)
def fonk7():
    if len(sys.argv) != 4:
        fonk6()
    b7, filename, b2 = sys.argv[1:4]
    if b7 not in ["encrypt", "decrypt"]:
        fonk6()
    try:
        with open(filename, "rb") as f:
            b6 = f.read()
    except IOError as e:
        print(f"Failed to read '{filename}': {e}")
        sys.exit(1)
    b5 = class1(b2)
    if b7 = = "encrypt":
        b8 = b5.fonk4(b6.decode())
        b9 = f"{filename}.crypt"
    else:
        b8 = b5.fonk5(b6).encode()
        b9 = filename.rsplit('.', 1)[0]
    try:
        with open(b9, "wb") as f:
            f.write(b8)
    except IOError as e:
        print(f"Failed to write '{b9}': {e}")
        sys.exit(1)
if b10 = = "__main__":
    fonk7()