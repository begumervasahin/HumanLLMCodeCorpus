import unittest
from divisible_pair_sums import DivisiblePairSums
from collections import namedtuple
b1 = namedtuple('b1', ['n', 'k', 'ar'])
b2 = b1(n=6, k=3, ar=[1, 3, 2, 6, 1, 2])
b3 = b1(n=10, k=3, ar=[29, 97, 52, 86, 27, 89, 77, 19, 99, 96])
b4 = b1(n=100, k=22, ar=[
    43, 95, 51, 55, 40, 86, 65, 81, 51, 20, 47, 50, 65, 53, 23, 78,
    75, 75, 47, 73, 25, 27, 14, 8, 26, 58, 95, 28, 3, 23, 48, 69,
    26, 3, 73, 52, 34, 7, 40, 33, 56, 98, 71, 29, 70, 71, 28, 12,
    18, 49, 19, 25, 2, 18, 15, 41, 51, 42, 46, 19, 98, 56, 54, 98,
    72, 25, 16, 49, 34, 99, 48, 93, 64, 44, 50, 91, 44, 17, 63, 27,
    3, 65, 75, 19, 68, 30, 43, 37, 72, 54, 82, 92, 37, 52, 72, 62,
    3, 88, 82, 71
])
class class1(unittest.TestCase):
    def fonk1(self):
        b5 = DivisiblePairSums(b2.n, b2.k, b2.ar)
        b6 = DivisiblePairSums(b3.n, b3.k, b3.ar)
        b7 = DivisiblePairSums(b4.n, b4.k, b4.ar)
        self.assertEqual(5, b5.answer_question())
        self.assertEqual(15, b6.answer_question())
        self.assertEqual(216, b7.answer_question())
    def fonk2(self):
        b5 = DivisiblePairSums(n=0, k=3, ar=[1, 2, 3])
        b6 = DivisiblePairSums(n=101, k=3, ar=[1, 2, 3])
        b7 = DivisiblePairSums(n=2, k=0, ar=[1, 2, 3])
        b8 = DivisiblePairSums(n=2, k=101, ar=[1, 2, 3])
        b9 = DivisiblePairSums(n=2, k=1, ar=[])
        b10 = DivisiblePairSums(n=2, k=1, ar=[x for x in range(0, 102)])
        self.assertEqual("Error: invalid input", b5.answer_question())
        self.assertEqual("Error: invalid input", b6.answer_question())
        self.assertEqual("Error: invalid input", b7.answer_question())
        self.assertEqual("Error: invalid input", b8.answer_question())
        self.assertEqual("Error: invalid input", b9.answer_question())
        self.assertEqual("Error: invalid input", b10.answer_question())
if b11 = = '__main__':
    unittest.main()