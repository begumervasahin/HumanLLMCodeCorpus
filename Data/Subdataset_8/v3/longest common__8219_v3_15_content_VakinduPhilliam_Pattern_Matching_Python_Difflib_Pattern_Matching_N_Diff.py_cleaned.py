from difflib import ndiff
original_text = 'one\ntwo\nthree\n'.splitlines(keepends=True)
modified_text = 'ore\ntree\nemu\n'.splitlines(keepends=True)
differences = ndiff(original_text, modified_text)
print(''.join(differences), end="")