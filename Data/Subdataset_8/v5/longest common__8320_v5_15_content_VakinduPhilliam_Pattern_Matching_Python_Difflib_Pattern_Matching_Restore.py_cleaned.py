from difflib import ndiff
original_text = 'one\ntwo\nthree\n'
modified_text = 'ore\ntree\nemu\n'
original_lines = original_text.splitlines(keepends=True)
modified_lines = modified_text.splitlines(keepends=True)
line_diffs = ndiff(original_lines, modified_lines)
restored_original = ''.join(line[2:] for line in line_diffs if line.startswith(' '))
restored_modified = ''.join(line[2:] for line in line_diffs if line.startswith('+'))
print(restored_original, end="")
print(restored_modified, end="")