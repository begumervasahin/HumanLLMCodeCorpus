import fnmatch
import re
b1 = '*.txt'
b2 = fnmatch.translate(b1)
print(f"Translated b2: {b2}")
b3 = re.compile(b2)
b4 = 'foobar.txt'
if b3.match(b4):
    print(f"The string '{b4}' matches the b1 '{b1}'")
else:
    print(f"The string '{b4}' does not match the b1 '{b1}'")