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
options = {'start': 'foo', 'stop': 'Bar', 'finish': 'enough'}
words = [
    'fish',
    'hat',
    'Foo',
    'cow',
    'SIAMESE',
    'wonderland',
    'FOO',
    'toothpaste',
    'bar',
    'umbrella',
    'foo',
    'milky',
    'flight-manual',
    'toothpick',
    'bar',
    'enough',
    'event-horizon',
    'bar'
]
class FilterTest(unittest.TestCase):
    def test_constructor(self):
        filter_instance = Filter(options)
        self.assertEqual(filter_instance.start, options['start'].lower())
        self.assertEqual(filter_instance.stop, options['stop'].lower())
        self.assertEqual(filter_instance.finish, options['finish'].lower())
    def test_filter_simple(self):
        expected_result = [
            'fish',
            'hat',
            '',
            'cow',
            'siamese',
            'wonderland',
            '',
            'toothpaste',
            '',
            'umbrella',
            '',
            'milky',
            'flight-manual',
            'toothpick',
            '',
            None,
            '',
            ''
        ]
        generated_result = []
        filter_instance = Filter(options)
        for word in words:
            generated_result.append(filter_instance.filter(word))
        self.assertEqual(generated_result, expected_result)
    def test_filter_sudden_stop(self):
        words_subset = [
            'cow',
            'foo',
            'fish',
            'flamingo',
            'enough',
            'trampoline',
            'apollo',
        ]
        expected_result = [
            'cow',
            '',
            'fish',
            'flamingo',
            None,
            '',
            ''
        ]
        filtered_result = []
        filter_instance = Filter(options)
        for word in words_subset:
            filtered_result.append(filter_instance.filter(word))
        self.assertEqual(filtered_result, expected_result)
    def test_filter_run_out(self):
        words_subset = [
            'cow',
            'foo',
            'fish',
            'flamingo',
            'trampoline',
            'apollo',
        ]
        expected_result = [
            'cow',
            '',
            'fish',
            'flamingo',
            'trampoline',
            'apollo'
        ]
        filter_instance = Filter(options)
        filtered_result = []
        for word in words_subset:
            filtered_result.append(filter_instance.filter(word))
        self.assertEqual(filtered_result, expected_result)
    def test_filter_finish_same_as_stop(self):
        words_subset = [
            'cow',
            'foo',
            'fish',
            'flamingo',
            'trampoline',
            'apollo',
            'cow',
            'pancakes',
        ]
        modified_options = {'start': 'cow', 'stop': 'Flamingo', 'finish': 'flamingo'}
        expected_result = [
            '',
            'foo',
            'fish',
            None,
            '',
            '',
            '',
            'pancakes',
        ]
        filter_instance = Filter(modified_options)
        filtered_result = []
        for word in words_subset:
            filtered_result.append(filter_instance.filter(word))
        self.assertEqual(expected_result, filtered_result)
if __name__ == '__main__':
    unittest.main()