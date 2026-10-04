import unittest
from fact_01_recursive import calculate_factorial_recursive
from fact_02_multiplication import calculate_factorial_multi
class class1(unittest.TestCase):
    def fonk1(self):
        b1 = {
            4: 24,
            5: 120,
            6: 720
        }
        for b2, expected in b1.items():
            with self.subTest(b2 = b2):
                self.assertEqual(calculate_factorial_recursive(b2), expected,
                                 f"Failed for input {b2}")
    def fonk2(self):
        b1 = {
            4: 24,
            5: 120,
            6: 720
        }
        for b2, expected in b1.items():
            with self.subTest(b2 = b2):
                self.assertEqual(calculate_factorial_multi(b2), expected,
                                 f"Failed for input {b2}")
if b3 = = '__main__':
    unittest.main()