import difflib
b1 = 'one\ntwo\nthree\n'
b2 = 'ore\ntree\nemu\n'
b3 = b1.splitlines(keepends=True)
b4 = b2.splitlines(keepends=True)
b5 = difflib.Differ()
b6 = list(b5.compare(b3, b4))
b7 = difflib.restore(b6, 1)
b8 = difflib.restore(b6, 2)
b9 = ''.join(b7)
b10 = ''.join(b8)
print(b9, b11 = "")
print(b10, b11 = "")