import unittest
from time import time
def read_words_from_file(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file]
def process_words(words, processor):
    return [processor(word) for word in words]
def process_word(word):
    if word == 'umbrella':
        return None
    return word + 'hi'
class TestGetFile(unittest.TestCase):
    def setUp(self):
        self.sample_words = [
            'Fish', 'hat', 'foo', 'cow', 'Cow', 'siamese.', 'Wonderland',
            'foo', 'toothpaste', 'bar', 'umbrella', 'foo\n', 'milky',
            '\'"flight-manual"\'', 'toothpick', 'bar', 'enough',
            'event-horizon', 'bar!'
        ]
    def test_getFile_basic(self):
        self.assertEqual(self.sample_words, read_words_from_file('small_test.txt'))
    def test_getFile_no_file(self):
        with self.assertRaises(FileNotFoundError):
            read_words_from_file('aaa.txt')
    def test_process_words(self):
        expected_output = [
            'Fishhi', 'hathi', 'foohi', 'cowhi', 'Cowhi', 'siamese.hi',
            'Wonderlandhi', 'foohi', 'toothpastehi', 'barhi'
        ]
        self.assertEqual(expected_output, process_words(self.sample_words, process_word))
    def test_performance(self):
        t0 = time()
        words = read_words_from_file('moby_test.txt')
        processed_words = process_words(words, process_word)
        self.assertLess(100000, len(processed_words))
        t1 = time()
        print('Moby import time sec:', t1 - t0)
if __name__ == '__main__':
    unittest.main()