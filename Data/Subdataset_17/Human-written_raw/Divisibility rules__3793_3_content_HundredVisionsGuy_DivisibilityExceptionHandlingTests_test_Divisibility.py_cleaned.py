import unittest
import Divisibility
import re
class KnownValues(unittest.TestCase):
    def setUp(self):
        self.textfile = open('Divisibility.py', 'r')
        self.scripttext = self.textfile.read()
    def tearDown(self):
        self.textfile.close()
    def test_divisibility_forZeroDivisionErrorHandling(self):
        self.assertEquals('error', Divisibility.divisibility(10,0))
    def test_divisibility_forValueErrorHandling(self):
        self.assertEquals('error', Divisibility.divisibility(10, 'five'))
    def test_divisibility_forEvenlyDivisible(self):
        result = Divisibility.divisibility(21, 3)
        self.assertEquals('divides evenly', result)
    def test_divisibility_forEvenlyDivisible_10_2(self):
        result = Divisibility.divisibility(10, 2)
        self.assertEquals('divides evenly', result)
    def test_divisibility_forNotEvenlyDivisible(self):
        result = Divisibility.divisibility(5,2)
        self.assertEquals("doesn't divide evenly", result)
    def test_divisibility_forNotEvenlyDivisible_7_2(self):
        result = Divisibility.divisibility(7,2)
        self.assertEquals("doesn't divide evenly", result)
    def test_try_cmd_present(self):
        matches = re.findall("try:", self.scripttext)
        match = matches[0]
        self.assertEquals("try:", match)
    def test_except_block_present(self):
        matches = re.findall("except ValueError:", self.scripttext)
        matches += re.findall("except:", self.scripttext)
        matches += re.findall("except ZeroDivisionError:", self.scripttext)
        hasMatch = bool(matches)
        self.assertEquals(True, hasMatch)
if __name__ == '__main__':
    unittest.main()