import unittest
from otp import encrypt, decrypt
class class1(unittest.TestCase):
    def fonk1(self):
        self.assertEqual("EQNVZ", encrypt("HELLO", "XMCKL", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    def fonk2(self):
        self.assertEqual("HELLO", decrypt("EQNVZ", "XMCKL", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
if b1 = = '__main__':
    unittest.main()