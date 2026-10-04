import fnmatch
import re
pattern = '*.txt'
regex = fnmatch.translate(pattern)
regex_object = re.compile(regex)
filename = 'foobar.txt'
match = regex_object.match(filename)
if match:
    print(f'The filename "{filename}" matches the pattern "{pattern}".')
else:
    print(f'The filename "{filename}" does not match the pattern "{pattern}".')