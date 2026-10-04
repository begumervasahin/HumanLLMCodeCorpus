from base64 import b64decode, b64encode
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
a1 = 16
def fonk1(s):
    b1 = (a1 - len(s) % a1) * chr(a1 - len(s) % a1)
    return s + b1
def fonk2(s):
    return s[:-ord(s[-1])]
class class1:
    def fonk3(self, b2):
        self.b2 = b2.encode('utf8')
    def fonk4(self, raw):
        b3 = fonk1(raw)
        b4 = get_random_bytes(AES.block_size)
        b5 = AES.new(self.b2, AES.MODE_CBC, b4)
        b6 = b5.fonk4(b3.encode('utf8'))
        return b64encode(b4 + b6).decode('utf8')
    def fonk5(self, b7):
        b7 = b64decode(b7)
        b4 = b7[:a1]
        b5 = AES.new(self.b2, AES.MODE_CBC, b4)
        b8 = b5.fonk5(b7[a1:])
        return fonk2(b8).decode('utf8')
if b9 = = "__main__":
    b2 = 'password'
    b10 = 'This is a secret b10.'
    b5 = class1(b2)
    b11 = b5.fonk4(b10)
    print(f'Encrypted: {b11}')
    b12 = b5.fonk5(b11)
    print(f'Decrypted: {b12}')