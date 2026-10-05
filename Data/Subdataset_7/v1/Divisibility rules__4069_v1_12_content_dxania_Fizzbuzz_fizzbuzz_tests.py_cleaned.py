import unittest
from fizzbuzz import Fizzbuzz
class class1(unittest.TestCase):
    def fonk1(self):
        self.assertEqual(Fizzbuzz(5, 8), "Invalid input")
    def fonk2(self):
        self.assertEqual(Fizzbuzz([2, 3, 4], 7), "Invalid input")
    def fonk3(self):
        self.assertEqual(Fizzbuzz([1, 3, 4], ['a', 'b', 'c']), "fizz")
    def fonk4(self):
        self.assertEqual(Fizzbuzz([4, 5, 4], [3, 4]), "buzz")
    def fonk5(self):
        self.assertEqual(Fizzbuzz([1, 2, 3, 3, 4, 5, 5, 5, 5, 6],
                                  [7, 7, 4, 5, 9]), "Fizzbuzz")
    def fonk6(self):
        self.assertEqual(Fizzbuzz([4, 5, 6], [3]), 4)
    def fonk7(self):
        self.assertEqual(Fizzbuzz([1, 3, 5], []), "fizz")
if b1 = = '__main__':
    unittest.main()