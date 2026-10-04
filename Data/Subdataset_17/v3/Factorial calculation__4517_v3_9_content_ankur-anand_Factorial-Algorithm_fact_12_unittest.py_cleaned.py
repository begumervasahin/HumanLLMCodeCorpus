import unittest
from fact_01_recursive import calculate_factorial_recursive
from fact_02_multiplication import calculate_factorial_multi
class TestFactorialFunctions(unittest.TestCase):
    def test_calculate_factorial_recursive(self):
        self.assertEqual(calculate_factorial_recursive(4), 24, "Failed for input 4")
        self.assertEqual(calculate_factorial_recursive(5), 120, "Failed for input 5")
        self.assertEqual(calculate_factorial_recursive(6), 720, "Failed for input 6")
    def test_calculate_factorial_multi(self):
        self.assertEqual(calculate_factorial_multi(4), 24, "Failed for input 4")
        self.assertEqual(calculate_factorial_multi(5), 120, "Failed for input 5")
        self.assertEqual(calculate_factorial_multi(6), 720, "Failed for input 6")
if __name__ == '__main__':
    unittest.main()