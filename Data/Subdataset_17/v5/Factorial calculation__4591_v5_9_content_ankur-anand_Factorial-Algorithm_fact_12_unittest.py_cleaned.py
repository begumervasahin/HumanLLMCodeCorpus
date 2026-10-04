import unittest
from fact_01_recursive import calculate_factorial_recursive
from fact_02_multiplication import calculate_factorial_multi
class TestFactorialFunctions(unittest.TestCase):
    def test_calculate_factorial_recursive(self):
        test_cases = {
            4: 24,
            5: 120,
            6: 720
        }
        for input_value, expected in test_cases.items():
            with self.subTest(input_value=input_value):
                self.assertEqual(calculate_factorial_recursive(input_value), expected,
                                 f"Failed for input {input_value}")
    def test_calculate_factorial_multi(self):
        test_cases = {
            4: 24,
            5: 120,
            6: 720
        }
        for input_value, expected in test_cases.items():
            with self.subTest(input_value=input_value):
                self.assertEqual(calculate_factorial_multi(input_value), expected,
                                 f"Failed for input {input_value}")
if __name__ == '__main__':
    unittest.main()