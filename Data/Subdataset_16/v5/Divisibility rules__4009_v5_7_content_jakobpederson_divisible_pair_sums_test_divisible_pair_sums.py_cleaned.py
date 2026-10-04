import unittest
from collections import namedtuple
from divisible_pair_sums import DivisiblePairSums
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
        b4 = [5, 15, 216]
        for b5, expected in zip(b2, b4):
            with self.subTest(b5 = b5):
                b6 = DivisiblePairSums(b5.b3, b5.k, b5.ar)
                self.assertEqual(b6.answer_question(), expected)
    def fonk2(self):
        b7 = [
            (0, 3, [1, 2, 3]),
            (101, 3, [1, 2, 3]),
            (2, 0, [1, 2, 3]),
            (2, 101, [1, 2, 3]),
            (2, 1, []),
            (2, 1, [x for x in range(102)])
        ]
        for b3, k, ar in b7:
            with self.subTest(b3 = b3, k=k, ar=ar):
                b6 = DivisiblePairSums(b3, k, ar)
                self.assertEqual(b6.answer_question(), "Error: invalid input")
if b8 = = "__main__":
    unittest.main()