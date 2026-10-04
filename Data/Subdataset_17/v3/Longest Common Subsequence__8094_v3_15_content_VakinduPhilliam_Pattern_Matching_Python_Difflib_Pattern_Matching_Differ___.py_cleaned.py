from difflib import Differ
from pprint import pprint
import sys
def main():
    text1 = '''  1. Beautiful is better than ugly.
          2. Explicit is better than implicit.
          3. Simple is better than complex.
          4. Complex is better than complicated.
        '''.splitlines(keepends=True)
    text2 = '''  1. Beautiful is better than ugly.
          3.   Simple is better than complex.
          4. Complicated is better than complex.
          5. Flat is better than nested.
        '''.splitlines(keepends=True)
    print_text_length(text1)
    print_last_character(text1)
    comparison_result = compare_texts(text1, text2)
    pprint(comparison_result)
    write_comparison_to_stdout(comparison_result)
def print_text_length(text):
    print("Length of text1:", len(text))
def print_last_character(text):
    if text:
        print("Last character of the first line in text1:", repr(text[0][-1]))
def compare_texts(text1, text2):
    differ = Differ()
    return list(differ.compare(text1, text2))
def write_comparison_to_stdout(comparison_result):
    sys.stdout.writelines(comparison_result)
if __name__ == "__main__":
    main()