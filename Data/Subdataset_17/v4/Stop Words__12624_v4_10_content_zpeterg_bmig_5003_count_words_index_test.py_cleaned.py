import unittest
from time import time
from os import remove, path
from index import getAndFilter, run
class IndexTest(unittest.TestCase):
    file_name = 'temp_output_for_index_test.json'
    file_name_csv = 'temp_output_for_index_test.csv'
    def test_speed_with_moby(self):
        start_time = time()
        options = {
            'file': 'moby_test.txt',
            'start': 'whale',
            'stop': 'mast',
            'finish': 'ffff9999',
        }
        result = getAndFilter(options)
        self.assertGreater(len(result), 190000)
        end_time = time()
        print('Moby total get & parse time sec:', end_time - start_time)
    def test_get_and_filter_simple(self):
        options = {
            'file': 'small_test.txt',
            'start': 'foo',
            'stop': 'bar',
            'finish': 'enough',
        }
        expected_result = [
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
        self.assertEqual(getAndFilter(options), expected_result)
    def test_index_run(self):
        run([
            '',
            '--input=small_test.txt',
            '--start=foo',
            '--stop=bar',
            '--finish=007',
            '-s',
            f'--output={self.file_name}',
        ])
        expected_result = (
            '{\n    "cow": 2,\n    "siamese": 1,\n    "wonderland": 1,\n    "foo": 1,\n    "toothpaste": 1,\n    "milky": 1,\n    "flight-manual": 1,\n    "toothpick": 1\n}'
        )
        with open(self.file_name, 'r') as file:
            contents = file.read()
            self.assertEqual(expected_result, contents)
    def test_index_run_csv(self):
        run([
            '',
            '--input=small_test.txt',
            '--start=foo',
            '--stop=bar',
            '--finish=007',
            '-s',
            f'--output={self.file_name_csv}',
            '-c',
        ])
        expected_result = (
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
        with open(self.file_name_csv, 'r') as file:
            contents = file.read()
            self.assertEqual(expected_result, contents)
    def tearDown(self):
        if path.isfile(self.file_name):
            remove(self.file_name)
        if path.isfile(self.file_name_csv):
            remove(self.file_name_csv)
if __name__ == '__main__':
    unittest.main()