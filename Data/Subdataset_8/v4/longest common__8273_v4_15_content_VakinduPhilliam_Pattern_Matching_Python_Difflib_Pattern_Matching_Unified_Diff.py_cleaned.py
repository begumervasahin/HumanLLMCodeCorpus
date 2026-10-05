import sys
from difflib import unified_diff
before_changes = ['bacon\n', 'eggs\n', 'ham\n', 'guido\n']
after_changes = ['python\n', 'eggy\n', 'hamster\n', 'guido\n']
differences = unified_diff(before_changes, after_changes, fromfile='before.py', tofile='after.py')
sys.stdout.writelines(differences)