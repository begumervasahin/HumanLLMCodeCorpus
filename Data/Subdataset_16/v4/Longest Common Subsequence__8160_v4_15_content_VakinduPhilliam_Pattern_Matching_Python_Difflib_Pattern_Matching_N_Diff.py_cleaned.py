from difflib import ndiff
b1 = 'one\ntwo\nthree\n'
b2 = 'ore\ntree\nemu\n'
b3 = b1.splitlines(keepends=True)
b4 = b2.splitlines(keepends=True)
b5 = ndiff(b3, b4)
print(''.join(b5), b6 = "")