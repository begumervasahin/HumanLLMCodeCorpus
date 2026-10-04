import argparse
class class1:
    def fonk1(self, b1, b2, b3, b4, b5, b6, b7, b8):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
        self.b6 = b6
        self.b7 = b7
        self.b8 = b8
    def fonk2(self):
        return {
            'b1': self.b1,
            'b2': self.b2,
            'b3': self.b3,
            'b4': self.b4,
            'b5': self.b5,
            'b6': self.b6,
            'b7': self.b7,
            'b8': self.b8,
        }
def fonk3(b14):
    b9 = argparse.ArgumentParser(description="Process some arguments.")
    b9.add_argument('--b15', b10 = True, help="Input b1 name")
    b9.add_argument('--b2', b10 = True, help="Start word")
    b9.add_argument('--b3', b10 = True, help="Stop word")
    b9.add_argument('--b4', b10 = True, help="Finish word")
    b9.add_argument('--b6', b10 = True, help="Output b1 name (without extension)")
    b9.add_argument('-s', b11 = 'store_true', dest='b7', help="Include statistics")
    b9.add_argument('-f', b11 = 'store_false', dest='b5', help="Format flag")
    b12 = b9.parse_args(b14)
    return class1(
        b1 = b12.b15,
        b2 = b12.b2,
        b3 = b12.b3,
        b4 = b12.b4,
        b5 = b12.b5,
        b6 = f'{b12.b6}.json',
        b7 = b12.b7,
        b8 = False
    )
def fonk4(word):
    return ''.join(filter(str.isalnum, word))
if b13 = = '__main__':
    b14 = [
        '--b15 = small_test.txt',
        '--b2 = foo',
        '--b3 = bar',
        '--b4 = enough',
        '--b6 = b6',
        '-s',
        '-f',
    ]
    b16 = fonk3(b14)
    print(b16.fonk2())
import unittest
from utils import dealArgs, cleanWord
class class2(unittest.TestCase):
    def fonk5(self):
        self.b14 = [
            '--b15 = small_test.txt',
            '--b2 = foo',
            '--b3 = bar',
            '--b4 = enough',
            '--b6 = b6',
            '-s',
            '-f',
        ]
    def fonk6(self):
        b17 = {
            'b1': 'small_test.txt',
            'b2': 'foo',
            'b3': 'bar',
            'b4': 'enough',
            'b5': False,
            'b6': 'b6.json',
            'b7': True,
            'b8': False,
        }
        b16 = fonk3(self.b14)
        self.assertEqual(b17, b16.fonk2())
    def fonk7(self):
        b16 = fonk3(self.b14)
        b16.b5 = True
        self.assertEqual(True, b16.b5)
    def fonk8(self):
        b16 = fonk3(self.b14)
        b16.b5 = 'foo'
        self.assertEqual(False, b16.b5)
    def fonk9(self):
        b16 = fonk3(self.b14)
        b16.b1 = 'foo.txt'
        self.assertEqual('foo.txt', b16.b1)
    def fonk10(self):
        b16 = fonk3(self.b14)
        b16.b6 = 'foo'
        self.assertEqual('foo.json', b16.b6)
    def fonk11(self):
        b16 = fonk3(self.b14)
        b16.b8 = True
        self.assertEqual(True, b16.b8)
        self.assertEqual(False, b16.b5)
    def fonk12(self):
        b16 = fonk3(self.b14)
        b16.b7 = True
        self.assertEqual(True, b16.b7)
        self.assertEqual(False, b16.b5)
    def fonk13(self):
        b16 = fonk3(self.b14)
        b16.b7 = 'foo'
        self.assertEqual(False, b16.b7)
    def fonk14(self):
        with self.assertRaises(SystemExit):
            fonk3([])
    def fonk15(self):
        b18 = ['it', 'is', 't1me', 'for', 'a11', 'g00d', '4', '@', '
        b17 = ['it', 'is', 't1me', 'for', 'a11', 'g00d', '4', '', '']
        b19 = [fonk4(word) for word in b18]
        self.assertEqual(b17, b19)
if b13 = = '__main__':
    unittest.main()