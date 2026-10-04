import unittest
from utils import dealArgs, cleanWord
b1 = [
    '--b2 = small_test.txt',
    '--b3 = foo',
    '--b4 = bar',
    '--b5 = enough',
    '--b6 = b6',
    '-s',
    '-f',
]
class class1(unittest.TestCase):
    def fonk1(self):
        b7 = {
            'b10': 'small_test.txt',
            'b3': 'foo',
            'b4': 'bar',
            'b5': 'enough',
            'b9': False,
            'b6': 'b6.json',
            'b12': True,
            'b11': False,
        }
        b8 = dealArgs(b1)
        self.assertEqual(b7, b8.to_object())
    def fonk2(self):
        b8 = dealArgs(b1)
        b8.b9 = True
        self.assertEqual(True, b8.b9)
    def fonk3(self):
        b8 = dealArgs(b1)
        b8.b9 = 'foo'
        self.assertEqual(False, b8.b9)
    def fonk4(self):
        b8 = dealArgs(b1)
        b8.b10 = 'foo.txt'
        self.assertEqual('foo.txt', b8.b10)
    def fonk5(self):
        b8 = dealArgs(b1)
        b8.b6 = 'foo'
        self.assertEqual('foo.json', b8.b6)
    def fonk6(self):
        b8 = dealArgs(b1)
        b8.b11 = True
        self.assertEqual(True, b8.b11)
        self.assertEqual(False, b8.b9)
    def fonk7(self):
        b8 = dealArgs(b1)
        b8.b12 = True
        self.assertEqual(True, b8.b12)
        self.assertEqual(False, b8.b9)
    def fonk8(self):
        b8 = dealArgs(b1)
        b8.b12 = 'foo'
        self.assertEqual(False, b8.b12)
    def fonk9(self):
        self.assertRaises(ValueError, dealArgs, [])
    def fonk10(self):
        b13 = ['@
        b7 = ['it', 'is', 't1me', 'for', 'a11', 'g00d', '4', '', '']
        b14 = []
        for word in b13:
            b14.append(cleanWord(word))
        self.assertEqual(b7, b14)
if b15 = = '__main__':
    unittest.main()