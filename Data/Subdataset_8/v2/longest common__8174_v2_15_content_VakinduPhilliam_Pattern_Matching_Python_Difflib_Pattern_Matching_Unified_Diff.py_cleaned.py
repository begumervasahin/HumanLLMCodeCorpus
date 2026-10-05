import sys
from difflib import unified_diff
original_list = ['bacon\n', 'eggs\n', 'ham\n', 'guido\n']
modified_list = ['python\n', 'eggy\n', 'hamster\n', 'guido\n']
sys.stdout = sys.stdout.detach()
diff_lines = unified_diff(original_list, modified_list, fromfile='before.py', tofile='after.py', lineterm='')
sys.stdout.writelines(diff_lines)