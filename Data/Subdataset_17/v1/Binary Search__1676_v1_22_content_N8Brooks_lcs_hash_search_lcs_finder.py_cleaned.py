import sys
import serial_hash_search
import parallel_hash_search
PARALLEL = False
def read_text(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        return file.read()
def main():
    if len(sys.argv) == 3:
        file_a = str(sys.argv[1])
        file_b = str(sys.argv[2])
        a = read_text(file_a)
        b = read_text(file_b)
    else:
        print('Please provide exactly two text file paths as arguments.')
        sys.exit(1)
    lcs_function = parallel_hash_search.lcs if PARALLEL else serial_hash_search.lcs
    length, substrings = lcs_function(a, b)
    if len(substrings) == 1:
        multiple = ['is', len(substrings), '']
    else:
        multiple = ['are', len(substrings), 's']
    print(f'The length of the longest common substring is: {length}')
    print(f'There {multiple[0]} {multiple[1]} longest common substring{multiple[2]}:')
    print('\n'.join(f'"{s}"' for s in substrings))
if __name__ == '__main__':
    main()