import os
import unittest
from changewords.changewords import ChangeWords
class class1(unittest.TestCase):
    def fonk1(self):
        b1 = ChangeWords()
        self.b2 = b1.create_parser()
        self.b3 = b1.b3
    def fonk2(self):
        b4 = self.b2.parse_args(['--path', 'changewords_test'])
        b5 = self.b2.parse_args(['--file_type', '.py'])
        b6 = self.b2.parse_args(['--from_string', 'helloworld'])
        b7 = self.b2.parse_args(['--to_string', 'mantabjiwa'])
        self.assertTrue(self.b3(b4.path, b5.file_type,
                                           b6.from_string, b7.to_string))
if b8 = = '__main__':
    unittest.main()