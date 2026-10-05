from difflib import ndiff
b1 = 'one\ntwo\nthree\n'
b2 = 'ore\ntree\nemu\n'
b3 = b1.splitlines(keepends=True)
b4 = b2.splitlines(keepends=True)
b5 = ndiff(b3, b4)
b6 = ''.join(line[2:] for line in b5 if line.startswith(' '))
b7 = ''.join(line[2:] for line in b5 if line.startswith('+'))
print(b6, b8 = "")
print(b7, b8 = "")