import os
import unittest
from changewords.changewords import ChangeWords
class class1(unittest.TestCase):
    def fonk1(self):
        self.b1 = ChangeWords()
        self.b2 = self.b1.create_parser()
        self.b3 = self.b1.b3
    def fonk2(self):
        b4 = self.b2.parse_args(['--b5', 'changewords_test',
                                              '--b6', '.py',
                                              '--b7', 'helloworld',
                                              '--b8', 'mantabjiwa'])
        b5 = b4.b5
        b6 = b4.b6
        b7 = b4.b7
        b8 = b4.b8
        self.assertTrue(self.b3(b5, b6, b7, b8))
if b9 = = '__main__':
    unittest.main()