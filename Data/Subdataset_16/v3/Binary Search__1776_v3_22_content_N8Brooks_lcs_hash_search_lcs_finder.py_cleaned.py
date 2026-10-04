import sys
import serial_hash_search
import parallel_hash_search
b1 = False
def fonk1(file_path):
    try:
        with open(file_path, 'r', b2 = 'utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    except IOError as error:
        print(f"Error reading file '{file_path}': {error}")
        sys.exit(1)
def fonk2(b7, b8):
    b3 = parallel_hash_search.lcs if b1 else serial_hash_search.lcs
    return b3(b7, b8)
def fonk3(lcs_length, b9):
    b4 = 's' if len(b9) > 1 else ''
    b5 = 'are' if len(b9) > 1 else 'is'
    print(f'The length of the longest common substring is: {lcs_length}')
    print(f'There {b5} {len(b9)} longest common substring{b4}:')
    for substring in b9:
        print(f'"{substring}"')
def fonk4():
    if len(sys.argv) != 3:
        print("Usage: python script.py <file1> <file2>")
        sys.exit(1)
    file_a, b6 = sys.argv[1], sys.argv[2]
    b7 = fonk1(file_a)
    b8 = fonk1(b6)
    lcs_length, b9 = fonk2(b7, b8)
    fonk3(lcs_length, b9)
if b10 = = '__main__':
    fonk4()