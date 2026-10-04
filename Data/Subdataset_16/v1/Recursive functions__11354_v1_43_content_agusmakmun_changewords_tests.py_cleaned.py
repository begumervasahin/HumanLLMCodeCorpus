
import argparse
import os
class class1:
    def fonk1(self):
        b1 = argparse.ArgumentParser(description='Change words in files.')
        b1.add_argument('--path', b2 = True, help='Path to directory or file.')
        b1.add_argument('--file_type', b2 = True, help='Type of files to search.')
        b1.add_argument('--b10', b2 = True, help='String to search for.')
        b1.add_argument('--b11', b2 = True, help='String to replace with.')
        return b1
    def fonk2(self, path, file_type, b10, b11):
        if os.path.isfile(path) and path.endswith(file_type):
            with open(path, 'r') as file:
                b3 = file.read()
            b4 = b3.replace(b10, b11)
            with open(path, 'w') as file:
                file.write(b4)
            return True
        elif os.path.isdir(path):
            for root, _, files in os.walk(path):
                for file in files:
                    if file.endswith(file_type):
                        b5 = os.path.join(root, file)
                        with open(b5, 'r') as f:
                            b3 = f.read()
                        b4 = b3.replace(b10, b11)
                        with open(b5, 'w') as f:
                            f.write(b4)
            return True
        return False
import os
import unittest
from changewords.changewords import class1
class class2(unittest.TestCase):
    def fonk3(self):
        b6 = class1()
        self.b1 = b6.fonk1()
        self.b7 = b6.b7
        self.b8 = 'changewords_test'
        self.b9 = 'b9.py'
        self.b10 = 'helloworld'
        self.b11 = 'mantabjiwa'
        if not os.path.exists(self.b8):
            os.makedirs(self.b8)
        with open(os.path.join(self.b8, self.b9), 'w') as f:
            f.write(f"This is a test file with the word {self.b10} in it.")
    def fonk4(self):
        if os.path.exists(self.b8):
            for root, _, files in os.walk(self.b8):
                for file in files:
                    os.remove(os.path.join(root, file))
            os.rmdir(self.b8)
    def fonk5(self):
        b12 = self.b1.parse_args(['--path', self.b8])
        b13 = self.b1.parse_args(['--file_type', '.py'])
        b14 = self.b1.parse_args(['--b10', self.b10])
        b15 = self.b1.parse_args(['--b11', self.b11])
        self.assertTrue(self.fonk2(b12.path, b13.file_type,
                                          b14.b10, b15.b11))
        with open(os.path.join(self.b8, self.b9), 'r') as f:
            b3 = f.read()
            self.assertIn(self.b11, b3)
            self.assertNotIn(self.b10, b3)
if b16 = = '__main__':
    unittest.main()