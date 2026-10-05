import fnmatch
import re
regex_pattern = fnmatch.translate('*.txt')
regex_object = re.compile(regex_pattern)
match_result = regex_object.match('foobar.txt')