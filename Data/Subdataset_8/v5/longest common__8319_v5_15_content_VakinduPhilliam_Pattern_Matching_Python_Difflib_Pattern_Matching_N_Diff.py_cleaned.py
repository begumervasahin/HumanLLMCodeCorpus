
first_lines = 'one\ntwo\nthree\n'.splitlines(keepends=True)
second_lines = 'ore\ntree\nemu\n'.splitlines(keepends=True)
line_difference = ndiff(first_lines, second_lines)
print(''.join(line_difference), end="")