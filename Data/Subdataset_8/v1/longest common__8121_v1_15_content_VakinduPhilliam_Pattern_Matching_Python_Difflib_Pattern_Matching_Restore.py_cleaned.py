from difflib import ndiff, restore
diff = ndiff('one\ntwo\nthree\n'.splitlines(keepends=True),
             'ore\ntree\nemu\n'.splitlines(keepends=True))
diff = list(diff)
restored_1 = ''.join(restore(diff, 1))
restored_2 = ''.join(restore(diff, 2))
print(restored_1, end="")
print(restored_2, end="")