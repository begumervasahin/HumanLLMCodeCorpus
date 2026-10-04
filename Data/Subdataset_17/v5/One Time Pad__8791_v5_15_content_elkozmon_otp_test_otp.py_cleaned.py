import unittest
from otp import encrypt, decrypt
class OtpEncryptionTests(unittest.TestCase):
    def setUp(self):
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    def test_encrypt_hello(self):
        plaintext = "HELLO"
        key = "XMCKL"
        expected_ciphertext = "EQNVZ"
        actual_ciphertext = encrypt(plaintext, key, self.alphabet)
        self.assertEqual(actual_ciphertext, expected_ciphertext,
                         f"Expected ciphertext '{expected_ciphertext}' but got '{actual_ciphertext}'")
    def test_decrypt_hello(self):
        ciphertext = "EQNVZ"
        key = "XMCKL"
        expected_plaintext = "HELLO"
        actual_plaintext = decrypt(ciphertext, key, self.alphabet)
        self.assertEqual(actual_plaintext, expected_plaintext,
                         f"Expected plaintext '{expected_plaintext}' but got '{actual_plaintext}'")
if __name__ == '__main__':
    unittest.main()