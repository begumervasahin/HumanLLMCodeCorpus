import unittest
from time import time
from getFile import getFile
words = [
    'Fish', 'hat', 'foo', 'cow', 'Cow', 'siamese.', 'Wonderland', 'foo', 'toothpaste',
    'bar', 'umbrella', 'foo\n', 'milky', '\'"flight-manual"\'', 'toothpick', 'bar',
    'enough', 'event-horizon', 'bar!'
]
def on_word(word):
    if word == 'umbrella':
        return None
    return word + 'hi'
class GetFileTest(unittest.TestCase):
    def test_getFile_basic(self):
        self.assertEqual(words, getFile('small_test.txt', lambda a: a))
    def test_getFile_no_file(self):
        self.assertRaises(FileNotFoundError, getFile, 'aaa.txt', lambda a: a)
    def test_getFile_modified(self):
        expected_result = ['Fishhi', 'hathi', 'foohi', 'cowhi', 'Cowhi', 'siamese.hi',
                           'Wonderlandhi', 'foohi', 'toothpastehi', 'barhi']
        self.assertEqual(expected_result, getFile('small_test.txt', on_word))
    def test_getFile_moby(self):
        start_time = time()
        result = getFile('moby_test.txt', on_word)
        self.assertLess(100000, len(result))
        end_time = time()
        print('Time taken to import Moby Dick (seconds):', end_time - start_time)
if __name__ == '__main__':
    unittest.main()