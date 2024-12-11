
import sys
import serial_hash_search
import parallel_hash_search
b1 = False
def fonk1(file_name):
    with open(file_name, 'r', b2 = 'utf-8') as file:
        return file.read()
if b3 = = '__main__':
    if len(sys.argv) == 3:
        b4 = str(sys.argv[1])
        b5 = str(sys.argv[2])
        b6 = fonk1(b4)
        b7 = fonk1(b5)
    else:
        print('Please provide two text file arguments.')
        exit()
    b8 = parallel_hash_search.lcs if b1 else serial_hash_search.lcs
    length, b9 = b8(b6, b7)
    if len(b9) == 1:
        b10 = ('is', len(b9), '')
    else:
        b10 = ('are', len(b9), 's')
    print(f'The length of the longest common substring is: {length}')
    print(f'There {b10[0]} {b10[1]} longest common substring{b10[2]}:')
    print('\n'.join(f'"{s}"' for s in b9), b11 = '')