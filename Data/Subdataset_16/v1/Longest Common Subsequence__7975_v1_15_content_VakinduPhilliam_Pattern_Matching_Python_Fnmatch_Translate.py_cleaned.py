import fnmatch
import re
b1 = '*.txt'
b2 = fnmatch.translate(b1)
print(f"Translated b2: {b2}")
b3 = re.compile(b2)
b4 = 'foobar.txt'
b5 = b3.b5(b4)
if b5:
    print(f"The string '{b4}' matches the b1 '{b1}'")
else:
    print(f"The string '{b4}' does not b5 the b1 '{b1}'")