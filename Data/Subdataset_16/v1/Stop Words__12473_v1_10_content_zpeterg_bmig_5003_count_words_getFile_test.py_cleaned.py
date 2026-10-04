import unittest
from time import time
def fonk1(filename, callback):
    try:
        with open(filename, 'r') as f:
            b1 = f.read().split()
        return [callback(b2) for b2 in b1 if callback(b2) is not None]
    except FileNotFoundError:
        raise FileNotFoundError(f"File {filename} not found")
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
def fonk2(b2):
    if b2 = = 'umbrella':
        return None
    return b2 + 'hi'
class class1(unittest.TestCase):
    def fonk3(self):
        self.assertEqual(b1, fonk1('small_test.txt', lambda a: a))
    def fonk4(self):
        self.assertRaises(FileNotFoundError, getFile, 'aaa.txt', lambda a: a)
    def fonk5(self):
        b3 = ['Fishhi', 'hathi', 'foohi', 'cowhi', 'Cowhi', 'siamese.hi', 'Wonderlandhi', 'foohi', 'toothpastehi', 'barhi']
        self.assertEqual(b3, fonk1('small_test.txt', on_word))
    def fonk6(self):
        b4 = time()
        self.assertLess(100000, len(fonk1('moby_test.txt', on_word)))
        b5 = time()
        print('Moby import time sec:', b5 - b4)
if b6 = = '__main__':
    unittest.main()