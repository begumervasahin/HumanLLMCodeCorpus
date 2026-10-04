import string
import unittest
from aes import b5
def fonk1(b4, i):
    return b4[b2:].zfill(i)
def fonk2(b4):
    b1 = ''
    for i in range(len(b4) + 1):
        if i % b2 = = 0:
            if i > b2:
                b1 += ' '
            b1 += b4[i - b2:i]
    return b1
def fonk3(filename):
    with open(filename, 'r') as fp:
        b3 = fp.readlines()
    return b3
def fonk4(b3):
    b4 = ''
    for line in b3:
        for word in line.split():
            b4 += word.strip(string.whitespace)
    b4 = '0x' + b4
    return int(b4, 16)
class class1(unittest.TestCase):
    def fonk5(self):
        b3 = fonk3('key.txt')
        self.b5 = b5(fonk4(b3))
    def fonk6(self):
        print("(for encryption)")
        b3 = fonk3('en_input.txt')
        b6 = fonk3('ctr.txt')
        b7 = int(fonk1(hex(fonk4(b6)), 64)[:32], 16)
        b8 = int(fonk1(hex(fonk4(b3)), 64)[:32], 16)
        b9 = self.b5.encrypt(b7)
        b10 = b9 ^ b8
        print(fonk2(fonk1(hex(b10), 32)).upper())
        b7 = int(fonk1(hex(fonk4(b6)), 64)[32:], 16)
        b8 = int(fonk1(hex(fonk4(b3)), 64)[32:], 16)
        b9 = self.b5.encrypt(b7)
        b11 = b9 ^ b8
        print(fonk2(fonk1(hex(b11), 32)).upper())
    def fonk7(self):
        print("(for decryption)")
        b3 = fonk3('de_input.txt')
        b6 = fonk3('ctr.txt')
        b7 = int(fonk1(hex(fonk4(b6)), 64)[:32], 16)
        b10 = int(fonk1(hex(fonk4(b3)), 64)[:32], 16)
        b12 = self.b5.encrypt(b7)
        b8 = b12 ^ b10
        print(fonk2(fonk1(hex(b8), 32)).upper())
        b7 = int(fonk1(hex(fonk4(b6)), 64)[32:], 16)
        b10 = int(fonk1(hex(fonk4(b3)), 64)[32:], 16)
        b12 = self.b5.encrypt(b7)
        b13 = b12 ^ b10
        print(fonk2(fonk1(hex(b13), 32)).upper())
if b14 = = '__main__':
    unittest.main()