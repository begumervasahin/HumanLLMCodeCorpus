from difflib import ndiff, restore
original_lines = 'one\ntwo\nthree\n'.splitlines(keepends=True)
modified_lines = 'ore\ntree\nemu\n'.splitlines(keepends=True)
diff = ndiff(original_lines, modified_lines)
diff = list(diff)
restored_original = ''.join(restore(diff, 1))
restored_modified = ''.join(restore(diff, 2))
print(restored_original, end="")
print(restored_modified, end="")