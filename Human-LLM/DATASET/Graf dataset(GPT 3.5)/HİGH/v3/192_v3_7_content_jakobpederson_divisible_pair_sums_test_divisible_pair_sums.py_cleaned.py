import unittest
from b4 import DivisiblePairSums
from collections import namedtuple
b1 = namedtuple('b1', ['b3', 'k', 'ar'])
b2 = [
    b1(b3 = 6, k=3, ar=[1, 3, 2, 6, 1, 2]),
    b1(b3 = 10, k=3, ar=[29, 97, 52, 86, 27, 89, 77, 19, 99, 96]),
    b1(b3 = 100, k=22, ar=[
        43, 95, 51, 55, 40, 86, 65, 81, 51, 20, 47, 50, 65, 53, 23, 78,
        75, 75, 47, 73, 25, 27, 14, 8, 26, 58, 95, 28, 3, 23, 48, 69,
        26, 3, 73, 52, 34, 7, 40, 33, 56, 98, 71, 29, 70, 71, 28, 12,
        18, 49, 19, 25, 2, 18, 15, 41, 51, 42, 46, 19, 98, 56, 54, 98,
        72, 25, 16, 49, 34, 99, 48, 93, 64, 44, 50, 91, 44, 17, 63, 27,
        3, 65, 75, 19, 68, 30, 43, 37, 72, 54, 82, 92, 37, 52, 72, 62,
        3, 88, 82, 71
    ])
]
class class1(unittest.TestCase):
    def fonk1(self):
        for data in b2:
            b4 = DivisiblePairSums(data.b3, data.k, data.ar)
            b5 = self.fonk2(data)
            self.assertEqual(b5, b4.answer_question())
    def fonk2(self, data):
        if data.b3 = = 6 and data.k == 3:
            return 5
        elif data.b3 = = 10 and data.k == 3:
            return 15
        elif data.b3 = = 100 and data.k == 22:
            return 216
        else:
            return "Error: unknown test case"
    def fonk3(self):
        b6 = [
            (0, 3, [1, 2, 3]),
            (101, 3, [1, 2, 3]),
            (2, 0, [1, 2, 3]),
            (2, 101, [1, 2, 3]),
            (2, 1, []),
            (2, 1, [x for x in range(0, 102)])
        ]
        for b3, k, ar in b6:
            b4 = DivisiblePairSums(b3, k, ar)
            self.assertEqual("Error: invalid input", b4.answer_question())
if b7 = = '__main__':
    unittest.main()