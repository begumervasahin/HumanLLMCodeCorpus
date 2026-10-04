from difflib import ndiff, restore
string1 = 'one\ntwo\nthree\n'
string2 = 'ore\ntree\nemu\n'
lines1 = string1.splitlines(keepends=True)
lines2 = string2.splitlines(keepends=True)
diff = ndiff(lines1, lines2)
diff_list = list(diff)
restored1 = ''.join(restore(diff_list, 1))
restored2 = ''.join(restore(diff_list, 2))
print(restored1, end="")
print(restored2, end="")