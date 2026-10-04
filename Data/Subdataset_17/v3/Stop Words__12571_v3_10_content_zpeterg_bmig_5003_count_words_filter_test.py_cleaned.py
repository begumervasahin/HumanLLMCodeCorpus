class Filter:
    def __init__(self, options):
        self.start = options['start'].lower()
        self.stop = options['stop'].lower()
        self.finish = options['finish'].lower()
        self.stop_found = False
    def filter(self, word):
        word_lower = word.lower()
        if self.stop_found:
            return ''
        if word_lower == self.finish:
            return None
        if word_lower == self.stop:
            self.stop_found = True
            return ''
        if word_lower == self.start:
            return ''
        return word
import unittest
class FilterTest(unittest.TestCase):
    def setUp(self):
        self.options = {'start': 'foo', 'stop': 'Bar', 'finish': 'enough'}
        self.words = [
            'fish', 'hat', 'Foo', 'cow', 'SIAMESE', 'wonderland',
            'FOO', 'toothpaste', 'bar', 'umbrella', 'foo',
            'milky', 'flight-manual', 'toothpick', 'bar', 'enough',
            'event-horizon', 'bar'
        ]
        self.filter_instance = Filter(self.options)
    def test_constructor(self):
        self.assertEqual(self.filter_instance.start, self.options['start'].lower())
        self.assertEqual(self.filter_instance.stop, self.options['stop'].lower())
        self.assertEqual(self.filter_instance.finish, self.options['finish'].lower())
    def test_filter_simple(self):
        expected_result = [
            'fish', 'hat', '', 'cow', 'siamese', 'wonderland',
            '', 'toothpaste', '', 'umbrella', '', 'milky',
            'flight-manual', 'toothpick', '', None, '', ''
        ]
        generated_result = [self.filter_instance.filter(word) for word in self.words]
        self.assertEqual(generated_result, expected_result)
    def test_filter_sudden_stop(self):
        words_subset = ['cow', 'foo', 'fish', 'flamingo', 'enough', 'trampoline', 'apollo']
        expected_result = ['cow', '', 'fish', 'flamingo', None, '', '']
        generated_result = [self.filter_instance.filter(word) for word in words_subset]
        self.assertEqual(generated_result, expected_result)
    def test_filter_run_out(self):
        words_subset = ['cow', 'foo', 'fish', 'flamingo', 'trampoline', 'apollo']
        expected_result = ['cow', '', 'fish', 'flamingo', 'trampoline', 'apollo']
        generated_result = [self.filter_instance.filter(word) for word in words_subset]
        self.assertEqual(generated_result, expected_result)
    def test_filter_finish_same_as_stop(self):
        words_subset = [
            'cow', 'foo', 'fish', 'flamingo', 'trampoline',
            'apollo', 'cow', 'pancakes'
        ]
        modified_options = {'start': 'cow', 'stop': 'Flamingo', 'finish': 'flamingo'}
        filter_instance = Filter(modified_options)
        expected_result = ['', 'foo', 'fish', None, '', '', '', 'pancakes']
        generated_result = [filter_instance.filter(word) for word in words_subset]
        self.assertEqual(generated_result, expected_result)
if __name__ == '__main__':
    unittest.main()