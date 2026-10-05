import unittest
from divisible_pair_sums import DivisiblePairSums
from collections import namedtuple
TestData = namedtuple('TestData', ['n', 'k', 'ar'])
TEST_DATA_1 = TestData(n=6, k=3, ar=[1, 3, 2, 6, 1, 2])
TEST_DATA_2 = TestData(n=10, k=3, ar=[29, 97, 52, 86, 27, 89, 77, 19, 99, 96])
TEST_DATA_3 = TestData(n=100, k=22, ar=[
    43, 95, 51, 55, 40, 86, 65, 81, 51, 20, 47, 50, 65, 53, 23, 78,
    75, 75, 47, 73, 25, 27, 14, 8, 26, 58, 95, 28, 3, 23, 48, 69,
    26, 3, 73, 52, 34, 7, 40, 33, 56, 98, 71, 29, 70, 71, 28, 12,
    18, 49, 19, 25, 2, 18, 15, 41, 51, 42, 46, 19, 98, 56, 54, 98,
    72, 25, 16, 49, 34, 99, 48, 93, 64, 44, 50, 91, 44, 17, 63, 27,
    3, 65, 75, 19, 68, 30, 43, 37, 72, 54, 82, 92, 37, 52, 72, 62,
    3, 88, 82, 71
])
class TestDivisiblePairSums(unittest.TestCase):
    def test_answer_question(self):
        test_1 = DivisiblePairSums(TEST_DATA_1.n, TEST_DATA_1.k, TEST_DATA_1.ar)
        test_2 = DivisiblePairSums(TEST_DATA_2.n, TEST_DATA_2.k, TEST_DATA_2.ar)
        test_3 = DivisiblePairSums(TEST_DATA_3.n, TEST_DATA_3.k, TEST_DATA_3.ar)
        self.assertEqual(5, test_1.answer_question())
        self.assertEqual(15, test_2.answer_question())
        self.assertEqual(216, test_3.answer_question())
    def test_validate_input(self):
        test_4 = DivisiblePairSums(n=0, k=3, ar=[1, 2, 3])
        test_5 = DivisiblePairSums(n=101, k=3, ar=[1, 2, 3])
        test_6 = DivisiblePairSums(n=2, k=0, ar=[1, 2, 3])
        test_7 = DivisiblePairSums(n=2, k=101, ar=[1, 2, 3])
        test_8 = DivisiblePairSums(n=2, k=1, ar=[])
        test_9 = DivisiblePairSums(n=2, k=1, ar=[x for x in range(0, 102)])
        self.assertEqual("Error: invalid input", test_4.answer_question())
        self.assertEqual("Error: invalid input", test_5.answer_question())
        self.assertEqual("Error: invalid input", test_6.answer_question())
        self.assertEqual("Error: invalid input", test_7.answer_question())
        self.assertEqual("Error: invalid input", test_8.answer_question())
        self.assertEqual("Error: invalid input", test_9.answer_question())
if __name__ == '__main__':
    unittest.main()