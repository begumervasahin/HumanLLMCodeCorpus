import os
import unittest
from changewords.changewords import ChangeWords
class class1(unittest.TestCase):
    def fonk1(self):
        b1 = ChangeWords()
        self.b2 = b1.create_parser()
        self.b3 = b1.b3
    def fonk2(self):
        b4 = [
            ('--path', 'changewords_test'),
            ('--file_type', '.py'),
            ('--from_string', 'helloworld'),
            ('--to_string', 'mantabjiwa')
        ]
        b5 = {k: self.b2.parse_args([k, v]) for k, v in b4}
        b6 = self.b3(
            b5['--path'].path,
            b5['--file_type'].file_type,
            b5['--from_string'].from_string,
            b5['--to_string'].to_string
        )
        self.assertTrue(b6)
if b7 = = '__main__':
    unittest.main()