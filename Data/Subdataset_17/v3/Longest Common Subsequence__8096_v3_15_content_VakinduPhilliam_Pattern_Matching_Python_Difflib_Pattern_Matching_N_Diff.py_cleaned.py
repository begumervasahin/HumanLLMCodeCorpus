import difflib
def compare_strings(str1, str2):
    lines1 = str1.splitlines(keepends=True)
    lines2 = str2.splitlines(keepends=True)
    differ = difflib.Differ()
    diff = differ.ndiff(lines1, lines2)
    print(''.join(diff), end="")
string1 = 'one\ntwo\nthree\n'
string2 = 'ore\ntree\nemu\n'
compare_strings(string1, string2)