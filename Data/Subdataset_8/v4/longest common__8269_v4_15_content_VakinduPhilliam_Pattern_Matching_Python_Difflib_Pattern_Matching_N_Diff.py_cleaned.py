
first_list = 'one\ntwo\nthree\n'.splitlines(keepends=True)
second_list = 'ore\ntree\nemu\n'.splitlines(keepends=True)
difference = ndiff(first_list, second_list)
print(''.join(difference), end="")