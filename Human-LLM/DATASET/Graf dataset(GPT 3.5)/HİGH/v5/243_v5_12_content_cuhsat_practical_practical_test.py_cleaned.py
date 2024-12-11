
import sys
import re
import pytest
from b2 import Practical
try:
    import pytest
except ImportError:
    sys.exit("Requires pytest")
class class1:
    b1 = [
        ("AAAAAA", "999999", "999999"),
        ("999999", "999999", "AAAAAA"),
        ("A9A9A9", "A9A9A9", "AAAAAA"),
    ]
    def fonk1(self):
        for b6, expected_ciphertext, b4 in self.b1:
            assert Practical().encrypt(b6, b4) == expected_ciphertext
    def fonk2(self):
        for expected_plaintext, b5, b4 in self.b1:
            assert Practical().decrypt(b5, b4) == expected_plaintext
    def fonk3(self):
        assert re.match("^([A-Z0-9]|\s)+$", Practical().b4())
    def fonk4(self):
        b2 = Practical()
        for length in range(1000):
            b3 = b2.b4(length, 1, 1)
            b4 = b2.b4(length, 1, 1)
            b5 = b2.encrypt(b3, b4)
            b6 = b2.decrypt(b5, b4)
            assert b6 = = b3
if b7 = = "__main__":
    sys.exit(pytest.main(list(sys.argv)))