import sys
import serial_hash_search
import parallel_hash_search
PARALLEL = False
def read_text(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        sys.exit(1)
    except IOError as e:
        print(f"Error reading file '{file_name}': {e}")
        sys.exit(1)
def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <file1> <file2>")
        sys.exit(1)
    file_a, file_b = sys.argv[1], sys.argv[2]
    text_a = read_text(file_a)
    text_b = read_text(file_b)
    lcs_function = parallel_hash_search.lcs if PARALLEL else serial_hash_search.lcs
    lcs_length, lcs_substrings = lcs_function(text_a, text_b)
    plural_suffix = 's' if len(lcs_substrings) > 1 else ''
    verb = 'are' if len(lcs_substrings) > 1 else 'is'
    print(f'The length of the longest common substring is: {lcs_length}')
    print(f'There {verb} {len(lcs_substrings)} longest common substring{plural_suffix}:')
    for substring in lcs_substrings:
        print(f'"{substring}"')
if __name__ == '__main__':
    main()