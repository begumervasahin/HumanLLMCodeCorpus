import sys
from difflib import unified_diff
def generate_diff(list1, list2, from_file, to_file):
    return unified_diff(list1, list2, fromfile=from_file, tofile=to_file)
def main():
    s1 = ['bacon\n', 'eggs\n', 'ham\n', 'guido\n']
    s2 = ['python\n', 'eggy\n', 'hamster\n', 'guido\n']
    diff = generate_diff(s1, s2, 'before.py', 'after.py')
    sys.stdout.writelines(diff)
if __name__ == "__main__":
    main()