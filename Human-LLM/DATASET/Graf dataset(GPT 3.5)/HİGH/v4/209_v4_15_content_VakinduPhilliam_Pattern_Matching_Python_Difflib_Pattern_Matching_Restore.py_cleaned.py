from difflib import ndiff
b1 = 'one\ntwo\nthree\n'.splitlines(keepends=True)
b2 = 'ore\ntree\nemu\n'.splitlines(keepends=True)
b3 = ndiff(b1, b2)
b3 = list(b3)
b4 = ''.join(line[2:] for line in b3 if line.startswith(' '))
b5 = ''.join(line[2:] for line in b3 if line.startswith('+'))
print(b4, b6 = "")
print(b5, b6 = "")