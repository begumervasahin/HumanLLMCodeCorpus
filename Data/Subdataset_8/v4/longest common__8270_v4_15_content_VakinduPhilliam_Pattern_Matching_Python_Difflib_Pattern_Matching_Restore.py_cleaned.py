from difflib import ndiff
original_lines = 'one\ntwo\nthree\n'.splitlines(keepends=True)
modified_lines = 'ore\ntree\nemu\n'.splitlines(keepends=True)
differences = ndiff(original_lines, modified_lines)
differences = list(differences)
restored_original = ''.join(line[2:] for line in differences if line.startswith(' '))
restored_modified = ''.join(line[2:] for line in differences if line.startswith('+'))
print(restored_original, end="")
print(restored_modified, end="")