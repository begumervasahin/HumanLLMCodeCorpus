import sys
from difflib import unified_diff
b1 = ['bacon\n', 'eggs\n', 'ham\n', 'guido\n']
b2 = ['python\n', 'eggy\n', 'hamster\n', 'guido\n']
sys.b3 = sys.b3.detach()
b4 = unified_diff(b1, b2, fromfile='before.py', tofile='after.py', lineterm='')
sys.b3.writelines(b4)