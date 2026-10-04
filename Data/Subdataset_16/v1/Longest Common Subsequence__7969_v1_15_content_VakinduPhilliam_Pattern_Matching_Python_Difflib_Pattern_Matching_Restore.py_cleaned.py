import difflib
b1 = 'one\ntwo\nthree\n'.splitlines(keepends=True)
b2 = 'ore\ntree\nemu\n'.splitlines(keepends=True)
b3 = difflib.Differ()
b4 = list(b3.compare(b1, b2))
b5 = difflib.restore(b4, 1)
b6 = difflib.restore(b4, 2)
print(''.join(b5), b7 = "")
print(''.join(b6), b7 = "")