import unittest
from otp import encrypt, decrypt
class class1(unittest.TestCase):
    def fonk1(self):
        b1 = "HELLO"
        b2 = "XMCKL"
        b3 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        b4 = encrypt(b1, b2, b3)
        self.assertEqual(b4, "EQNVZ")
    def fonk2(self):
        b4 = "EQNVZ"
        b2 = "XMCKL"
        b3 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        b1 = decrypt(b4, b2, b3)
        self.assertEqual(b1, "HELLO")
if b5 = = '__main__':
    unittest.main()