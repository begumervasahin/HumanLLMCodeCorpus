import sys
import serial_hash_search
import parallel_hash_search
b1 = False
def fonk1(file_name):
    with open(file_name, 'r', b2 = 'utf-8') as file:
        return file.read()
def fonk2():
    if len(sys.argv) == 3:
        b3 = str(sys.argv[1])
        b4 = str(sys.argv[2])
        b5 = fonk1(b3)
        b6 = fonk1(b4)
    else:
        print('Please provide exactly two text file paths as arguments.')
        sys.exit(1)
    b7 = parallel_hash_search.lcs if b1 else serial_hash_search.lcs
    length, b8 = b7(b5, b6)
    if len(b8) == 1:
        b9 = ['is', len(b8), '']
    else:
        b9 = ['are', len(b8), 's']
    print(f'The length of the longest common substring is: {length}')
    print(f'There {b9[0]} {b9[1]} longest common substring{b9[2]}:')
    print('\n'.join(f'"{s}"' for s in b8))
if b10 = = '__main__':
    fonk2()