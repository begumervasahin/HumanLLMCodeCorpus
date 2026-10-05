import unittest
from fact_01_recursive import calculate_factorial_recursive
from fact_02_multiplication import calculate_factorial_multi
class FactorialTesting(unittest.TestCase):
    def test_calculate_factorial_recursive(self):
        expected_results = {4: 24, 5: 120, 6: 720}
        for input_value, expected_result in expected_results.items():
            with self.subTest(input_value=input_value):
                self.assertEqual(calculate_factorial_recursive(input_value), expected_result)
    def test_calculate_factorial_multi(self):
        expected_results = {4: 24, 5: 120, 6: 720}
        for input_value, expected_result in expected_results.items():
            with self.subTest(input_value=input_value):
                self.assertEqual(calculate_factorial_multi(input_value), expected_result)
if __name__ == '__main__':
    unittest.main()