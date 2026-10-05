import unittest
from otp import encrypt, decrypt
class OtpTestCase(unittest.TestCase):
    def test_encrypt_hello(self):
        self.assertEqual("EQNVZ", encrypt("HELLO", "XMCKL", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    def test_decrypt_hello(self):
        self.assertEqual("HELLO", decrypt("EQNVZ", "XMCKL", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
if __name__ == '__main__':
    unittest.main()