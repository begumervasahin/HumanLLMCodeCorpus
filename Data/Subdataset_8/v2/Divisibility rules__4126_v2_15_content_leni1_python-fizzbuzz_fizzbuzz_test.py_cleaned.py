import unittest
from fizzbuzz import fizzbuzz
class FizzbuzzTest(unittest.TestCase):
    def test_non_list_inputs(self):
        result = fizzbuzz(5, 8)
        self.assertEqual(result, "Invalid input")
    def test_non_list_input(self):
        result = fizzbuzz([2, 3, 4], 7)
        self.assertEqual(result, "Invalid input")
    def test_fizz(self):
        result = fizzbuzz([1, 3, 4], ['a', 'b', 'c'])
        self.assertEqual(result, "fizz")
    def test_buzz(self):
        result = fizzbuzz([4, 5, 4], [3, 4])
        self.assertEqual(result, "buzz")
    def test_fizz_buzz(self):
        result = fizzbuzz([1, 2, 3, 3, 4, 5, 5, 5, 5, 6], [7, 7, 4, 5, 9])
        self.assertEqual(result, "fizzbuzz")
    def test_other_total(self):
        result = fizzbuzz([4, 5, 6], [3])
        self.assertEqual(result, 4)
    def test_both_empty(self):
        result = fizzbuzz([1, 3, 5], [])
        self.assertEqual(result, "fizz")
if __name__ == '__main__':
    unittest.main()