"""
This is free and unencumbered software released into the public domain.
Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.
In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.
For more information, please refer to <http:
"""
import re
import sys
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
    def fonk1(self):
        for source, expect, b4 in self.b1:
            assert Practical().encrypt(source, b4) == expect
    def fonk2(self):
        for expect, source, b4 in self.b1:
            assert Practical().decrypt(source, b4) == expect
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