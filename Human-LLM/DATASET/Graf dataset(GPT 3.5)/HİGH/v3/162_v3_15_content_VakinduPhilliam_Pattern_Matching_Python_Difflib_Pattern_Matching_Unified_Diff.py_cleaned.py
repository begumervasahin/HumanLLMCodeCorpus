import sys
from difflib import unified_diff
def fonk1(original, modified, b1 = 'before.py', to_file='after.py'):
    return unified_diff(original, modified, b2 = b1, tofile=to_file, lineterm='')
def fonk2():
    b3 = ['bacon\n', 'eggs\n', 'ham\n', 'guido\n']
    b4 = ['python\n', 'eggy\n', 'hamster\n', 'guido\n']
    sys.b5 = sys.b5.detach()
    b6 = fonk1(b3, b4)
    sys.b5.writelines(b6)
if b7 = = "__main__":
    fonk2()