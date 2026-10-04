diff = ndiff('one\ntwo\nthree\n'.splitlines(keepends=True),
                 'ore\ntree\nemu\n'.splitlines(keepends=True))
diff = list(diff)
print(''.join(restore(diff, 1)), end="")
print(''.join(restore(diff, 2)), end="")