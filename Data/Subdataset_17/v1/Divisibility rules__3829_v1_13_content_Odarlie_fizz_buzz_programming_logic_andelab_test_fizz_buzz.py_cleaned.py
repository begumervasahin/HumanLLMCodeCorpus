import unittest
def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return 'FizzBuzz'
    if number % 3 == 0:
        return 'Fizz'
    if number % 5 == 0:
        return 'Buzz'
    return number
class FizzBuzzClassTest(unittest.TestCase):
    def test_fizz_1(self):
        self.assertEqual(fizz_buzz(3), 'Fizz', msg='should return `Fizz` for number divisible by 3')
    def test_fizz_2(self):
        self.assertEqual(fizz_buzz(33), 'Fizz', msg='should return `Fizz` for number divisible by 3')
    def test_buzz_1(self):
        self.assertEqual(fizz_buzz(5), 'Buzz', msg='should return `Buzz` for number divisible by 5')
    def test_buzz_2(self):
        self.assertEqual(fizz_buzz(25), 'Buzz', msg='should return `Buzz` for number divisible by 5')
    def test_fizz_buzz_1(self):
        self.assertEqual(fizz_buzz(15), 'FizzBuzz', msg='should return `FizzBuzz` for number divisible by 3 and 5')
    def test_fizz_buzz_2(self):
        self.assertEqual(fizz_buzz(105), 'FizzBuzz', msg='should return `FizzBuzz` for number divisible by 3 and 5')
    def test_indivisible_1(self):
        self.assertEqual(fizz_buzz(101), 101, msg='should return the number if it is indivisible by neither 3 nor 5')
    def test_indivisible_2(self):
        self.assertEqual(fizz_buzz(8), 8, msg='should return the number if it is indivisible by neither 3 nor 5')
if __name__ == '__main__':
    unittest.main()