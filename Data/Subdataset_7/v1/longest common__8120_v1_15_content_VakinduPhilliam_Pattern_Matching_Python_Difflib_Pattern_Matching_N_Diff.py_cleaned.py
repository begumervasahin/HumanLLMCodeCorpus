from difflib import ndiff
b1 = ndiff('one\ntwo\nthree\n'.splitlines(b2=True),
             'ore\ntree\nemu\n'.splitlines(b2 = True))
print(''.join(b1), b3 = "")