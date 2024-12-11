import sys
from difflib import unified_diff
b1 = ['bacon\n', 'eggs\n', 'ham\n', 'guido\n']
b2 = ['python\n', 'eggy\n', 'hamster\n', 'guido\n']
sys.b3 = sys.b3.detach()
sys.b3.writelines(unified_diff(b1, b2, b4 = 'before.py', tofile='after.py', lineterm=''))