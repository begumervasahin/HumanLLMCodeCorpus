import unittest
from time import time
from os import remove, path
from index import getAndFilter, run
JSON_OUTPUT_FILE = 'temp_output_for_index_test.json'
CSV_OUTPUT_FILE = 'temp_output_for_index_test.csv'
class IndexTest(unittest.TestCase):
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
        print('Moby total get & parse time (sec):', end_time - start_time)
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
        result = getAndFilter(options)
        self.assertEqual(result, expected_result)
    def test_index_run(self):
        run([
            '',
            '--input=small_test.txt',
            '--start=foo',
            '--stop=bar',
            '--finish=007',
            '-s',
            f'--output={JSON_OUTPUT_FILE}',
        ])
        expected_output = (
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
        with open(JSON_OUTPUT_FILE, 'r') as file:
            contents = file.read()
            self.assertEqual(contents, expected_output)
    def test_index_run_csv(self):
        run([
            '',
            '--input=small_test.txt',
            '--start=foo',
            '--stop=bar',
            '--finish=007',
            '-s',
            f'--output={CSV_OUTPUT_FILE}',
            '-c',
        ])
        expected_output_csv = (
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
        with open(CSV_OUTPUT_FILE, 'r') as file:
            contents = file.read()
            self.assertEqual(contents, expected_output_csv)
    def tearDown(self):
        if path.isfile(JSON_OUTPUT_FILE):
            remove(JSON_OUTPUT_FILE)
        if path.isfile(CSV_OUTPUT_FILE):
            remove(CSV_OUTPUT_FILE)
if __name__ == '__main__':
    unittest.main()