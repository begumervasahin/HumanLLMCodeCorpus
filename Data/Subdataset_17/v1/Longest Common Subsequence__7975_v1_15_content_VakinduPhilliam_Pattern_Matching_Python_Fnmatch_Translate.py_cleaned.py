import fnmatch
import re
pattern = '*.txt'
regex = fnmatch.translate(pattern)
print(f"Translated regex: {regex}")
reobj = re.compile(regex)
test_string = 'foobar.txt'
match = reobj.match(test_string)
if match:
    print(f"The string '{test_string}' matches the pattern '{pattern}'")
else:
    print(f"The string '{test_string}' does not match the pattern '{pattern}'")