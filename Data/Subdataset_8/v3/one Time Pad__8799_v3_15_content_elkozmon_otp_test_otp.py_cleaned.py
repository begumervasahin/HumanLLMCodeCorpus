import unittest
from otp import encrypt, decrypt
class OtpTestCase(unittest.TestCase):
    def test_encrypt_hello(self):
        plaintext = "HELLO"
        key = "XMCKL"
        ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        expected_ciphertext = "EQNVZ"
        self.assertEqual(expected_ciphertext, encrypt(plaintext, key, ALPHABET))
    def test_decrypt_hello(self):
        ciphertext = "EQNVZ"
        key = "XMCKL"
        ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        expected_plaintext = "HELLO"
        self.assertEqual(expected_plaintext, decrypt(ciphertext, key, ALPHABET))
if __name__ == '__main__':
    unittest.main()