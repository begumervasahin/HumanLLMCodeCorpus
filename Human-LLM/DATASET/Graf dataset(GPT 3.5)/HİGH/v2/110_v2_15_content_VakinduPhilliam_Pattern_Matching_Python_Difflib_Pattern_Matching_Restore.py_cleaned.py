from difflib import ndiff, restore
b1 = 'one\ntwo\nthree\n'.splitlines(keepends=True)
b2 = 'ore\ntree\nemu\n'.splitlines(keepends=True)
b3 = ndiff(b1, b2)
b3 = list(b3)
b4 = ''.join(restore(b3, 1))
b5 = ''.join(restore(b3, 2))
print(b4, b6 = "")
print(b5, b6 = "")