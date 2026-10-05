import sys
from difflib import context_diff
def generate_diff_lines():
    before_state = ['bacon\n', 'eggs\n', 'ham\n', 'guido\n']
    after_state = ['python\n', 'eggy\n', 'hamster\n', 'guido\n']
    diff_lines = context_diff(before_state, after_state, fromfile='before.py', tofile='after.py')
    return list(diff_lines)
def print_diff_lines(diff_lines):
    for line in diff_lines:
        sys.stdout.write(line)
def main():
    diff_lines = generate_diff_lines()
    print_diff_lines(diff_lines)
if __name__ == "__main__":
    main()