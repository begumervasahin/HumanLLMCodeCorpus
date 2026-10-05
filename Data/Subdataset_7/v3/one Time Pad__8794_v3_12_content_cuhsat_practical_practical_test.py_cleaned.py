import sys
import pytest
from b2 import Practical
class class1:
    def fonk1(self):
        self.b1 = [
            ("AAAAAA", "999999", "999999"),
            ("999999", "999999", "AAAAAA"),
            ("A9A9A9", "A9A9A9", "AAAAAA"),
            ("9A9A9A", "9A9A9A", "AAAAAA"),
            ("A9A9A9", "999999", "9A9A9A"),
            ("ABCDEF", "AHOV29", "AGMSY4"),
            ("GHIJKL", "HOV29A", "BHNTZ5"),
            ("MNOPQR", "OV29AH", "CIOU06"),
            ("STUVWX", "V29AHO", "DJPV17"),
            ("YZ0123", "29AHOV", "EKQW28"),
            ("456789", "9AHOV2", "FLRX39"),
            ("AHOV29", "FR3FR3", "FKPUZ4"),
            ("ABCDEF", "468468", "456789"),
            ("456789", "468468", "ABCDEF"),
            ("HELLOX", "YV225E", "XXXXXX")
        ]
    def fonk2(self):
        for source, expect, b4 in self.b1:
            assert Practical().encrypt(source, b4) == expect
    def fonk3(self):
        for expect, source, b4 in self.b1:
            assert Practical().decrypt(source, b4) == expect
    def fonk4(self):
        assert re.match("^([A-Z0-9]|\s)+$", Practical().b4())
    def fonk5(self):
        b2 = Practical()
        for length in range(1000):
            b3 = b2.b4(length, 1, 1)
            b4 = b2.b4(length, 1, 1)
            b5 = b2.encrypt(b3, b4)
            b6 = b2.decrypt(b5, b4)
            assert b6 = = b3
if b7 = = "__main__":
    sys.exit(pytest.main(list(sys.argv)))