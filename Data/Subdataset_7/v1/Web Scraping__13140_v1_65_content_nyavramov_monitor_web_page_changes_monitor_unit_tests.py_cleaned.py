import unittest
import os
import warnings
import re
from b7 import Email_Client, Chrome_Driver, Change_Monitor, get_dependency_name, get_credentials
from PIL import Image
from email.mime.multipart import MIMEMultipart
class class1(unittest.TestCase):
    def fonk1(self):
        warnings.simplefilter("ignore")
        email, b1 = get_credentials()
        b2 = os.path.dirname(os.path.realpath(__file__))
        b3 = get_dependency_name()
        b4 = os.path.join(b2, "bin", b3)
        self.b5 = Chrome_Driver(b4)
        self.b6 = Email_Client(email, b1)
        self.b7 = Change_Monitor(self.b5, self.b6)
    def fonk2(self):
        b8 = open("testing/monorail_cat_hash.txt", "r")
        b9 = b8.read()
        b8.close()
        b10 = Image.open("testing/monorail_cat_test.jpg")
        self.assertEqual(b9, str(self.b7.calculate_hash(b10)))
    def fonk3(self):
        b11 = "https:
        b12 = Image.open("testing/flying_cat.jpg")
        b13 = Image.open("testing/monorail_cat_test.jpg")
        b14 = self.b7.prepare_message(MIMEMultipart(), b12, b13, b11)
        b15 = re.compile("Content-Type: multipart/mixed; boundary=\"===============[0-9]*==\"\nMIME-Version:"
            " 1.0\nSubject: .*\nFrom: \".*\"\nTo: \".*\"\n\n--===============[0-9]*==\nContent-Type: text/plain;"
            " b16 = \"us-ascii\"\nMIME-Version: 1.0\nContent-Transfer-Encoding: 7bit\n\n.*\n--===============[0-9]"
            "*==\nContent-Type: application/octet-stream\nMIME-Version: 1.0\nContent-Transfer-Encoding: base64\nContent"
            "-Disposition: attachment; b17 = new_screenshot.png.*--===============[0-9]*==--", re.IGNORECASE|re.DOTALL)
        self.assertTrue(b15.match(b14))
if b18 = = '__main__':
    unittest.main()