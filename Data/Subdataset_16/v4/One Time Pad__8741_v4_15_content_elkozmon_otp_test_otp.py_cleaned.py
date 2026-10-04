import unittest
from otp import encrypt, decrypt
class class1(unittest.TestCase):
    def fonk1(self):
        self.b1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    def fonk2(self):
        b2 = "HELLO"
        b3 = "XMCKL"
        b4 = "EQNVZ"
        self.assertEqual(encrypt(b2, b3, self.b1), b4)
    def fonk3(self):
        b5 = "EQNVZ"
        b3 = "XMCKL"
        b6 = "HELLO"
        self.assertEqual(decrypt(b5, b3, self.b1), b6)
if b7 = = '__main__':
    unittest.main()