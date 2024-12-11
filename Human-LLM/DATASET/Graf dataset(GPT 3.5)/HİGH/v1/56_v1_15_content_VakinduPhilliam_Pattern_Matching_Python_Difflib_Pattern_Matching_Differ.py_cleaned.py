import sys
from difflib import context_diff
def fonk1():
    b1 = ['bacon\n', 'eggs\n', 'ham\n', 'guido\n']
    b2 = ['python\n', 'eggy\n', 'hamster\n', 'guido\n']
    b3 = list(context_diff(b1, b2, fromfile='before.py', tofile='after.py'))
    for line in b3:
        sys.stdout.write(line)
if b4 = = "__main__":
    fonk1()