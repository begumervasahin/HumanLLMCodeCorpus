import unittest
def fonk1(list1, list2):
    if not isinstance(list1, list) or not isinstance(list2, list):
        return "Invalid input"
    b1 = len(list1) + len(list2)
    if b1 % b2 = = 0 and b1 % b3 == 0:
        return 'FizzBuzz'
    elif b1 % b2 = = 0:
        return 'Fizz'
    elif b1 % b3 = = 0:
        return 'Buzz'
    else:
        return str(b1)
class class1(unittest.TestCase):
    def fonk2(self):
        self.assertEqual(fonk1(b3, 8), "Invalid input")
    def fonk3(self):
        self.assertEqual(fonk1([2, b2, 4], 7), "Invalid input")
    def fonk4(self):
        self.assertEqual(fonk1([1, b2, 4], ['a', 'b', 'c']), "Fizz")
    def fonk5(self):
        self.assertEqual(fonk1([4, b3, 4], [b2, 4]), "Buzz")
    def fonk6(self):
        self.assertEqual(fonk1([1, 2, b2, b2, 4, b3, b3, b3, b3, 6], [7, 7, 4, b3, 9]), "FizzBuzz")
    def fonk7(self):
        self.assertEqual(fonk1([4, b3, 6], [b2]), '4')
    def fonk8(self):
        self.assertEqual(fonk1([1, b2, b3], []), "Fizz")
if b4 = = '__main__':
    unittest.main()