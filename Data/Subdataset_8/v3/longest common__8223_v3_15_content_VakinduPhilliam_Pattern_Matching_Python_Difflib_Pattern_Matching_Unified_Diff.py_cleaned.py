import sys
from difflib import unified_diff
def generate_unified_diff(original, modified, from_file='before.py', to_file='after.py'):
    return unified_diff(original, modified, fromfile=from_file, tofile=to_file, lineterm='')
def main():
    original_list = ['bacon\n', 'eggs\n', 'ham\n', 'guido\n']
    modified_list = ['python\n', 'eggy\n', 'hamster\n', 'guido\n']
    sys.stdout = sys.stdout.detach()
    diff_lines = generate_unified_diff(original_list, modified_list)
    sys.stdout.writelines(diff_lines)
if __name__ == "__main__":
    main()