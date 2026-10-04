import unittest
from fizzbuzz import fizzbuzz
class TestFizzBuzz(unittest.TestCase):
    def test_non_list_inputs(self):
        self.assertEqual(fizzbuzz(5, 8), "Invalid input")
    def test_one_non_list_input(self):
        self.assertEqual(fizzbuzz([2, 3, 4], 7), "Invalid input")
    def test_fizz(self):
        self.assertEqual(fizzbuzz([1, 3, 4], ['a', 'b', 'c']), "Fizz")
    def test_buzz(self):
        self.assertEqual(fizzbuzz([4, 5, 4], [3, 4]), "Buzz")
    def test_fizzbuzz(self):
        list1 = [1, 2, 3, 3, 4, 5, 5, 5, 5, 6]
        list2 = [7, 7, 4, 5, 9]
        self.assertEqual(fizzbuzz(list1, list2), "FizzBuzz")
    def test_combined_length(self):
        self.assertEqual(fizzbuzz([4, 5, 6], [3]), "4")
    def test_empty_second_list(self):
        self.assertEqual(fizzbuzz([1, 3, 5], []), "Fizz")
if __name__ == '__main__':
    unittest.main()