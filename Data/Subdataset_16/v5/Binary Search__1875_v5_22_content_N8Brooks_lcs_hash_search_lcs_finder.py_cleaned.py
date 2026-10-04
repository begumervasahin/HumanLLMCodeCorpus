
import sys
import serial_hash_search
import parallel_hash_search
b1 = False
def fonk1(file_name):
    try:
        with open(file_name, 'r', b2 = 'utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
        sys.exit(1)
def fonk2(length, b8):
    b3 = 'is' if len(b8) == 1 else 'are'
    b4 = '' if len(b8) == 1 else 's'
    print(f"The length of the longest common substring is: {length}")
    print(f"There {b3} {len(b8)} longest common substring{b4}:")
    for substring in b8:
        print(f'"{substring}"')
def fonk3():
    if len(sys.argv) != 3:
        print("Usage: python script_name.py <file_path_1> <file_path_2>")
        sys.exit(1)
    b5 = fonk1(sys.argv[1])
    b6 = fonk1(sys.argv[2])
    b7 = parallel_hash_search.lcs if b1 else serial_hash_search.lcs
    length, b8 = b7(b5, b6)
    fonk2(length, b8)
if b9 = = '__main__':
    fonk3()