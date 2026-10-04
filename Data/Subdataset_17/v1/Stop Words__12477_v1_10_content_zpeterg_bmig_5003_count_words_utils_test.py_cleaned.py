import argparse
import json
class Options:
    def __init__(self, file, start, stop, finish, format, output, stats, csv):
        self.file = file
        self.start = start
        self.stop = stop
        self.finish = finish
        self.format = format
        self.output = output
        self.stats = stats
        self.csv = csv
    def to_object(self):
        return {
            'file': self.file,
            'start': self.start,
            'stop': self.stop,
            'finish': self.finish,
            'format': self.format,
            'output': self.output,
            'stats': self.stats,
            'csv': self.csv,
        }
def dealArgs(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True)
    parser.add_argument('--start', required=True)
    parser.add_argument('--stop', required=True)
    parser.add_argument('--finish', required=True)
    parser.add_argument('--output', required=True)
    parser.add_argument('-s', action='store_true', dest='stats')
    parser.add_argument('-f', action='store_false', dest='format')
    parsed_args = parser.parse_args(args)
    options = Options(
        file=parsed_args.input,
        start=parsed_args.start,
        stop=parsed_args.stop,
        finish=parsed_args.finish,
        format=parsed_args.format,
        output=f'{parsed_args.output}.json',
        stats=parsed_args.stats,
        csv=False
    )
    return options
def cleanWord(word):
    return ''.join(filter(str.isalnum, word))
if __name__ == '__main__':
    args = [
        '--input=small_test.txt',
        '--start=foo',
        '--stop=bar',
        '--finish=enough',
        '--output=output',
        '-s',
        '-f',
    ]
    options = dealArgs(args)
    print(options.to_object())
import unittest
from utils import dealArgs, cleanWord
args = [
    '--input=small_test.txt',
    '--start=foo',
    '--stop=bar',
    '--finish=enough',
    '--output=output',
    '-s',
    '-f',
]
class UtilsTest(unittest.TestCase):
    def test_deal_args(self):
        res = {
            'file': 'small_test.txt',
            'start': 'foo',
            'stop': 'bar',
            'finish': 'enough',
            'format': False,
            'output': 'output.json',
            'stats': True,
            'csv': False,
        }
        options = dealArgs(args)
        self.assertEqual(res, options.to_object())
    def test_change_format(self):
        options = dealArgs(args)
        options.format = True
        self.assertEqual(True, options.format)
    def test_change_format_override(self):
        options = dealArgs(args)
        options.format = 'foo'
        self.assertEqual(False, options.format)
    def test_change_file(self):
        options = dealArgs(args)
        options.file = 'foo.txt'
        self.assertEqual('foo.txt', options.file)
    def test_change_output_override(self):
        options = dealArgs(args)
        options.output = 'foo'
        self.assertEqual('foo.json', options.output)
    def test_change_csv_override(self):
        options = dealArgs(args)
        options.csv = True
        self.assertEqual(True, options.csv)
        self.assertEqual(False, options.format)
    def test_change_stats(self):
        options = dealArgs(args)
        options.stats = True
        self.assertEqual(True, options.stats)
        self.assertEqual(False, options.format)
    def test_change_stats_override(self):
        options = dealArgs(args)
        options.stats = 'foo'
        self.assertEqual(False, options.stats)
    def test_deal_no_args(self):
        self.assertRaises(SystemExit, dealArgs, [])
    def test_clean_word(self):
        arr = ['it', 'is', 't1me', 'for', 'a11', 'g00d', '4', '@', '
        res = ['it', 'is', 't1me', 'for', 'a11', 'g00d', '4', '', '']
        cleaned = []
        for word in arr:
            cleaned.append(cleanWord(word))
        self.assertEqual(res, cleaned)
if __name__ == '__main__':
    unittest.main()