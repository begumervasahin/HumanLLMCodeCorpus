import unittest
class TestIsPrime(unittest.TestCase):
    def test_zero(self):
        self.assertFalse(is_prime(0))
    def test_negative_numbers(self):
        self.assertFalse(is_prime(-1))
    def test_one_is_not_prime(self):
        self.assertFalse(is_prime(1))
    def test_prime_number(self):
        self.assertTrue(is_prime(13))
    def test_big_prime_number(self):
        self.assertTrue(is_prime(373))
class TestGeneratePrime(unittest.TestCase):
    def test_string_input(self):
        self.assertEqual(generate_prime('i'), 'Cannot input anything besides a whole number')
    def test_float_input(self):
        self.assertEqual(generate_prime(2.58), 'Cannot input anything besides a whole number')
    def test_negative_input(self):
        self.assertEqual(generate_prime(-2), "Retry with a positive integer greater than 1")
    def test_zero_input(self):
        self.assertEqual(generate_prime(0), "Retry with a positive integer greater than 1")
    def test_input_one(self):
        self.assertEqual(generate_prime(1), "Retry with a positive integer greater than 1")
if __name__ == '__main__':
    unittest.main()