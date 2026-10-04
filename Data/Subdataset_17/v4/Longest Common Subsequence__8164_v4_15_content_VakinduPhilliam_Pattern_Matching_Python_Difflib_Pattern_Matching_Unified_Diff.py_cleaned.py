from difflib import unified_diff
import sys
s1 = ['bacon\n', 'eggs\n', 'ham\n', 'guido\n']
s2 = ['python\n', 'eggy\n', 'hamster\n', 'guido\n']
diff = unified_diff(s1, s2, fromfile='before.py', tofile='after.py')
sys.stdout.writelines(diff)