import string
import unittest
from b3 import AES
def fonk1(s, length):
    return s[2:].zfill(length)
def fonk2(s):
    return ' '.join(s[i:i+2] for i in range(0, len(s), 2)).upper()
def fonk3(filename):
    with open(filename, 'r') as file:
        return file.readlines()
def fonk4(b2):
    b1 = ''.join(word.strip(string.whitespace) for line in b2 for word in line.split())
    return int('0x' + b1, 16)
class class1(unittest.TestCase):
    def fonk5(self):
        b2 = fonk3('key.txt')
        self.b3 = AES(fonk4(b2))
    def fonk6(self):
        print("(for encryption)")
        b4 = fonk3('en_input.txt')
        b5 = fonk3('ctr.txt')
        b6 = fonk4(b5)
        b7 = fonk4(b4)
        b8 = self.b3.encrypt(b6)
        b9 = b8 ^ (b7 >> 64)
        print(fonk2(fonk1(hex(b9), 16)))
        b8 = self.b3.encrypt(b6 + 1)
        b10 = b8 ^ (b7 & ((1 << 64) - 1))
        print(fonk2(fonk1(hex(b10), 16)))
    def fonk7(self):
        print("(for decryption)")
        b11 = fonk3('de_input.txt')
        b5 = fonk3('ctr.txt')
        b6 = fonk4(b5)
        b12 = fonk4(b11)
        b13 = self.b3.encrypt(b6)
        b14 = b13 ^ (b12 >> 64)
        print(fonk2(fonk1(hex(b14), 16)))
        b13 = self.b3.encrypt(b6 + 1)
        b15 = b13 ^ (b12 & ((1 << 64) - 1))
        print(fonk2(fonk1(hex(b15), 16)))
if b16 = = '__main__':
    unittest.main()