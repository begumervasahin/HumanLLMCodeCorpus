import unittest
from filter import Filter
b1 = {'start': 'foo', 'stop': 'Bar', 'finish': 'enough'}
b2 = [
    'fish', 'hat', 'Foo', 'cow', 'SIAMESE', 'wonderland', 'FOO', 'toothpaste',
    'bar', 'umbrella', 'foo', 'milky', 'flight-manual', 'toothpick', 'bar',
    'enough', 'event-horizon', 'bar'
]
class class1(unittest.TestCase):
    def fonk1(self):
        self.b3 = Filter(b1)
    def fonk2(self):
        self.assertEqual(self.b3.start, b1['start'].lower())
        self.assertEqual(self.b3.stop, b1['stop'].lower())
        self.assertEqual(self.b3.finish, b1['finish'].lower())
    def fonk3(self):
        b4 = [
            '', '', '', 'cow', 'siamese', 'wonderland', 'foo', 'toothpaste', '',
            '', '', 'milky', 'flight-manual', 'toothpick', '', None, '', ''
        ]
        b5 = [self.b3.filter(word) for word in b2]
        self.assertEqual(b5, b4)
    def fonk4(self):
        b6 = ['cow', 'foo', 'fish', 'flamingo', 'enough', 'trampoline', 'apollo']
        b4 = ['', '', 'fish', 'flamingo', None, '', '']
        b5 = [self.b3.filter(word) for word in b6]
        self.assertEqual(b5, b4)
    def fonk5(self):
        b6 = ['cow', 'foo', 'fish', 'flamingo', 'trampoline', 'apollo']
        b4 = ['', '', 'fish', 'flamingo', 'trampoline', 'apollo']
        b5 = [self.b3.filter(word) for word in b6]
        self.assertEqual(b5, b4)
    def fonk6(self):
        b6 = [
            'cow', 'foo', 'fish', 'flamingo', 'trampoline', 'apollo', 'cow', 'pancakes'
        ]
        b7 = {'start': 'cow', 'stop': 'Flamingo', 'finish': 'flamingo'}
        b4 = ['', 'foo', 'fish', None, '', '', '', 'pancakes']
        b3 = Filter(b7)
        b5 = [b3.filter(word) for word in b6]
        self.assertEqual(b5, b4)
if b8 = = '__main__':
    unittest.main()