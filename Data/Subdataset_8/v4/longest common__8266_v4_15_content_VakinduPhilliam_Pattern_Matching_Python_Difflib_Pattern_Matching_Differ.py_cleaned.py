import sys
from difflib import context_diff
s1 = ['bacon\n', 'eggs\n', 'ham\n', 'guido\n']
s2 = ['python\n', 'eggy\n', 'hamster\n', 'guido\n']
diff = context_diff(s1, s2, fromfile='before.py', tofile='after.py')
for line in diff:
    sys.stdout.write(line)