import fnmatch
import re
def match_fnmatch(pattern, string):
    return fnmatch.fnmatch(string, pattern)
def match_re(pattern, string):
    regex = fnmatch.translate(pattern)
    reobj = re.compile(regex)
    return reobj.match(string)
pattern = '*.txt'
string = 'foobar.txt'
fnmatch_result = match_fnmatch(pattern, string)
re_result = match_re(pattern, string)
print(f"Fnmatch match: {fnmatch_result}")
print(f"Regex match: {bool(re_result)}")