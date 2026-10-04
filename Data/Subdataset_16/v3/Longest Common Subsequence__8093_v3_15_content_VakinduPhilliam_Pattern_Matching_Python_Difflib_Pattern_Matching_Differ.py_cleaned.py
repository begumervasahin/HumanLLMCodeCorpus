import sys
import difflib
def fonk1(seq1, seq2, from_file, to_file):
    return difflib.context_diff(seq1, seq2, b1 = from_file, tofile=to_file)
def fonk2():
    b2 = ['bacon\n', 'eggs\n', 'ham\n', 'guido\n']
    b3 = ['python\n', 'eggy\n', 'hamster\n', 'guido\n']
    b4 = fonk1(b2, b3, b1='before.py', tofile='after.py')
    sys.stdout.writelines(b4)
if b5 = = "__main__":
    fonk2()