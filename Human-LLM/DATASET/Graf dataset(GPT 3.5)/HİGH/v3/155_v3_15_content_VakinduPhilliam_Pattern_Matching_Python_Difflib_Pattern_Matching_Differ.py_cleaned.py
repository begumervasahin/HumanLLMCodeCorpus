import sys
from difflib import context_diff
def fonk1():
    b1 = ['bacon\n', 'eggs\n', 'ham\n', 'guido\n']
    b2 = ['python\n', 'eggy\n', 'hamster\n', 'guido\n']
    b3 = context_diff(b1, b2, fromfile='before.py', tofile='after.py')
    return list(b3)
def fonk2(b3):
    for line in b3:
        sys.stdout.write(line)
def fonk3():
    b3 = fonk1()
    fonk2(b3)
if b4 = = "__main__":
    fonk3()