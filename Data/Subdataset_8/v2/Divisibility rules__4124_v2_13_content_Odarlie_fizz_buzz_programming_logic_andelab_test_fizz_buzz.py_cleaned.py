import unittest
def fizz_buzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return 'FizzBuzz'
    elif n % 3 == 0:
        return 'Fizz'
    elif n % 5 == 0:
        return 'Buzz'
    else:
        return n
class FizzBuzzClassTest(unittest.TestCase):
    def test_fizz_divisible_by_3(self):
        self.assertEqual(fizz_buzz(3), 'Fizz', msg='should return `Fizz` for a number divisible by 3')
    def test_fizz_33(self):
        self.assertEqual(fizz_buzz(33), 'Fizz', msg='should return `Fizz` for a number divisible by 3')
    def test_buzz_divisible_by_5(self):
        self.assertEqual(fizz_buzz(5), 'Buzz', msg='should return `Buzz` for a number divisible by 5')
    def test_buzz_25(self):
        self.assertEqual(fizz_buzz(25), 'Buzz', msg='should return `Buzz` for a number divisible by 5')
    def test_fizzbuzz_divisible_by_3_and_5(self):
        self.assertEqual(fizz_buzz(15), 'FizzBuzz', msg='should return `FizzBuzz` for a number divisible by 3 and 5')
    def test_fizzbuzz_105(self):
        self.assertEqual(fizz_buzz(105), 'FizzBuzz', msg='should return `FizzBuzz` for a number divisible by 3 and 5')
    def test_indivisible_by_3_or_5(self):
        self.assertEqual(fizz_buzz(101), 101, msg='should return the number itself if it is not divisible by 3 or 5')
    def test_indivisible_by_3_or_5_8(self):
        self.assertEqual(fizz_buzz(8), 8, msg='should return the number itself if it is not divisible by 3 or 5')
if __name__ == '__main__':
    unittest.main()