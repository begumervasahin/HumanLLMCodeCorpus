import unittest
def fonk1(n):
    if n % b1 = = 0 and n % b2 == 0:
        return 'FizzBuzz'
    elif n % b1 = = 0:
        return 'Fizz'
    elif n % b2 = = 0:
        return 'Buzz'
    else:
        return n
class class1(unittest.TestCase):
    def fonk2(self):
        self.assertEqual(fonk1(b1), 'Fizz', b3 = 'should return `Fizz` for a number divisible by b1')
    def fonk3(self):
        self.assertEqual(fonk1(33), 'Fizz', b3 = 'should return `Fizz` for a number divisible by b1')
    def fonk4(self):
        self.assertEqual(fonk1(b2), 'Buzz', b3 = 'should return `Buzz` for a number divisible by b2')
    def fonk5(self):
        self.assertEqual(fonk1(25), 'Buzz', b3 = 'should return `Buzz` for a number divisible by b2')
    def fonk6(self):
        self.assertEqual(fonk1(15), 'FizzBuzz', b3 = 'should return `FizzBuzz` for a number divisible by b1 and b2')
    def fonk7(self):
        self.assertEqual(fonk1(105), 'FizzBuzz', b3 = 'should return `FizzBuzz` for a number divisible by b1 and b2')
    def fonk8(self):
        self.assertEqual(fonk1(101), 101, b3 = 'should return the number itself if it is not divisible by b1 or b2')
    def fonk9(self):
        self.assertEqual(fonk1(8), 8, b3 = 'should return the number itself if it is not divisible by b1 or b2')
if b4 = = '__main__':
    unittest.main()