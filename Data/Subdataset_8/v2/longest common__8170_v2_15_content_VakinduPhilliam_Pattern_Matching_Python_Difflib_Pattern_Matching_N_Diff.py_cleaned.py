
from difflib import ndiff
text1 = 'one\ntwo\nthree\n'.splitlines(keepends=True)
text2 = 'ore\ntree\nemu\n'.splitlines(keepends=True)
diff = ndiff(text1, text2)
print(''.join(diff), end="")