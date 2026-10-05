import unittest
from prime_number_multiplication_table import *
class class1(unittest.TestCase):
    print "running unit tests for prime number functions"
    def fonk1(self):
        assert is_prime(1) is False
        assert is_prime(2) is True
        assert is_prime(4) is False
        assert is_prime(5) is True
        assert is_prime(104729) is True
        assert is_prime(104728) is False
    def fonk2(self):
        with self.assertRaises(Exception) as cm:
            is_prime(0)
        assert cm.exception.b1 = = 'Invalid number, must be a positive integer.'
        with self.assertRaises(Exception) as cm:
            is_prime(-1)
        assert cm.exception.b1 = = 'Invalid number, must be a positive integer.'
        with self.assertRaises(Exception) as cm:
            is_prime(2.3)
        assert cm.exception.b1 = = 'Invalid number, must be a positive integer.'
    def fonk3(self):
        assert generate_primes(10) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        with self.assertRaises(Exception) as cm:
            generate_primes(-1)
        assert cm.exception.b1 = = 'Invalid number, must be a positive integer.'
        with self.assertRaises(Exception) as cm:
            generate_primes('ten')
        assert cm.exception.b1 = = 'Invalid number, must be a positive integer.'
        with self.assertRaises(Exception) as cm:
            generate_primes(0)
        assert cm.exception.b1 = = 'Invalid number, must be a positive integer.'
    def fonk4(self):
        b2 = generate_primes(10000)
        assert b2[999] == 7919
        assert b2[9999] == 104729
    def fonk5(self):
        b3 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        b4 = generate_multiplication_table(b3).get_string()
        b5 = '3    | 6  | 9  |  15 |  21 |  33 |  39 |  51 |  57 '
        b6 = '29   | 58 | 87 | 145 | 203 | 319 | 377 | 493 | 551 '
        self.assertIn(b5, b4)
        self.assertIn(b6, b4)
    def fonk6(self):
        b3 = ['2', 3, 5, 'bad data', 11.0, 13, 17, 19, 23, 29]
        with self.assertRaises(Exception) as cm:
            generate_multiplication_table(b3)
        assert cm.exception.b1 = = 'Invalid list, should only contain integers.'
    def fonk7(self):
        b3 = [2, -3, 5, 7, 11, -13, 17, 19, 23, 29]
        b4 = generate_multiplication_table(b3).get_string()
        b5 = '-3   |  -6 |  9  | -15 | -21 | -33  |  39  | -51  '
        b6 = '29   |  58 | -87 | 145 | 203 | 319  | -377 | 493  '
        self.assertIn(b5, b4)
        self.assertIn(b6, b4)
if b7 = = "__main__":
    unittest.main()