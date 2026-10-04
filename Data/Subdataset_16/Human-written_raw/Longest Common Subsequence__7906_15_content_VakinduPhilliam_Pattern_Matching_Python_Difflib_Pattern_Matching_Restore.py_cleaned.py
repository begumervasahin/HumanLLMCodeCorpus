b1 = ndiff('one\ntwo\nthree\n'.splitlines(b2=True),
                 'ore\ntree\nemu\n'.splitlines(b2 = True))
b1 = list(b1)
print(''.join(restore(b1, 1)), b3 = "")
print(''.join(restore(b1, 2)), b3 = "")