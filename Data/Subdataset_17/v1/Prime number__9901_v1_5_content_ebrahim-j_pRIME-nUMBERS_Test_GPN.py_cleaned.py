import unittest
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def generate_prime(n):
    if isinstance(n, str) or isinstance(n, float):
        return 'Cannot input anything besides a whole number'
    if n <= 1:
        return "Retry with a positive integer greater than 1"
    return n if is_prime(n) else "Not a prime number"
class TestIsPrime(unittest.TestCase):
    def test_for_zero(self):
        self.assertFalse(is_prime(0))
    def test_negative_numbers(self):
        self.assertFalse(is_prime(-1))
    def test_one_is_prime(self):
        self.assertFalse(is_prime(1))
    def test_prime_number(self):
        self.assertTrue(is_prime(13))
    def test_big_prime_number(self):
        self.assertTrue(is_prime(373))
class TestGeneratePrime(unittest.TestCase):
    def test_string_type(self):
        self.assertEqual(generate_prime('i'), 'Cannot input anything besides a whole number')
    def test_float_type(self):
        self.assertEqual(generate_prime(2.58), 'Cannot input anything besides a whole number')
    def test_negative_input(self):
        self.assertEqual(generate_prime(-2), "Retry with a positive integer greater than 1")
    def test_zero_input(self):
        self.assertEqual(generate_prime(0), "Retry with a positive integer greater than 1")
    def test_input_one(self):
        self.assertEqual(generate_prime(1), "Retry with a positive integer greater than 1")
if __name__ == '__main__':
    unittest.main()