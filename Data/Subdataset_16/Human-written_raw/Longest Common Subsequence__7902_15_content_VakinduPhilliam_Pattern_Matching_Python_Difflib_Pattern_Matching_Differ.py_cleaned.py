b1 = ['bacon\n', 'eggs\n', 'ham\n', 'guido\n']
b2 = ['python\n', 'eggy\n', 'hamster\n', 'guido\n']
sys.stdout.writelines(context_diff(b1, b2, b3 = 'before.py', tofile='after.py'))