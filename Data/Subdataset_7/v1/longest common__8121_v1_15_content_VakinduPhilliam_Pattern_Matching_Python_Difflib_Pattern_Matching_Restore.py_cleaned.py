from difflib import ndiff, restore
b1 = ndiff('one\ntwo\nthree\n'.splitlines(b2=True),
             'ore\ntree\nemu\n'.splitlines(b2 = True))
b1 = list(b1)
b3 = ''.join(restore(b1, 1))
b4 = ''.join(restore(b1, 2))
print(b3, b5 = "")
print(b4, b5 = "")