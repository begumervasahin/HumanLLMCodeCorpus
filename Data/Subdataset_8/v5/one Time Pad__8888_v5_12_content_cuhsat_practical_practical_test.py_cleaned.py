
import sys
import re
import pytest
from practical import Practical
try:
    import pytest
except ImportError:
    sys.exit("Requires pytest")
class TestPracticalCipher:
    TEST_VECTORS = [
        ("AAAAAA", "999999", "999999"),
        ("999999", "999999", "AAAAAA"),
        ("A9A9A9", "A9A9A9", "AAAAAA"),
    ]
    def test_encrypt(self):
        for plaintext, expected_ciphertext, key in self.TEST_VECTORS:
            assert Practical().encrypt(plaintext, key) == expected_ciphertext
    def test_decrypt(self):
        for expected_plaintext, ciphertext, key in self.TEST_VECTORS:
            assert Practical().decrypt(ciphertext, key) == expected_plaintext
    def test_key_generation(self):
        assert re.match("^([A-Z0-9]|\s)+$", Practical().key())
    def test_random_data(self):
        practical = Practical()
        for length in range(1000):
            text = practical.key(length, 1, 1)
            key = practical.key(length, 1, 1)
            ciphertext = practical.encrypt(text, key)
            plaintext = practical.decrypt(ciphertext, key)
            assert plaintext == text
if __name__ == "__main__":
    sys.exit(pytest.main(list(sys.argv)))