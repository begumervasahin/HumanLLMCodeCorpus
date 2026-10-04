import unittest
from prime_number_multiplication_table import *
class PrimeNumberUnitTests(unittest.TestCase):
    print "running unit tests for prime number functions"
    def test_is_prime(self):
        assert is_prime(1) is False
        assert is_prime(2) is True
        assert is_prime(4) is False
        assert is_prime(5) is True
        assert is_prime(104729) is True
        assert is_prime(104728) is False
    def test_is_prime_exception_handling(self):
        with self.assertRaises(Exception) as cm:
            is_prime(0)
        assert cm.exception.message == 'Invalid number, must be a positive integer.'
        with self.assertRaises(Exception) as cm:
            is_prime(-1)
        assert cm.exception.message == 'Invalid number, must be a positive integer.'
        with self.assertRaises(Exception) as cm:
            is_prime(2.3)
        assert cm.exception.message == 'Invalid number, must be a positive integer.'
    def test_generate_primes(self):
        assert generate_primes(10) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        with self.assertRaises(Exception) as cm:
            generate_primes(-1)
        assert cm.exception.message == 'Invalid number, must be a positive integer.'
        with self.assertRaises(Exception) as cm:
            generate_primes('ten')
        assert cm.exception.message == 'Invalid number, must be a positive integer.'
        with self.assertRaises(Exception) as cm:
            generate_primes(0)
        assert cm.exception.message == 'Invalid number, must be a positive integer.'
    def test_generate_10000_primes(self):
        large_prime_list = generate_primes(10000)
        assert large_prime_list[999] == 7919
        assert large_prime_list[9999] == 104729
    def test_generate_multiplication_table(self):
        prime_example = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        prime_results = generate_multiplication_table(prime_example).get_string()
        result_contains_1 = '3    | 6  | 9  |  15 |  21 |  33 |  39 |  51 |  57 '
        result_contains_2 = '29   | 58 | 87 | 145 | 203 | 319 | 377 | 493 | 551 '
        self.assertIn(result_contains_1, prime_results)
        self.assertIn(result_contains_2, prime_results)
    def test_generate_multiplication_table_exception(self):
        prime_example = ['2', 3, 5, 'bad data', 11.0, 13, 17, 19, 23, 29]
        with self.assertRaises(Exception) as cm:
            generate_multiplication_table(prime_example)
        assert cm.exception.message == 'Invalid list, should only contain integers.'
    def test_generate_multiplication_table_negatives(self):
        prime_example = [2, -3, 5, 7, 11, -13, 17, 19, 23, 29]
        prime_results = generate_multiplication_table(prime_example).get_string()
        result_contains_1 = '-3   |  -6 |  9  | -15 | -21 | -33  |  39  | -51  '
        result_contains_2 = '29   |  58 | -87 | 145 | 203 | 319  | -377 | 493  '
        self.assertIn(result_contains_1, prime_results)
        self.assertIn(result_contains_2, prime_results)
if __name__ == "__main__":
    unittest.main()