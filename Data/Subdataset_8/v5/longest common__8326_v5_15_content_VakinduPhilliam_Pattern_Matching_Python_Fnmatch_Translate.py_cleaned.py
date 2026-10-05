import fnmatch
import re
file_pattern = '*.txt'
regex_pattern = fnmatch.translate(file_pattern)
regex_object = re.compile(regex_pattern)
is_match = regex_object.match('foobar.txt')