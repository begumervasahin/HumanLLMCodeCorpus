
import sys
import serial_hash_search
import parallel_hash_search
USE_PARALLEL = False
def read_text(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
        sys.exit(1)
def print_lcs_results(length, substrings):
    verb = 'is' if len(substrings) == 1 else 'are'
    plural_suffix = '' if len(substrings) == 1 else 's'
    print(f"The length of the longest common substring is: {length}")
    print(f"There {verb} {len(substrings)} longest common substring{plural_suffix}:")
    for substring in substrings:
        print(f'"{substring}"')
def main():
    if len(sys.argv) != 3:
        print("Usage: python script_name.py <file_path_1> <file_path_2>")
        sys.exit(1)
    file_a = read_text(sys.argv[1])
    file_b = read_text(sys.argv[2])
    lcs_function = parallel_hash_search.lcs if USE_PARALLEL else serial_hash_search.lcs
    length, substrings = lcs_function(file_a, file_b)
    print_lcs_results(length, substrings)
if __name__ == '__main__':
    main()