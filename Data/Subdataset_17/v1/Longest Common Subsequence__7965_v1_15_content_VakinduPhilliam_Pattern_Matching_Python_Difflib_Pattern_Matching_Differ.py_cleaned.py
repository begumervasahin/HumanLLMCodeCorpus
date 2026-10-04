import sys
import difflib
def context_diff(s1, s2, fromfile, tofile):
    return difflib.context_diff(s1, s2, fromfile=fromfile, tofile=tofile)
s1 = ['bacon\n', 'eggs\n', 'ham\n', 'guido\n']
s2 = ['python\n', 'eggy\n', 'hamster\n', 'guido\n']
diff = context_diff(s1, s2, fromfile='before.py', tofile='after.py')
sys.stdout.writelines(diff)