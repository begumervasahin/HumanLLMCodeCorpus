import unittest
from time import time
from os import remove, path
from index import getAndFilter, run
b1 = 'temp_output_for_index_test.json'
b2 = 'temp_output_for_index_test.csv'
class class1(unittest.TestCase):
    def fonk1(self):
        b3 = time()
        b4 = {
            'file': 'moby_test.txt',
            'b8': 'whale',
            'b9': 'mast',
            'b10': 'ffff9999',
        }
        self.assertLess(190000, len(getAndFilter(b4)))
        b5 = time()
        print('Moby total get & parse time sec:', b5 - b3)
    def fonk2(self):
        b4 = {
            'file': 'small_test.txt',
            'b8': 'foo',
            'b9': 'bar',
            'b10': 'enough',
        }
        b6 = [
            'cow',
            'cow',
            'siamese',
            'wonderland',
            'foo',
            'toothpaste',
            'milky',
            'flight-manual',
            'toothpick',
        ]
        self.assertEqual(getAndFilter(b4), b6)
    def fonk3(self):
        run([
            '',
            '--b7 = small_test.txt',
            '--b8 = foo',
            '--b9 = bar',
            '--b10 = 007',
            '-s',
            f'--b11 = {b1}',
        ])
        b12 = (
            '{\n'
            '    "cow": 2,\n'
            '    "siamese": 1,\n'
            '    "wonderland": 1,\n'
            '    "foo": 1,\n'
            '    "toothpaste": 1,\n'
            '    "milky": 1,\n'
            '    "flight-manual": 1,\n'
            '    "toothpick": 1\n'
            '}'
        )
        with open(b1, 'r') as file:
            b13 = file.read()
            self.assertEqual(b13, b12)
    def fonk4(self):
        run([
            '',
            '--b7 = small_test.txt',
            '--b8 = foo',
            '--b9 = bar',
            '--b10 = 007',
            '-s',
            f'--b11 = {b2}',
            '-c',
        ])
        b14 = (
            'Name,Count\n'
            'cow,2\n'
            'siamese,1\n'
            'wonderland,1\n'
            'foo,1\n'
            'toothpaste,1\n'
            'milky,1\n'
            'flight-manual,1\n'
            'toothpick,1\n'
        )
        with open(b2, 'r') as file:
            b13 = file.read()
            self.assertEqual(b13, b14)
    def fonk5(self):
        if path.isfile(b1):
            remove(b1)
        if path.isfile(b2):
            remove(b2)
if b15 = = '__main__':
    unittest.main()