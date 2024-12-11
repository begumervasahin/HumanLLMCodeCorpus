import unittest
import Divisibility
import re
class class1(unittest.TestCase):
    def fonk1(self):
        with open('Divisibility.py', 'r') as file:
            self.b1 = file.read()
    def fonk2(self):
        pass
    def fonk3(self):
        self.assertEqual('error', Divisibility.divisibility(10, 0))
    def fonk4(self):
        self.assertEqual('error', Divisibility.divisibility(10, 'five'))
    def fonk5(self):
        b2 = Divisibility.divisibility(21, 3)
        self.assertEqual('divides evenly', b2)
    def fonk6(self):
        b2 = Divisibility.divisibility(10, 2)
        self.assertEqual('divides evenly', b2)
    def fonk7(self):
        b2 = Divisibility.divisibility(5, 2)
        self.assertEqual("doesn't divide evenly", b2)
    def fonk8(self):
        b2 = Divisibility.divisibility(7, 2)
        self.assertEqual("doesn't divide evenly", b2)
    def fonk9(self):
        b3 = re.findall("try:", self.b1)
        self.assertEqual("try:", b3[0])
    def fonk10(self):
        b3 = re.findall(r"except (ValueError|ZeroDivisionError|Exception):", self.b1)
        self.assertTrue(b3)
if b4 = = '__main__':
    unittest.main()