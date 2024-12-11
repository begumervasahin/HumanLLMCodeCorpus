import unittest
from time import time
from getFile import getFile
b1 = [
    'Fish',
    'hat',
    'foo',
    'cow',
    'Cow',
    'siamese.',
    'Wonderland',
    'foo',
    'toothpaste',
    'bar',
    'umbrella',
    'foo\n',
    'milky',
    '\'"flight-manual"\'',
    'toothpick',
    'bar',
    'enough',
    'event-horizon',
    'bar!'
]
def fonk1(b2):
    if b2 = = 'umbrella':
        return None
    return b2 + 'hi'
class class1(unittest.TestCase):
    def fonk2(self):
        self.assertEqual(b1, getFile('small_test.txt', lambda a: a))
    def fonk3(self):
        self.assertRaises(FileNotFoundError, getFile, 'aaa.txt', lambda a: a)
    def fonk4(self):
        b3 = ['Fishhi', 'hathi', 'foohi', 'cowhi', 'Cowhi', 'siamese.hi', 'Wonderlandhi', 'foohi', 'toothpastehi', 'barhi']
        self.assertEqual(b3, getFile('small_test.txt', on_word))
    def fonk5(self):
        b4 = time()
        self.assertLess(100000, len(getFile('moby_test.txt', on_word)))
        b5 = time()
        print('Moby import time sec:', b5 - b4)
if b6 = = '__main__':
    unittest.main()