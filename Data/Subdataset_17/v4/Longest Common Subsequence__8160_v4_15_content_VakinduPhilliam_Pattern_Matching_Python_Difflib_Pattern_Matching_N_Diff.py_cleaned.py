from difflib import ndiff
original_text = 'one\ntwo\nthree\n'
modified_text = 'ore\ntree\nemu\n'
original_lines = original_text.splitlines(keepends=True)
modified_lines = modified_text.splitlines(keepends=True)
diff = ndiff(original_lines, modified_lines)
print(''.join(diff), end="")