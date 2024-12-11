import sys
import serial_hash_search
import parallel_hash_search
b1 = False
def fonk1(file_name):
    with open(file_name, 'r', b2 = 'utf-8') as file:
        return file.read()
if b3 = = '__main__':
    if len(sys.argv) == 3:
        b4 = fonk1(sys.argv[1])
        b5 = fonk1(sys.argv[2])
    else:
        print('Please provide two text file paths as arguments.')
        exit()
    b6 = parallel_hash_search.lcs if b1 else serial_hash_search.lcs
    length, b7 = b6(b4, b5)
    if len(b7) == 1:
        b8 = 'is'
    else:
        b8 = 'are'
    print(f'The length of the longest common substring is: {length}')
    print(f'There {b8} {len(b7)} longest common substring{"s" if len(b7) > 1 else ""}:')
    for substring in b7:
        print(f'"{substring}"')