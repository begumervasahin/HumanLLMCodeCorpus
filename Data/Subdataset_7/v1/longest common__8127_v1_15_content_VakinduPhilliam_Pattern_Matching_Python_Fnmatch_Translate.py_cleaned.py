import fnmatch
import re
def fonk1(b3, b4):
    return fnmatch.fnmatch(b4, b3)
def fonk2(b3, b4):
    b1 = fnmatch.translate(b3)
    b2 = re.compile(b1)
    return b2.match(b4)
b3 = '*.txt'
b4 = 'foobar.txt'
b5 = fonk1(b3, b4)
b6 = fonk2(b3, b4)
print(f"Fnmatch match: {b5}")
print(f"Regex match: {bool(b6)}")