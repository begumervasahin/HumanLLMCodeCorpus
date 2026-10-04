
import sys
import serial_hash_search
import parallel_hash_search
PARALLEL = False
def read_text(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        return file.read()
def main():
    if len(sys.argv) == 3:
        file_a = read_text(sys.argv[1])
        file_b = read_text(sys.argv[2])
    else:
        print("Please provide two text file paths as arguments.")
        sys.exit(1)
    lcs_function = parallel_hash_search.lcs if PARALLEL else serial_hash_search.lcs
    length, substrings = lcs_function(file_a, file_b)
    if len(substrings) == 1:
        multiple = ['is', '']
    else:
        multiple = ['are', 's']
    print(f"The length of the longest common substring is: {length}")
    print(f"There {multiple[0]} {len(substrings)} longest common substring{multiple[1]}:")
    print('\n'.join(f'"{s}"' for s in substrings))
if __name__ == '__main__':
    main()