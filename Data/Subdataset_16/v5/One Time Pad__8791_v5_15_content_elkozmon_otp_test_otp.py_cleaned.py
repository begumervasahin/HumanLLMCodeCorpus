import unittest
from otp import encrypt, decrypt
class class1(unittest.TestCase):
    def fonk1(self):
        self.b1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    def fonk2(self):
        b2 = "HELLO"
        b3 = "XMCKL"
        b4 = "EQNVZ"
        b5 = encrypt(b2, b3, self.b1)
        self.assertEqual(b5, b4,
                         f"Expected b6 '{b4}' but got '{b5}'")
    def fonk3(self):
        b6 = "EQNVZ"
        b3 = "XMCKL"
        b7 = "HELLO"
        b8 = decrypt(b6, b3, self.b1)
        self.assertEqual(b8, b7,
                         f"Expected b2 '{b7}' but got '{b8}'")
if b9 = = '__main__':
    unittest.main()