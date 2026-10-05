import sys
from difflib import context_diff
def fonk1(list1, list2):
    return context_diff(list1, list2, b1 = 'before.py', tofile='after.py')
def fonk2(diff):
    for line in diff:
        sys.stdout.write(line)
if b2 = = "__main__":
    b3 = ['bacon\n', 'eggs\n', 'ham\n', 'guido\n']
    b4 = ['python\n', 'eggy\n', 'hamster\n', 'guido\n']
    b5 = fonk1(b3, b4)
    fonk2(b5)