class class1:
    def fonk1(self, b6):
        self.b1 = b6['b1'].lower()
        self.b2 = b6['b2'].lower()
        self.b3 = b6['b3'].lower()
        self.b4 = False
    def fonk2(self, word):
        b5 = word.lower()
        if self.b4:
            return ''
        if b5 = = self.b3:
            return None
        if b5 = = self.b2:
            self.b4 = True
            return ''
        if b5 = = self.b1:
            return ''
        return word
import unittest
class class2(unittest.TestCase):
    def fonk3(self):
        self.b6 = {'b1': 'foo', 'b2': 'Bar', 'b3': 'enough'}
        self.b7 = [
            'fish', 'hat', 'Foo', 'cow', 'SIAMESE', 'wonderland',
            'FOO', 'toothpaste', 'bar', 'umbrella', 'foo',
            'milky', 'flight-manual', 'toothpick', 'bar', 'enough',
            'event-horizon', 'bar'
        ]
        self.b8 = class1(self.b6)
    def fonk4(self):
        self.assertEqual(self.b8.b1, self.b6['b1'].lower())
        self.assertEqual(self.b8.b2, self.b6['b2'].lower())
        self.assertEqual(self.b8.b3, self.b6['b3'].lower())
    def fonk5(self):
        b9 = [
            'fish', 'hat', '', 'cow', 'siamese', 'wonderland',
            '', 'toothpaste', '', 'umbrella', '', 'milky',
            'flight-manual', 'toothpick', '', None, '', ''
        ]
        b10 = [self.b8.fonk2(word) for word in self.b7]
        self.assertEqual(b10, b9)
    def fonk6(self):
        b11 = ['cow', 'foo', 'fish', 'flamingo', 'enough', 'trampoline', 'apollo']
        b9 = ['cow', '', 'fish', 'flamingo', None, '', '']
        b10 = [self.b8.fonk2(word) for word in b11]
        self.assertEqual(b10, b9)
    def fonk7(self):
        b11 = ['cow', 'foo', 'fish', 'flamingo', 'trampoline', 'apollo']
        b9 = ['cow', '', 'fish', 'flamingo', 'trampoline', 'apollo']
        b10 = [self.b8.fonk2(word) for word in b11]
        self.assertEqual(b10, b9)
    def fonk8(self):
        b11 = [
            'cow', 'foo', 'fish', 'flamingo', 'trampoline',
            'apollo', 'cow', 'pancakes'
        ]
        b12 = {'b1': 'cow', 'b2': 'Flamingo', 'b3': 'flamingo'}
        b8 = class1(b12)
        b9 = ['', 'foo', 'fish', None, '', '', '', 'pancakes']
        b10 = [b8.fonk2(word) for word in b11]
        self.assertEqual(b10, b9)
if b13 = = '__main__':
    unittest.main()