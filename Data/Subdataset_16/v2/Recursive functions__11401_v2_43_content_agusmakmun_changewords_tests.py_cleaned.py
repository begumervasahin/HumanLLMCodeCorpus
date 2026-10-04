import argparse
import os
class class1:
    def fonk1(self):
        b1 = argparse.ArgumentParser(description='Change words in files.')
        b1.add_argument('--path', b2 = True, help='Path to directory or file.')
        b1.add_argument('--file_type', b2 = True, help='Type of files to search.')
        b1.add_argument('--b12', b2 = True, help='String to search for.')
        b1.add_argument('--b13', b2 = True, help='String to replace with.')
        return b1
    def fonk2(self, path, file_type, b12, b13):
        if os.path.isfile(path) and path.endswith(file_type):
            self.fonk3(path, b12, b13)
            return True
        elif os.path.isdir(path):
            for root, _, files in os.walk(path):
                for file in files:
                    if file.endswith(file_type):
                        b3 = os.path.join(root, file)
                        self.fonk3(b3, b12, b13)
            return True
        return False
    def fonk3(self, b3, b12, b13):
        with open(b3, 'r') as file:
            b4 = file.read()
        b5 = b4.replace(b12, b13)
        with open(b3, 'w') as file:
            file.write(b5)
if b6 = = "__main__":
    b7 = class1()
    b1 = b7.fonk1()
    b8 = b1.parse_args()
    b7.fonk2(b8.path, b8.file_type, b8.b12, b8.b13)
import os
import unittest
from changewords.changewords import class1
class class2(unittest.TestCase):
    def fonk4(self):
        self.b9 = class1()
        self.b1 = self.b9.fonk1()
        self.b10 = 'changewords_test'
        self.b11 = 'b11.py'
        self.b12 = 'helloworld'
        self.b13 = 'mantabjiwa'
        if not os.path.exists(self.b10):
            os.makedirs(self.b10)
        with open(os.path.join(self.b10, self.b11), 'w') as f:
            f.write(f"This is a test file with the word {self.b12} in it.")
    def fonk5(self):
        if os.path.exists(self.b10):
            for root, _, files in os.walk(self.b10):
                for file in files:
                    os.remove(os.path.join(root, file))
            os.rmdir(self.b10)
    def fonk6(self):
        b8 = self.b1.parse_args([
            '--path', self.b10,
            '--file_type', '.py',
            '--b12', self.b12,
            '--b13', self.b13
        ])
        self.assertTrue(self.b9.fonk2(
            b8.path, b8.file_type, b8.b12, b8.b13))
        with open(os.path.join(self.b10, self.b11), 'r') as f:
            b4 = f.read()
            self.assertIn(self.b13, b4)
            self.assertNotIn(self.b12, b4)
if b6 = = '__main__':
    unittest.main()