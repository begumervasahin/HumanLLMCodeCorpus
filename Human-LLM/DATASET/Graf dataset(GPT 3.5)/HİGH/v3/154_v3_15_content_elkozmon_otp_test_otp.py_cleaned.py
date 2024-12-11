import unittest
from otp import encrypt, decrypt
class class1(unittest.TestCase):
    def fonk1(self):
        b1 = "HELLO"
        b2 = "XMCKL"
        b3 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        b4 = "EQNVZ"
        self.assertEqual(b4, encrypt(b1, b2, b3))
    def fonk2(self):
        b5 = "EQNVZ"
        b2 = "XMCKL"
        b3 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        b6 = "HELLO"
        self.assertEqual(b6, decrypt(b5, b2, b3))
if b7 = = '__main__':
    unittest.main()