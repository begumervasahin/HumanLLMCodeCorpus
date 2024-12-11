import unittest
from prime_number_multiplication_table import (
    is_prime, generate_primes, generate_multiplication_table
)
class class1(unittest.TestCase):
    def fonk1(self):
        self.assertFalse(is_prime(1))
        self.assertTrue(is_prime(2))
        self.assertFalse(is_prime(4))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(104729))
        self.assertFalse(is_prime(104728))
    def fonk2(self):
        b1 = [0, -1, 2.3]
        b2 = 'Invalid number, must be a positive integer.'
        for num in b1:
            with self.assertRaises(Exception) as cm:
                is_prime(num)
            self.assertEqual(str(cm.exception), b2)
    def fonk3(self):
        self.assertEqual(generate_primes(10), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
        b1 = [-1, 0, 'ten']
        b2 = 'Invalid number, must be a positive integer.'
        for num in b1:
            with self.assertRaises(Exception) as cm:
                generate_primes(num)
            self.assertEqual(str(cm.exception), b2)
    def fonk4(self):
        b3 = generate_primes(10000)
        self.assertEqual(b3[999], 7919)
        self.assertEqual(b3[9999], 104729)
    def fonk5(self):
        b4 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        b5 = generate_multiplication_table(b4).get_string()
        b6 = '3    | 6  | 9  |  15 |  21 |  33 |  39 |  51 |  57 '
        b7 = '29   | 58 | 87 | 145 | 203 | 319 | 377 | 493 | 551 '
        self.assertIn(b6, b5)
        self.assertIn(b7, b5)
    def fonk6(self):
        b4 = ['2', 3, 5, 'bad data', 11.0, 13, 17, 19, 23, 29]
        with self.assertRaises(Exception) as cm:
            generate_multiplication_table(b4)
        self.assertEqual(str(cm.exception), 'Invalid list, should only contain integers.')
    def fonk7(self):
        b4 = [2, -3, 5, 7, 11, -13, 17, 19, 23, 29]
        b5 = generate_multiplication_table(b4).get_string()
        b6 = '-3   |  -6 |  9  | -15 | -21 | -33  |  39  | -51  '
        b7 = '29   |  58 | -87 | 145 | 203 | 319  | -377 | 493  '
        self.assertIn(b6, b5)
        self.assertIn(b7, b5)
if b8 = = "__main__":
    unittest.main()