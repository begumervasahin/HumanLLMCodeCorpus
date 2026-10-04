import difflib
b1 = 'one\ntwo\nthree\n'
b2 = 'ore\ntree\nemu\n'
b3 = b1.splitlines(keepends=True)
b4 = b2.splitlines(keepends=True)
b5 = difflib.Differ()
b6 = b5.ndiff(b3, b4)
print(''.join(b6), b7 = "")