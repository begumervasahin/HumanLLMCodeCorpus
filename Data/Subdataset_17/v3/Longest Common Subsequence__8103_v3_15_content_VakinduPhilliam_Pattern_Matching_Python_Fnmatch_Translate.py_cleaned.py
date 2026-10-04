import fnmatch
import re
def matches_pattern(test_string, pattern):
    regex = fnmatch.translate(pattern)
    print(f"Translated regex: {regex}")
    compiled_regex = re.compile(regex)
    return bool(compiled_regex.match(test_string))
pattern = '*.txt'
test_string = 'foobar.txt'
if matches_pattern(test_string, pattern):
    print(f"The string '{test_string}' matches the pattern '{pattern}'")
else:
    print(f"The string '{test_string}' does not match the pattern '{pattern}'")