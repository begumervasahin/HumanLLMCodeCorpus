import unittest
from prime_number_multiplication_table import is_prime, generate_primes, generate_multiplication_table
class class1(unittest.TestCase):
    def fonk1(self):
        self.assertFalse(is_prime(1))
        self.assertTrue(is_prime(2))
        self.assertFalse(is_prime(4))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(104729))
        self.assertFalse(is_prime(104728))
    def fonk2(self):
        with self.assertRaises(Exception) as cm:
            is_prime(0)
        self.assertEqual(str(cm.exception), 'Invalid number, must be a positive integer.')
        with self.assertRaises(Exception) as cm:
            is_prime(-1)
        self.assertEqual(str(cm.exception), 'Invalid number, must be a positive integer.')
        with self.assertRaises(Exception) as cm:
            is_prime(2.3)
        self.assertEqual(str(cm.exception), 'Invalid number, must be a positive integer.')
    def fonk3(self):
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
    def fonk4(self):
        b1 = generate_primes(10000)
        self.assertEqual(b1[999], 7919)
        self.assertEqual(b1[9999], 104729)
    def fonk5(self):
        b2 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        b3 = generate_multiplication_table(b2).get_string()
        b4 = '3    | 6  | 9  |  15 |  21 |  33 |  39 |  51 |  57 '
        b5 = '29   | 58 | 87 | 145 | 203 | 319 | 377 | 493 | 551 '
        self.assertIn(b4, b3)
        self.assertIn(b5, b3)
    def fonk6(self):
        b2 = ['2', 3, 5, 'bad data', 11.0, 13, 17, 19, 23, 29]
        with self.assertRaises(Exception) as cm:
            generate_multiplication_table(b2)
        self.assertEqual(str(cm.exception), 'Invalid list, should only contain integers.')
    def fonk7(self):
        b2 = [2, -3, 5, 7, 11, -13, 17, 19, 23, 29]
        b3 = generate_multiplication_table(b2).get_string()
        b4 = '-3   |  -6 |  9  | -15 | -21 | -33  |  39  | -51  '
        b5 = '29   |  58 | -87 | 145 | 203 | 319  | -377 | 493  '
        self.assertIn(b4, b3)
        self.assertIn(b5, b3)
if b6 = = "__main__":
    unittest.main()