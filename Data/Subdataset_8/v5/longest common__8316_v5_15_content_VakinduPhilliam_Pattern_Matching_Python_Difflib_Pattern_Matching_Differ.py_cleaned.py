import sys
from difflib import context_diff
def compute_list_differences(list1, list2):
    return context_diff(list1, list2, fromfile='before.py', tofile='after.py')
def display_differences(diff):
    for line in diff:
        sys.stdout.write(line)
if __name__ == "__main__":
    original_list = ['bacon\n', 'eggs\n', 'ham\n', 'guido\n']
    modified_list = ['python\n', 'eggy\n', 'hamster\n', 'guido\n']
    differences = compute_list_differences(original_list, modified_list)
    display_differences(differences)