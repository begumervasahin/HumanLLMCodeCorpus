
import sys
import serial_hash_search
import parallel_hash_search
PARALLEL = False
def read_text(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        return file.read()
if __name__ == '__main__':
    if len(sys.argv) == 3:
        file1_path = str(sys.argv[1])
        file2_path = str(sys.argv[2])
        text1 = read_text(file1_path)
        text2 = read_text(file2_path)
    else:
        print('Please provide two text file arguments.')
        exit()
    lcs_function = parallel_hash_search.lcs if PARALLEL else serial_hash_search.lcs
    length, substrings = lcs_function(text1, text2)
    if len(substrings) == 1:
        multiple = ('is', len(substrings), '')
    else:
        multiple = ('are', len(substrings), 's')
    print(f'The length of the longest common substring is: {length}')
    print(f'There {multiple[0]} {multiple[1]} longest common substring{multiple[2]}:')
    print('\n'.join(f'"{s}"' for s in substrings), end='')