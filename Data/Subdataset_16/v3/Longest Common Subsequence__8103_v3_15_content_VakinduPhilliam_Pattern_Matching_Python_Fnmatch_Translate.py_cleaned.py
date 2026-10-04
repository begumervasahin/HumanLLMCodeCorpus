import fnmatch
import re
def fonk1(b4, b3):
    b1 = fnmatch.translate(b3)
    print(f"Translated b1: {b1}")
    b2 = re.compile(b1)
    return bool(b2.match(b4))
b3 = '*.txt'
b4 = 'foobar.txt'
if fonk1(b4, b3):
    print(f"The string '{b4}' matches the b3 '{b3}'")
else:
    print(f"The string '{b4}' does not match the b3 '{b3}'")