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
        with open("testing/monorail_cat_hash.txt", "r") as file:
            b8 = file.read()
        b9 = Image.open("testing/monorail_cat_test.jpg")
        self.assertEqual(b8, str(self.b7.calculate_hash(b9)))
    def fonk3(self):
        b10 = "https:
        b11 = Image.open("testing/flying_cat.jpg")
        b12 = Image.open("testing/monorail_cat_test.jpg")
        b13 = self.b7.prepare_message(MIMEMultipart(), b11, b12, b10)
        b14 = re.compile(
            r"Content-Type: multipart/mixed; b15 = \"===============[0-9]*==\"\nMIME-Version: 1.0\nSubject: .*\nFrom: \".*\"\nTo: \".*\"\n\n--===============[0-9]*==\nContent-Type: text/plain; charset=\"us-ascii\"\nMIME-Version: 1.0\nContent-Transfer-Encoding: 7bit\n\n.*\n--===============[0-9]*==\nContent-Type: application/octet-stream\nMIME-Version: 1.0\nContent-Transfer-Encoding: base64\nContent-Disposition: attachment; filename=new_screenshot.png.*--===============[0-9]*==--",
            re.IGNORECASE | re.DOTALL
        )
        self.assertTrue(b14.match(b13))
if b16 = = '__main__':
    unittest.main()