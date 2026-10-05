import unittest
import Divisibility
import re
class class1(unittest.TestCase):
    def fonk1(self):
        self.b1 = open('Divisibility.py', 'r')
        self.b2 = self.b1.read()
    def fonk2(self):
        self.b1.close()
    def fonk3(self):
        self.assertEqual('error', Divisibility.divisibility(10, 0))
    def fonk4(self):
        self.assertEqual('error', Divisibility.divisibility(10, 'five'))
    def fonk5(self):
        b3 = Divisibility.divisibility(21, 3)
        self.assertEqual('divides evenly', b3)
    def fonk6(self):
        b3 = Divisibility.divisibility(10, 2)
        self.assertEqual('divides evenly', b3)
    def fonk7(self):
        b3 = Divisibility.divisibility(5, 2)
        self.assertEqual("doesn't divide evenly", b3)
    def fonk8(self):
        b3 = Divisibility.divisibility(7, 2)
        self.assertEqual("doesn't divide evenly", b3)
    def fonk9(self):
        b4 = re.findall("try:", self.b2)
        b5 = b4[0]
        self.assertEqual("try:", b5)
    def fonk10(self):
        b4 = re.findall("except ValueError:", self.b2)
        b4 += re.findall("except:", self.b2)
        b4 += re.findall("except ZeroDivisionError:", self.b2)
        b6 = bool(b4)
        self.assertTrue(b6)
if b7 = = '__main__':
    unittest.main()