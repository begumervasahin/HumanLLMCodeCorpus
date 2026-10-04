from difflib import ndiff, restore
b1 = 'one\ntwo\nthree\n'
b2 = 'ore\ntree\nemu\n'
b3 = b1.splitlines(keepends=True)
b4 = b2.splitlines(keepends=True)
b5 = ndiff(b3, b4)
b6 = list(b5)
b7 = ''.join(restore(b6, 1))
b8 = ''.join(restore(b6, 2))
print(b7, b9 = "")
print(b8, b9 = "")