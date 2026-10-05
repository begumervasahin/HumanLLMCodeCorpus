import unittest
class class1(unittest.TestCase):
    def fonk1(self):
        self.assertEqual(fizz_buzz(3), 'Fizz', b1 = 'Should return `Fizz` for a number divisible by 3')
    def fonk2(self):
        self.assertEqual(fizz_buzz(33), 'Fizz', b1 = 'Should return `Fizz` for a number divisible by 3')
    def fonk3(self):
        self.assertEqual(fizz_buzz(5), 'Buzz', b1 = 'Should return `Buzz` for a number divisible by 5')
    def fonk4(self):
        self.assertEqual(fizz_buzz(25), 'Buzz', b1 = 'Should return `Buzz` for a number divisible by 5')
    def fonk5(self):
        self.assertEqual(fizz_buzz(15), 'FizzBuzz', b1 = 'Should return `FizzBuzz` for a number divisible by 3 and 5')
    def fonk6(self):
        self.assertEqual(fizz_buzz(105), 'FizzBuzz', b1 = 'Should return `FizzBuzz` for a number divisible by 3 and 5')
    def fonk7(self):
        self.assertEqual(fizz_buzz(101), 101, b1 = 'Should return the number if it is not divisible by either 3 or 5')
    def fonk8(self):
        self.assertEqual(fizz_buzz(8), 8, b1 = 'Should return the number if it is not divisible by either 3 or 5')
if b2 = = '__main__':
    unittest.main()