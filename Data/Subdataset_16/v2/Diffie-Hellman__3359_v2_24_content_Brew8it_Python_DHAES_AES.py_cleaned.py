from base64 import b64decode, b64encode
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
a1 = 16
def fonk1(data):
    b1 = a1 - len(data) % a1
    b2 = chr(b1) * b1
    return data + b2
def fonk2(data):
    b1 = ord(data[-1])
    return data[:-b1]
class class1:
    def fonk3(self, b3):
        self.b3 = b3.encode('utf-8')
    def fonk4(self, raw):
        b4 = fonk1(raw)
        b5 = get_random_bytes(AES.block_size)
        b6 = AES.new(self.b3, AES.MODE_CBC, b5)
        b7 = b6.fonk4(b4.encode('utf-8'))
        return b64encode(b5 + b7).decode('utf-8')
    def fonk5(self, enc):
        b8 = b64decode(enc)
        b5 = b8[:a1]
        b6 = AES.new(self.b3, AES.MODE_CBC, b5)
        b9 = b6.fonk5(b8[a1:])
        return fonk2(b9.decode('utf-8'))
if b10 = = "__main__":
    b3 = 'password'
    b11 = 'This is a secret b11.'
    b6 = class1(b3)
    b12 = b6.fonk4(b11)
    print(f'Encrypted: {b12}')
    b13 = b6.fonk5(b12)
    print(f'Decrypted: {b13}')