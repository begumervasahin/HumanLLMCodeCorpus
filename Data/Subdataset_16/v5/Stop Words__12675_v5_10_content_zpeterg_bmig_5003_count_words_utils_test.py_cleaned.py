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
        self.b7 = {
            'b10': 'small_test.txt',
            'b3': 'foo',
            'b4': 'bar',
            'b5': 'enough',
            'b9': False,
            'b6': 'b6.json',
            'b12': True,
            'b11': False,
        }
        self.b8 = dealArgs(b1)
    def fonk2(self):
        self.assertEqual(self.b7, self.b8.to_object())
    def fonk3(self):
        self.b8.b9 = True
        self.assertTrue(self.b8.b9)
    def fonk4(self):
        self.b8.b9 = 'foo'
        self.assertFalse(self.b8.b9)
    def fonk5(self):
        self.b8.b10 = 'foo.txt'
        self.assertEqual('foo.txt', self.b8.b10)
    def fonk6(self):
        self.b8.b6 = 'foo'
        self.assertEqual('foo.json', self.b8.b6)
    def fonk7(self):
        self.b8.b11 = True
        self.assertTrue(self.b8.b11)
        self.assertFalse(self.b8.b9)
    def fonk8(self):
        self.b8.b12 = True
        self.assertTrue(self.b8.b12)
        self.assertFalse(self.b8.b9)
    def fonk9(self):
        self.b8.b12 = 'foo'
        self.assertFalse(self.b8.b12)
    def fonk10(self):
        self.assertRaises(ValueError, dealArgs, [])
    def fonk11(self):
        b13 = ['it!', 'is', 't1me', 'for', 'a11', 'g00d', '4', 'all', 'men']
        b14 = ['it', 'is', 't1me', 'for', 'a11', 'g00d', '4', 'all', 'men']
        b15 = [cleanWord(word) for word in b13]
        self.assertEqual(b14, b15)
if b16 = = '__main__':
    unittest.main()