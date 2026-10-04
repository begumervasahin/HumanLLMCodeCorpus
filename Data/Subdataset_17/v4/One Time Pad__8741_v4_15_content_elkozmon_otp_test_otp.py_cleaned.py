import unittest
from otp import encrypt, decrypt
class OtpTestCase(unittest.TestCase):
    def setUp(self):
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    def test_encrypt_hello(self):
        plaintext = "HELLO"
        key = "XMCKL"
        expected_ciphertext = "EQNVZ"
        self.assertEqual(encrypt(plaintext, key, self.alphabet), expected_ciphertext)
    def test_decrypt_hello(self):
        ciphertext = "EQNVZ"
        key = "XMCKL"
        expected_plaintext = "HELLO"
        self.assertEqual(decrypt(ciphertext, key, self.alphabet), expected_plaintext)
if __name__ == '__main__':
    unittest.main()