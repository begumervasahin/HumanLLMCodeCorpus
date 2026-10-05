import sys
import serial_hash_search
import parallel_hash_search
PARALLEL = False
def read_text(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        return file.read()
if __name__ == '__main__':
    if len(sys.argv) == 3:
        a = read_text(sys.argv[1])
        b = read_text(sys.argv[2])
    else:
        print('Please enter two text file arguments to read.')
        exit()
    lcs = parallel_hash_search.lcs if PARALLEL else serial_hash_search.lcs
    length, substrings = lcs(a, b)
    if len(substrings) == 1:
        multiple = ['is', len(substrings), '']
    else:
        multiple = ['are', len(substrings), 's']
    print(f'The length of the longest common substring is: {length}')
    print('There {} {} longest common substring{}:'.format(*multiple))
    print('\n'.join(f'"{s}"' for s in substrings), end='')