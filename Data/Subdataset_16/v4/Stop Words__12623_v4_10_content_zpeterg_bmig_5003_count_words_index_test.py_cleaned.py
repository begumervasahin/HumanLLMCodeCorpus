import unittest
from time import time
from os import remove, path
from index import getAndFilter, run
class class1(unittest.TestCase):
    b1 = 'temp_output_for_index_test.json'
    b2 = 'temp_output_for_index_test.csv'
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
        print('Moby total get & parse time sec:', b6 - b3)
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
        self.assertEqual(getAndFilter(b4), b7)
    def fonk3(self):
        run([
            '',
            '--b8 = small_test.txt',
            '--b9 = foo',
            '--b10 = bar',
            '--b11 = 007',
            '-s',
            f'--b12 = {self.b1}',
        ])
        b7 = (
            '{\n    "cow": 2,\n    "siamese": 1,\n    "wonderland": 1,\n    "foo": 1,\n    "toothpaste": 1,\n    "milky": 1,\n    "flight-manual": 1,\n    "toothpick": 1\n}'
        )
        with open(self.b1, 'r') as file:
            b13 = file.read()
            self.assertEqual(b7, b13)
    def fonk4(self):
        run([
            '',
            '--b8 = small_test.txt',
            '--b9 = foo',
            '--b10 = bar',
            '--b11 = 007',
            '-s',
            f'--b12 = {self.b2}',
            '-c',
        ])
        b7 = (
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
        with open(self.b2, 'r') as file:
            b13 = file.read()
            self.assertEqual(b7, b13)
    def fonk5(self):
        if path.isfile(self.b1):
            remove(self.b1)
        if path.isfile(self.b2):
            remove(self.b2)
if b14 = = '__main__':
    unittest.main()