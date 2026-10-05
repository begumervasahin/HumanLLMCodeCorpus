import unittest
from otp import encrypt, decrypt
class TestOtp(unittest.TestCase):
    def test_encrypt_hello_with_key_xmckl_results_in_ciphertext_eqnvz(self):
        plaintext = "HELLO"
        key = "XMCKL"
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        ciphertext = encrypt(plaintext, key, alphabet)
        self.assertEqual(ciphertext, "EQNVZ")
    def test_decrypt_eqnvz_with_key_xmckl_results_in_plaintext_hello(self):
        ciphertext = "EQNVZ"
        key = "XMCKL"
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        plaintext = decrypt(ciphertext, key, alphabet)
        self.assertEqual(plaintext, "HELLO")
if __name__ == '__main__':
    unittest.main()