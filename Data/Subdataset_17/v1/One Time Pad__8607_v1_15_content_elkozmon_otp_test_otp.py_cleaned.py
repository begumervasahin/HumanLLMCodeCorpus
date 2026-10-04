def encrypt(plaintext, key, alphabet):
    ciphertext = []
    alphabet_size = len(alphabet)
    for p, k in zip(plaintext, key):
        p_index = alphabet.index(p)
        k_index = alphabet.index(k)
        c_index = (p_index + k_index) % alphabet_size
        ciphertext.append(alphabet[c_index])
    return ''.join(ciphertext)
def decrypt(ciphertext, key, alphabet):
    plaintext = []
    alphabet_size = len(alphabet)
    for c, k in zip(ciphertext, key):
        c_index = alphabet.index(c)
        k_index = alphabet.index(k)
        p_index = (c_index - k_index) % alphabet_size
        plaintext.append(alphabet[p_index])
    return ''.join(plaintext)
import unittest
from otp import encrypt, decrypt
class OtpTestCase(unittest.TestCase):
    def test_encrypt_hello(self):
        self.assertEqual("EQNVZ", encrypt("HELLO", "XMCKL", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    def test_decrypt_hello(self):
        self.assertEqual("HELLO", decrypt("EQNVZ", "XMCKL", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
if __name__ == '__main__':
    unittest.main()