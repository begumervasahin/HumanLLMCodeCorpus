
import sys
import serial_hash_search
import parallel_hash_search
b1 = False
def fonk1(file_name):
    with open(file_name, 'r', b2 = 'utf-8') as file:
        return file.read()
def fonk2():
    if len(sys.argv) == 3:
        b3 = fonk1(sys.argv[1])
        b4 = fonk1(sys.argv[2])
    else:
        print("Please provide two text file paths as arguments.")
        sys.exit(1)
    b5 = parallel_hash_search.lcs if b1 else serial_hash_search.lcs
    length, b6 = b5(b3, b4)
    if len(b6) == 1:
        b7 = ['is', '']
    else:
        b7 = ['are', 's']
    print(f"The length of the longest common substring is: {length}")
    print(f"There {b7[0]} {len(b6)} longest common substring{b7[1]}:")
    print('\n'.join(f'"{s}"' for s in b6))
if b8 = = '__main__':
    fonk2()