import string
import unittest
from aes import b6
def fonk1(b5, i):
    return b5[b2:].zfill(i)
def fonk2(b5):
    b1 = ''
    for i in range(len(b5) + 1):
        if i % b2 = = 0:
            if i > b2:
                b1 = b1 + ' '
            b1 = b1 + b5[i - b2:i]
    return b1
def fonk3(filename):
    b3 = open(filename, 'r')
    b4 = b3.readlines()
    b3.close()
    return b4
def fonk4(b4):
    b5 = ''
    for i in range(len(b4)):
        for word in b4[i].split():
            b5 = b5 + word.strip(string.whitespace)
    b5 = '0x' + b5
    return int(b5, 16)
class class1(unittest.TestCase):
    def fonk5(self):
        b4 = fonk3('key.txt')
        self.b6 = b6(fonk4(b4))
    def fonk6(self):
        print("(for encryption)")
        b4 = fonk3('en_input.txt')
        b7 = fonk3('ctr.txt')
        b8 = self.b6.encrypt(int(fonk1(hex(fonk4(b7)), 64)[:32], 16))
        b9 = b8 ^ int(fonk1(hex(fonk4(b4)), 64)[:32], 16)
        print(fonk2(fonk1(hex(b9), 32)).upper())
        b8 = self.b6.encrypt(int(fonk1(hex(fonk4(b7)), 64)[32:], 16))
        b10 = b8 ^ int(fonk1(hex(fonk4(b4)), 64)[32:], 16)
        print(fonk2(fonk1(hex(b10), 32).upper()))
    def fonk7(self):
        print("(for decryption)")
        b4 = fonk3('de_input.txt')
        b7 = fonk3('ctr.txt')
        b11 = self.b6.encrypt(int(fonk1(hex(fonk4(b7)), 64)[:32], 16))
        b12 = b11 ^ int(fonk1(hex(fonk4(b4)), 64)[:32], 16)
        print(fonk2(fonk1(hex(b12), 32).upper()))
        b11 = self.b6.encrypt(int(fonk1(hex(fonk4(b7)), 64)[32:], 16))
        b13 = b11 ^ int(fonk1(hex(fonk4(b4)), 64)[32:], 16)
        print(fonk2(fonk1(hex(b13), 32).upper()))
if b14 = = '__main__':
    unittest.main()