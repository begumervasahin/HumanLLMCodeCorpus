import unittest
def isPrime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True
def GeneratePrime(number):
    if not isinstance(number, int):
        return 'Cannot input anything besides a whole number'
    if number <= 1:
        return "Retry with a positive integer greater than 1"
    return "Prime generation not implemented yet"
class Test_IsPrime(unittest.TestCase):
    def test_for_zero(self):
        self.assertFalse(isPrime(0))
    def test_negative_numbers(self):
        self.assertFalse(isPrime(-1))
    def test_one_is_prime(self):
        self.assertFalse(isPrime(1))
    def test_prime_number(self):
        "
        self.assertTrue(isPrime(13))
    def test_big_prime_number(self):
        self.assertTrue(isPrime(373))
class Test_GeneratePrime(unittest.TestCase):
    def test_string_type(self):
        self.assertEqual(GeneratePrime('i'), 'Cannot input anything besides a whole number')
    def test_float_type(self):
        self.assertEqual(GeneratePrime(2.58), 'Cannot input anything besides a whole number')
    def test_negative_input(self):
        self.assertEqual(GeneratePrime(-2), "Retry with a positive integer greater than 1")
    def test_zero_input(self):
        self.assertEqual(GeneratePrime(0), "Retry with a positive integer greater than 1")
    def test_input_one(self):
        self.assertEqual(GeneratePrime(1), "Retry with a positive integer greater than 1")
if __name__ == '__main__':
    unittest.main()