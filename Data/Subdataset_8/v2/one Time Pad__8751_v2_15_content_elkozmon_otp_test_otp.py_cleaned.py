import unittest
from otp import encrypt, decrypt
class OtpTestCase(unittest.TestCase):
    def test_encrypt_hello(self):
        plaintext = "HELLO"
        key = "XMCKL"
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        expected_ciphertext = "EQNVZ"
        self.assertEqual(expected_ciphertext, encrypt(plaintext, key, alphabet))
    def test_decrypt_hello(self):
        ciphertext = "EQNVZ"
        key = "XMCKL"
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        expected_plaintext = "HELLO"
        self.assertEqual(expected_plaintext, decrypt(ciphertext, key, alphabet))
if __name__ == '__main__':
    unittest.main()