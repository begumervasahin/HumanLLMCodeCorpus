from collections import namedtuple
import unittest
Element = namedtuple('Element', ['index', 'value'])
Data = namedtuple('Data', ['n', 'k', 'ar'])
class DivisiblePairSums:
    def __init__(self, n, k, ar):
        self.n = n
        self.k = k
        self.ar = ar
        self.elements = [Element(index, value) for index, value in enumerate(ar)]
    def answer_question(self):
        if not self._validate_data():
            return "Error: invalid input"
        count = 0
        for i in range(len(self.elements)):
            for j in range(i + 1, len(self.elements)):
                if (self.elements[i].value + self.elements[j].value) % self.k == 0:
                    count += 1
        return count
    def _validate_data(self):
        return 2 <= self.n <= 100 and 1 <= self.k <= 100 and len(self.ar) <= 100
DATA1 = Data(n=6, k=3, ar=[1, 3, 2, 6, 1, 2])
DATA2 = Data(n=10, k=3, ar=[29, 97, 52, 86, 27, 89, 77, 19, 99, 96])
DATA3 = Data(n=100, k=22, ar=[
    43, 95, 51, 55, 40, 86, 65, 81, 51, 20, 47, 50, 65, 53, 23, 78,
    75, 75, 47, 73, 25, 27, 14, 8, 26, 58, 95, 28, 3, 23, 48, 69,
    26, 3, 73, 52, 34, 7, 40, 33, 56, 98, 71, 29, 70, 71, 28, 12,
    18, 49, 19, 25, 2, 18, 15, 41, 51, 42, 46, 19, 98, 56, 54, 98,
    72, 25, 16, 49, 34, 99, 48, 93, 64, 44, 50, 91, 44, 17, 63, 27,
    3, 65, 75, 19, 68, 30, 43, 37, 72, 54, 82, 92, 37, 52, 72, 62,
    3, 88, 82, 71
])
class DivisiblePairSumsTest(unittest.TestCase):
    def test_answer_question(self):
        dps1 = DivisiblePairSums(DATA1.n, DATA1.k, DATA1.ar)
        dps2 = DivisiblePairSums(DATA2.n, DATA2.k, DATA2.ar)
        dps3 = DivisiblePairSums(DATA3.n, DATA3.k, DATA3.ar)
        self.assertEqual(5, dps1.answer_question())
        self.assertEqual(15, dps2.answer_question())
        self.assertEqual(216, dps3.answer_question())
    def test_validate_input(self):
        invalid_cases = [
            DivisiblePairSums(0, 3, [1, 2, 3]),
            DivisiblePairSums(101, 3, [1, 2, 3]),
            DivisiblePairSums(2, 0, [1, 2, 3]),
            DivisiblePairSums(2, 101, [1, 2, 3]),
            DivisiblePairSums(2, 1, []),
            DivisiblePairSums(2, 1, [x for x in range(102)])
        ]
        for case in invalid_cases:
            self.assertEqual("Error: invalid input", case.answer_question())
if __name__ == "__main__":
    unittest.main()