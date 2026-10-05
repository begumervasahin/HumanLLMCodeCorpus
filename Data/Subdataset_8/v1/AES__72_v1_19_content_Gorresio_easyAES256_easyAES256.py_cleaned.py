from hashlib import sha256
from Crypto import Random
from Crypto.Cipher import AES
import sys
BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s: s[:-ord(s[-1])]
class AESCipher:
    def __init__(self, key):
        self.key = sha256(key.encode('utf-8')).digest()
    def encrypt(self, raw):
        raw = pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return iv + cipher.encrypt(raw.encode('utf-8'))
    def decrypt(self, enc):
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')
def InvalidArguments():
    print("Usage: easyAES256 <encrypt|decrypt> <filename> <key>")
    exit()
try:
    option = sys.argv[1]
    filename = sys.argv[2]
    key = sys.argv[3]
    if option not in ("encrypt", "decrypt"):
        InvalidArguments()
except:
    InvalidArguments()
try:
    with open(filename, "rb") as fp:
        data = fp.read()
except IOError:
    print(f"Error IO on \"{filename}\"")
    exit()
c = AESCipher(key)
if option == "encrypt":
    encrypted_data = c.encrypt(data.decode('utf-8'))
    filename += ".crypt"
    data = encrypted_data
elif option == "decrypt":
    decrypted_data = c.decrypt(data)
    if not decrypted_data:
        print("Bad key or corrupted file.")
        exit()
    filename = filename[:-6]
    data = decrypted_data.encode('utf-8')
try:
    with open(filename, "wb") as fp:
        fp.write(data)
except IOError:
    print(f"Error IO on \"{filename}\"")
    exit()