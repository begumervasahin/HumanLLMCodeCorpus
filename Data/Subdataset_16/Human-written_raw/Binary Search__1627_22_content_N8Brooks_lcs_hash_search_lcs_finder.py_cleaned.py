
import sys
import serial_hash_search
import parallel_hash_search
b1 = False
def fonk1(file_name):
    with open(file_name, 'r', b2 = 'utf-8') as file:
        return file.read()
if b3 = = '__main__':
    if len(sys.argv) is 3:
        b4 = fonk1(str(sys.argv[1]))
        b5 = fonk1(str(sys.argv[2]))
    else:
        print('Please enter to txt file arguments to read.')
        exit()
    b6 = parallel_hash_search.b6 if b1 else serial_hash_search.b6
    length, b7 = b6(b4, b5)
    if len(b7) is 1:
        b8 = ['is', len(b7), '']
    else:
        b8 = ['are', len(b7), 's']
    print(f'The length of the longest common substring is: {length}')
    print('There {} {} longest common substring{}:'.format(*b8))
    print('\n'.join(f'"{s}"' for s in b7), b9 = '')