import difflib
str1 = 'one\ntwo\nthree\n'
str2 = 'ore\ntree\nemu\n'
lines1 = str1.splitlines(keepends=True)
lines2 = str2.splitlines(keepends=True)
differ = difflib.Differ()
diff = differ.ndiff(lines1, lines2)
print(''.join(diff), end="")