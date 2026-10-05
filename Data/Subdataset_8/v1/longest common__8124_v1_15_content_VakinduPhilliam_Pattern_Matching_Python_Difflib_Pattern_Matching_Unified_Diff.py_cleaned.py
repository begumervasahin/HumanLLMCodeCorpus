import sys
from difflib import unified_diff
s1 = ['bacon\n', 'eggs\n', 'ham\n', 'guido\n']
s2 = ['python\n', 'eggy\n', 'hamster\n', 'guido\n']
sys.stdout = sys.stdout.detach()
sys.stdout.writelines(unified_diff(s1, s2, fromfile='before.py', tofile='after.py', lineterm=''))