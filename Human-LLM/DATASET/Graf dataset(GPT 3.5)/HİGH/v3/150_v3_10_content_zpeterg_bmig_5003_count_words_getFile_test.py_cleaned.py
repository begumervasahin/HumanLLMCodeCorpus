import unittest
from time import time
def fonk1(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file]
def fonk2(b5, processor):
    return [processor(b1) for b1 in b5]
def fonk3(b1):
    if b1 = = 'umbrella':
        return None
    return b1 + 'hi'
class class1(unittest.TestCase):
    def fonk4(self):
        self.b2 = [
            'Fish', 'hat', 'foo', 'cow', 'Cow', 'siamese.', 'Wonderland',
            'foo', 'toothpaste', 'bar', 'umbrella', 'foo\n', 'milky',
            '\'"flight-manual"\'', 'toothpick', 'bar', 'enough',
            'event-horizon', 'bar!'
        ]
    def fonk5(self):
        self.assertEqual(self.b2, fonk1('small_test.txt'))
    def fonk6(self):
        with self.assertRaises(FileNotFoundError):
            fonk1('aaa.txt')
    def fonk7(self):
        b3 = [
            'Fishhi', 'hathi', 'foohi', 'cowhi', 'Cowhi', 'siamese.hi',
            'Wonderlandhi', 'foohi', 'toothpastehi', 'barhi'
        ]
        self.assertEqual(b3, fonk2(self.b2, process_word))
    def fonk8(self):
        b4 = time()
        b5 = fonk1('moby_test.txt')
        b6 = fonk2(b5, process_word)
        self.assertLess(100000, len(b6))
        b7 = time()
        print('Moby import time sec:', b7 - b4)
if b8 = = '__main__':
    unittest.main()