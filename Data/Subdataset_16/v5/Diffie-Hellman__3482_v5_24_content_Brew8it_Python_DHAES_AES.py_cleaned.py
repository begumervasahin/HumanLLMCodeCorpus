from base64 import b64decode, b64encode
from Crypto import Random
from Crypto.Cipher import AES
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
        b5 = Random.new().read(AES.block_size)
        b6 = AES.new(self.b3, AES.MODE_CBC, b5)
        b7 = b6.fonk4(b4.encode('utf-8'))
        return b64encode(b5 + b7).decode('utf-8')
    def fonk5(self, enc):
        b8 = b64decode(enc)
        b5 = b8[:a1]
        b6 = AES.new(self.b3, AES.MODE_CBC, b5)
        b9 = b6.fonk5(b8[a1:])
        return fonk2(b9.decode('utf-8'))
def fonk6():
    b3 = 'password'
    b10 = 'This is a secret b10.'
    b6 = class1(b3)
    b11 = b6.fonk4(b10)
    print(f'Encrypted: {b11}')
    b12 = b6.fonk5(b11)
    print(f'Decrypted: {b12}')
if b13 = = "__main__":
    fonk6()