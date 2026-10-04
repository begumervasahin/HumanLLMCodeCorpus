import unittest
import re
import Divisibility
class KnownValues(unittest.TestCase):
    def setUp(self):
        with open('Divisibility.py', 'r') as file:
            self.scripttext = file.read()
    def test_divisibility_handles_zero_division_error(self):
        self.assertEqual('error', Divisibility.divisibility(10, 0))
    def test_divisibility_handles_value_error(self):
        self.assertEqual('error', Divisibility.divisibility(10, 'five'))
    def test_divisibility_divides_evenly(self):
        result = Divisibility.divisibility(21, 3)
        self.assertEqual('divides evenly', result)
    def test_divisibility_divides_evenly_10_2(self):
        result = Divisibility.divisibility(10, 2)
        self.assertEqual('divides evenly', result)
    def test_divisibility_does_not_divide_evenly(self):
        result = Divisibility.divisibility(5, 2)
        self.assertEqual("doesn't divide evenly", result)
    def test_divisibility_does_not_divide_evenly_7_2(self):
        result = Divisibility.divisibility(7, 2)
        self.assertEqual("doesn't divide evenly", result)
    def test_try_command_present(self):
        matches = re.findall(r"try:", self.scripttext)
        self.assertTrue(matches)
    def test_except_block_present(self):
        matches = re.findall(r"except ValueError:", self.scripttext)
        matches += re.findall(r"except:", self.scripttext)
        matches += re.findall(r"except ZeroDivisionError:", self.scripttext)
        self.assertTrue(matches)
if __name__ == '__main__':
    unittest.main()