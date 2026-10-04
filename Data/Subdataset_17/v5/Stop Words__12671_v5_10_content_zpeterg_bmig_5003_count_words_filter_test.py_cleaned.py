import unittest
from filter import Filter
options = {'start': 'foo', 'stop': 'Bar', 'finish': 'enough'}
words = [
    'fish', 'hat', 'Foo', 'cow', 'SIAMESE', 'wonderland', 'FOO', 'toothpaste',
    'bar', 'umbrella', 'foo', 'milky', 'flight-manual', 'toothpick', 'bar',
    'enough', 'event-horizon', 'bar'
]
class FilterTest(unittest.TestCase):
    def setUp(self):
        self.filter_instance = Filter(options)
    def test_constructor(self):
        self.assertEqual(self.filter_instance.start, options['start'].lower())
        self.assertEqual(self.filter_instance.stop, options['stop'].lower())
        self.assertEqual(self.filter_instance.finish, options['finish'].lower())
    def test_filter_simple(self):
        expected_result = [
            '', '', '', 'cow', 'siamese', 'wonderland', 'foo', 'toothpaste', '',
            '', '', 'milky', 'flight-manual', 'toothpick', '', None, '', ''
        ]
        generated = [self.filter_instance.filter(word) for word in words]
        self.assertEqual(generated, expected_result)
    def test_filter_sudden_stop(self):
        test_words = ['cow', 'foo', 'fish', 'flamingo', 'enough', 'trampoline', 'apollo']
        expected_result = ['', '', 'fish', 'flamingo', None, '', '']
        generated = [self.filter_instance.filter(word) for word in test_words]
        self.assertEqual(generated, expected_result)
    def test_filter_run_out(self):
        test_words = ['cow', 'foo', 'fish', 'flamingo', 'trampoline', 'apollo']
        expected_result = ['', '', 'fish', 'flamingo', 'trampoline', 'apollo']
        generated = [self.filter_instance.filter(word) for word in test_words]
        self.assertEqual(generated, expected_result)
    def test_filter_finish_same_as_stop(self):
        test_words = [
            'cow', 'foo', 'fish', 'flamingo', 'trampoline', 'apollo', 'cow', 'pancakes'
        ]
        test_options = {'start': 'cow', 'stop': 'Flamingo', 'finish': 'flamingo'}
        expected_result = ['', 'foo', 'fish', None, '', '', '', 'pancakes']
        filter_instance = Filter(test_options)
        generated = [filter_instance.filter(word) for word in test_words]
        self.assertEqual(generated, expected_result)
if __name__ == '__main__':
    unittest.main()