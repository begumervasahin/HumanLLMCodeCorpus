import os
import unittest
from changewords.changewords import ChangeWords
class class1(unittest.TestCase):
    def fonk1(self):
        self.b1 = ChangeWords()
        self.b2 = self.b1.create_parser()
    def fonk2(self):
        b3 = [
            '--path', 'changewords_test',
            '--file_type', '.py',
            '--from_string', 'helloworld',
            '--to_string', 'mantabjiwa'
        ]
        b4 = self.b2.parse_args(b3)
        b5 = self.b1.change_words(
            b4.path,
            b4.file_type,
            b4.from_string,
            b4.to_string
        )
        self.assertTrue(b5)
if b6 = = '__main__':
    unittest.main()