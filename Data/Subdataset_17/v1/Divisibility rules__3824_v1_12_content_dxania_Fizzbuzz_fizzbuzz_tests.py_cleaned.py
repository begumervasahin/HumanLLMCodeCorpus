import unittest
def fizzbuzz(list1, list2):
    if not isinstance(list1, list) or not isinstance(list2, list):
        return "Invalid input"
    total_length = len(list1) + len(list2)
    if total_length % 3 == 0 and total_length % 5 == 0:
        return 'FizzBuzz'
    elif total_length % 3 == 0:
        return 'Fizz'
    elif total_length % 5 == 0:
        return 'Buzz'
    else:
        return str(total_length)
class FizzBuzzTest(unittest.TestCase):
    def test_non_list_inputs(self):
        self.assertEqual(fizzbuzz(5, 8), "Invalid input")
    def test_non_list_input(self):
        self.assertEqual(fizzbuzz([2, 3, 4], 7), "Invalid input")
    def test_fizz(self):
        self.assertEqual(fizzbuzz([1, 3, 4], ['a', 'b', 'c']), "Fizz")
    def test_buzz(self):
        self.assertEqual(fizzbuzz([4, 5, 4], [3, 4]), "Buzz")
    def test_fizz_buzz(self):
        self.assertEqual(fizzbuzz([1, 2, 3, 3, 4, 5, 5, 5, 5, 6], [7, 7, 4, 5, 9]), "FizzBuzz")
    def test_other_total(self):
        self.assertEqual(fizzbuzz([4, 5, 6], [3]), '4')
    def test_both_empty(self):
        self.assertEqual(fizzbuzz([1, 3, 5], []), "Fizz")
if __name__ == '__main__':
    unittest.main()