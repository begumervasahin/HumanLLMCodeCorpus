from difflib import unified_diff
import sys
b1 = ['bacon\n', 'eggs\n', 'ham\n', 'guido\n']
b2 = ['python\n', 'eggy\n', 'hamster\n', 'guido\n']
b3 = unified_diff(b1, b2, fromfile='before.py', tofile='after.py')
sys.stdout.writelines(b3)