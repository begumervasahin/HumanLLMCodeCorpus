import sys
import difflib
def generate_context_diff(seq1, seq2, from_file, to_file):
    return difflib.context_diff(seq1, seq2, fromfile=from_file, tofile=to_file)
def main():
    list1 = ['bacon\n', 'eggs\n', 'ham\n', 'guido\n']
    list2 = ['python\n', 'eggy\n', 'hamster\n', 'guido\n']
    diff_result = generate_context_diff(list1, list2, fromfile='before.py', tofile='after.py')
    sys.stdout.writelines(diff_result)
if __name__ == "__main__":
    main()