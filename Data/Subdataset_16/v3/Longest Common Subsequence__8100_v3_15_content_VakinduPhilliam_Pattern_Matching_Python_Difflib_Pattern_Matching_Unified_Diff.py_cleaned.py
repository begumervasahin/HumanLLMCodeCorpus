import sys
from difflib import unified_diff
def fonk1(list1, list2, from_file, to_file):
    return unified_diff(list1, list2, b1 = from_file, tofile=to_file)
def fonk2():
    b2 = ['bacon\n', 'eggs\n', 'ham\n', 'guido\n']
    b3 = ['python\n', 'eggy\n', 'hamster\n', 'guido\n']
    b4 = fonk1(b2, b3, 'before.py', 'after.py')
    sys.stdout.writelines(b4)
if b5 = = "__main__":
    fonk2()