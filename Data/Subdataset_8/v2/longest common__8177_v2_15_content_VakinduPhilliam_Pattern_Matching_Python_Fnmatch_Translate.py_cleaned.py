import fnmatch
import re
def does_match_fnmatch(pattern, string):
    return fnmatch.fnmatch(string, pattern)
def does_match_regex(pattern, string):
    translated_regex = fnmatch.translate(pattern)
    compiled_regex = re.compile(translated_regex)
    return compiled_regex.match(string)
pattern = '*.txt'
string = 'foobar.txt'
fnmatch_result = does_match_fnmatch(pattern, string)
regex_result = does_match_regex(pattern, string)
print(f"Using fnmatch, the string matches the pattern: {fnmatch_result}")
print(f"Using regular expressions, the string matches the pattern: {bool(regex_result)}")