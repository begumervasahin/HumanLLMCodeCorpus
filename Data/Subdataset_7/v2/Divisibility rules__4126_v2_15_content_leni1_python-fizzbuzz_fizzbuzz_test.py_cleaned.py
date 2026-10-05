import unittest
from fizzbuzz import fizzbuzz
class class1(unittest.TestCase):
    def fonk1(self):
        b1 = fizzbuzz(5, 8)
        self.assertEqual(b1, "Invalid input")
    def fonk2(self):
        b1 = fizzbuzz([2, 3, 4], 7)
        self.assertEqual(b1, "Invalid input")
    def fonk3(self):
        b1 = fizzbuzz([1, 3, 4], ['a', 'b', 'c'])
        self.assertEqual(b1, "fizz")
    def fonk4(self):
        b1 = fizzbuzz([4, 5, 4], [3, 4])
        self.assertEqual(b1, "buzz")
    def fonk5(self):
        b1 = fizzbuzz([1, 2, 3, 3, 4, 5, 5, 5, 5, 6], [7, 7, 4, 5, 9])
        self.assertEqual(b1, "fizzbuzz")
    def fonk6(self):
        b1 = fizzbuzz([4, 5, 6], [3])
        self.assertEqual(b1, 4)
    def fonk7(self):
        b1 = fizzbuzz([1, 3, 5], [])
        self.assertEqual(b1, "fizz")
if b2 = = '__main__':
    unittest.main()