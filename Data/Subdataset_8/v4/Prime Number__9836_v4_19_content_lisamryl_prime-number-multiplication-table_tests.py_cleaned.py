import unittest
from prime_number_multiplication_table import *
class PrimeNumberUnitTests(unittest.TestCase):
    def setUp(self):
        print("Running unit tests for prime number functions")
    def test_is_prime(self):
        self.assertFalse(is_prime(1))
        self.assertTrue(is_prime(2))
        self.assertFalse(is_prime(4))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(104729))
        self.assertFalse(is_prime(104728))
    def test_is_prime_exception_handling(self):
        with self.assertRaises(Exception) as cm:
            is_prime(0)
        self.assertEqual(str(cm.exception), 'Invalid number, must be a positive integer.')
        with self.assertRaises(Exception) as cm:
            is_prime(-1)
        self.assertEqual(str(cm.exception), 'Invalid number, must be a positive integer.')
        with self.assertRaises(Exception) as cm:
            is_prime(2.3)
        self.assertEqual(str(cm.exception), 'Invalid number, must be a positive integer.')
    def test_generate_primes(self):
        self.assertEqual(generate_primes(10), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
        with self.assertRaises(Exception) as cm:
            generate_primes(-1)
        self.assertEqual(str(cm.exception), 'Invalid number, must be a positive integer.')
        with self.assertRaises(Exception) as cm:
            generate_primes('ten')
        self.assertEqual(str(cm.exception), 'Invalid number, must be a positive integer.')
        with self.assertRaises(Exception) as cm:
            generate_primes(0)
        self.assertEqual(str(cm.exception), 'Invalid number, must be a positive integer.')
    def test_generate_10000_primes(self):
        large_prime_list = generate_primes(10000)
        self.assertEqual(large_prime_list[999], 7919)
        self.assertEqual(large_prime_list[9999], 104729)
    def test_generate_multiplication_table(self):
        prime_example = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        prime_results = generate_multiplication_table(prime_example).get_string()
        self.assertIn('3    | 6  | 9  |  15 |  21 |  33 |  39 |  51 |  57 ', prime_results)
        self.assertIn('29   | 58 | 87 | 145 | 203 | 319 | 377 | 493 | 551 ', prime_results)
    def test_generate_multiplication_table_exception(self):
        prime_example = ['2', 3, 5, 'bad data', 11.0, 13, 17, 19, 23, 29]
        with self.assertRaises(Exception) as cm:
            generate_multiplication_table(prime_example)
        self.assertEqual(str(cm.exception), 'Invalid list, should only contain integers.')
    def test_generate_multiplication_table_negatives(self):
        prime_example = [2, -3, 5, 7, 11, -13, 17, 19, 23, 29]
        prime_results = generate_multiplication_table(prime_example).get_string()
        self.assertIn('-3   |  -6 |  9  | -15 | -21 | -33  |  39  | -51  ', prime_results)
        self.assertIn('29   |  58 | -87 | 145 | 203 | 319  | -377 | 493  ', prime_results)
if __name__ == "__main__":
    unittest.main()