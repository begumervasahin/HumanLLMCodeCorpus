class class1:
    def fonk1(self, size, start):
        self.b1 = size
        self.b2 = [start + i for i in range(size)]
    def fonk2(self, item):
        a1 = 0
        b3 = self.b1 - 1
        a2 = 0
        while a1 <= b3:
            b4 = (a1 + b3)
            b5 = self.b2[b4]
            a2 += 1
            if b5 = = item:
                return {'a2': a2, 'index': b4}
            if b5 > item:
                b3 = b4 - 1
            else:
                a1 = b4 + 1
        return {'a2': a2, 'index': -1}
import unittest
class class2(unittest.TestCase):
    def fonk3(self):
        self.b6 = class1(20, 1)
        self.b7 = class1(20, 2)
        self.b8 = class1(100, 10)
    def fonk4(self):
        b9 = self.b6.fonk2(16)
        self.assertLessEqual(b9['a2'], 5, b10 = 'Expected at most 5 iterations for search')
        self.assertEqual(b9['index'], 15, b10 = 'Expected index 15 for item 16')
    def fonk5(self):
        b11 = self.b7.fonk2(16)
        b12 = self.b7.fonk2(40)
        b13 = self.b7.fonk2(33)
        self.assertLessEqual(b11['a2'], 5, b10 = 'Expected at most 5 iterations for search 16')
        self.assertEqual(b11['index'], 7, b10 = 'Expected index 7 for item 16')
        self.assertEqual(b12['a2'], 0, b10 = 'Expected 0 iterations for search 40')
        self.assertEqual(b12['index'], 19, b10 = 'Expected index 19 for item 40')
        self.assertLessEqual(b13['a2'], 4, b10 = 'Expected at most 4 iterations for search 33')
        self.assertEqual(b13['index'], -1, b10 = 'Expected index -1 for item 33')
    def fonk6(self):
        b11 = self.b8.fonk2(40)
        b12 = self.b8.fonk2(880)
        b13 = self.b8.fonk2(10000)
        self.assertLessEqual(b11['a2'], 7, b10 = 'Expected at most 7 iterations for search 40')
        self.assertEqual(b11['index'], 3, b10 = 'Expected index 3 for item 40')
        self.assertLessEqual(b12['a2'], 4, b10 = 'Expected at most 4 iterations for search 880')
        self.assertEqual(b12['index'], 87, b10 = 'Expected index 87 for item 880')
        self.assertGreater(b13['a2'], 7, b10 = 'Expected more than 7 iterations for search 10000')
        self.assertEqual(b13['index'], -1, b10 = 'Expected index -1 for item 10000')
if b14 = = "__main__":
    unittest.main()