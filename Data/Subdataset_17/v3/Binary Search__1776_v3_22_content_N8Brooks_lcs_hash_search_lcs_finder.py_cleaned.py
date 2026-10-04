import sys
import serial_hash_search
import parallel_hash_search
USE_PARALLEL_SEARCH = False
def read_text_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    except IOError as error:
        print(f"Error reading file '{file_path}': {error}")
        sys.exit(1)
def find_longest_common_substring(text_a, text_b):
    lcs_function = parallel_hash_search.lcs if USE_PARALLEL_SEARCH else serial_hash_search.lcs
    return lcs_function(text_a, text_b)
def print_lcs_results(lcs_length, lcs_substrings):
    plural_suffix = 's' if len(lcs_substrings) > 1 else ''
    verb = 'are' if len(lcs_substrings) > 1 else 'is'
    print(f'The length of the longest common substring is: {lcs_length}')
    print(f'There {verb} {len(lcs_substrings)} longest common substring{plural_suffix}:')
    for substring in lcs_substrings:
        print(f'"{substring}"')
def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <file1> <file2>")
        sys.exit(1)
    file_a, file_b = sys.argv[1], sys.argv[2]
    text_a = read_text_file(file_a)
    text_b = read_text_file(file_b)
    lcs_length, lcs_substrings = find_longest_common_substring(text_a, text_b)
    print_lcs_results(lcs_length, lcs_substrings)
if __name__ == '__main__':
    main()