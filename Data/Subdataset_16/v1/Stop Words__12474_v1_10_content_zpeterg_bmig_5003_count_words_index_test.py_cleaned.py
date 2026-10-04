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
        b6 = '{\n    "cow": 2,\n    "siamese": 1,\n    "wonderland": 1,\n    "foo": 1,\n    "toothpaste": 1,\n    "milky": 1,\n    "flight-manual": 1,\n    "toothpick": 1\n}'
        with open(b1, 'r') as file:
            b12 = file.read()
            self.assertEqual(b6, b12)
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
        b6 = 'Name,Count\ncow,2\nsiamese,1\nwonderland,1\nfoo,1\ntoothpaste,1\nmilky,1\nflight-manual,1\ntoothpick,1\n'
        with open(b2, 'r') as file:
            b12 = file.read()
            self.assertEqual(b6, b12)
    def fonk5(self):
        if path.isfile(b1):
            remove(b1)
        if path.isfile(b2):
            remove(b2)
if b13 = = '__main__':
    unittest.main()