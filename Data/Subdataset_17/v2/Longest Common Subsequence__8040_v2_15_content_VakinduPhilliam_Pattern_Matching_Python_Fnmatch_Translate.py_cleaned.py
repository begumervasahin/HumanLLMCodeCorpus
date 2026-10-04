import fnmatch
import re
pattern = '*.txt'
regex = fnmatch.translate(pattern)
print(f"Translated regex: {regex}")
compiled_regex = re.compile(regex)
test_string = 'foobar.txt'
if compiled_regex.match(test_string):
    print(f"The string '{test_string}' matches the pattern '{pattern}'")
else:
    print(f"The string '{test_string}' does not match the pattern '{pattern}'")