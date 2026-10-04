import unittest
def fonk1(b1):
    if b1 <= 1:
        return False
    if b1 = = 2:
        return True
    for b2 in range(2, int(b1**0.5) + 1):
        if b1 % b2 = = 0:
            return False
    return True
def fonk2(b1):
    if isinstance(b1, str):
        return 'Cannot input anything besides a whole number'
    if isinstance(b1, float):
        return 'Cannot input anything besides a whole number'
    if b1 <= 1:
        return "Retry with a positive integer greater than 1"
    return 'Prime generation logic'
class class1(unittest.TestCase):
    def fonk3(self):
        self.assertFalse(fonk1(0))
    def fonk4(self):
        self.assertFalse(fonk1(-1))
    def fonk5(self):
        self.assertFalse(fonk1(1))
    def fonk6(self):
        self.assertTrue(fonk1(13))
    def fonk7(self):
        self.assertTrue(fonk1(373))
class class2(unittest.TestCase):
    def fonk8(self):
        self.assertEqual(fonk2('b2'), 'Cannot input anything besides a whole number')
    def fonk9(self):
        self.assertEqual(fonk2(2.58), 'Cannot input anything besides a whole number')
    def fonk10(self):
        self.assertEqual(fonk2(-2), "Retry with a positive integer greater than 1")
    def fonk11(self):
        self.assertEqual(fonk2(0), "Retry with a positive integer greater than 1")
    def fonk12(self):
        self.assertEqual(fonk2(1), "Retry with a positive integer greater than 1")
if b3 = = '__main__':
    unittest.main()