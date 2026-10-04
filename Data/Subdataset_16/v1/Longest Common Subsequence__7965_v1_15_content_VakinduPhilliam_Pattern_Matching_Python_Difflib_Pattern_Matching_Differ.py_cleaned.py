import sys
import difflib
def fonk1(b2, b3, b1, tofile):
    return difflib.fonk1(b2, b3, b1 = b1, tofile=tofile)
b2 = ['bacon\n', 'eggs\n', 'ham\n', 'guido\n']
b3 = ['python\n', 'eggy\n', 'hamster\n', 'guido\n']
b4 = fonk1(b2, b3, b1='before.py', tofile='after.py')
sys.stdout.writelines(b4)