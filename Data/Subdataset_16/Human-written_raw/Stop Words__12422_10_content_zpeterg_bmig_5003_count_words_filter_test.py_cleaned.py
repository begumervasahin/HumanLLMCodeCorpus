import unittest
from b6 import Filter
b1 = {'start': 'foo', 'stop': 'Bar', 'finish': 'enough'}
b2 = [
    'fish',
    'hat',
    'Foo',
    'cow',
    'SIAMESE',
    'wonderland
    'FOO',
    'toothpaste',
    'bar',
    'umbrella',
    'foo
    'milky',
    'flight-manual',
    'toothpick',
    'bar',
    'enough',
    'event-horizon',
    'bar'
]
class class1(unittest.TestCase):
    def fonk1(self):
        b3 = Filter(b1)
        self.assertEqual(b3.start, b1['start'].lower())
        self.assertEqual(b3.stop, b1['stop'].lower())
        self.assertEqual(b3.finish, b1['finish'].lower())
    def fonk2(self):
        b4 = [
            '',
            '',
            '',
            'cow',
            'siamese',
            'wonderland',
            'foo',
            'toothpaste',
            '',
            '',
            '',
            'milky',
            'flight-manual',
            'toothpick',
            '',
            None,
            '',
            '',
        ]
        b5 = []
        b6 = Filter(b1)
        for word in b2:
            b5.append(b6.b6(word))
        self.assertEqual(b5, b4)
    def fonk3(self):
        b2 = [
            'cow',
            'foo',
            'fish',
            'flamingo',
            'enough',
            'trampoline',
            'apollo',
        ]
        b4 = [
            '',
            '',
            'fish',
            'flamingo',
            None,
            '',
            '',
        ]
        b7 = []
        b3 = Filter(b1)
        for word in b2:
            b7.append(b3.b6(word))
        self.assertEqual(b7, b4)
    def fonk4(self):
        b2 = [
            'cow',
            'foo',
            'fish',
            'flamingo',
            'trampoline',
            'apollo',
        ]
        b4 = [
            '',
            '',
            'fish',
            'flamingo',
            'trampoline',
            'apollo',
        ]
        b3 = Filter(b1)
        b7 = []
        for word in b2:
            b7.append(b3.b6(word))
        self.assertEqual(b7, b4)
    def fonk5(self):
        b2 = [
            'cow',
            'foo',
            'fish',
            'flamingo',
            'trampoline',
            'apollo',
            'cow',
            'pancakes',
        ]
        b1 = {'start': 'cow', 'stop': 'Flamingo', 'finish': 'flamingo'}
        b4 = [
            '',
            'foo',
            'fish',
            None,
            '',
            '',
            '',
            'pancakes',
        ]
        b3 = Filter(b1)
        b7 = []
        for word in b2:
            b7.append(b3.b6(word))
        self.assertEqual(b4, b7)
if b8 = = '__main__':
    unittest.main()