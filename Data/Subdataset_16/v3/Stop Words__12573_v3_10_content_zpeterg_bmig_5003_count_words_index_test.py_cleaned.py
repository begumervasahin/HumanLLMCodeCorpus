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
            'b9': 'whale',
            'b10': 'mast',
            'b11': 'ffff9999',
        }
        b5 = getAndFilter(b4)
        self.assertGreater(len(b5), 190000)
        b6 = time()
        print('Moby total get & parse time (sec):', b6 - b3)
    def fonk2(self):
        b4 = {
            'file': 'small_test.txt',
            'b9': 'foo',
            'b10': 'bar',
            'b11': 'enough',
        }
        b7 = [
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
        b5 = getAndFilter(b4)
        self.assertEqual(b5, b7)
    def fonk3(self):
        run([
            '',
            '--b8 = small_test.txt',
            '--b9 = foo',
            '--b10 = bar',
            '--b11 = 007',
            '-s',
            f'--b12 = {b1}',
        ])
        b13 = (
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
            b14 = file.read()
            self.assertEqual(b14, b13)
    def fonk4(self):
        run([
            '',
            '--b8 = small_test.txt',
            '--b9 = foo',
            '--b10 = bar',
            '--b11 = 007',
            '-s',
            f'--b12 = {b2}',
            '-c',
        ])
        b15 = (
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
            b14 = file.read()
            self.assertEqual(b14, b15)
    def fonk5(self):
        if path.isfile(b1):
            remove(b1)
        if path.isfile(b2):
            remove(b2)
if b16 = = '__main__':
    unittest.main()