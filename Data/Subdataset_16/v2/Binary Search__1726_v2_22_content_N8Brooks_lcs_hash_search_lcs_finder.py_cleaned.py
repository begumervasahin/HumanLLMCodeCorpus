import sys
import serial_hash_search
import parallel_hash_search
b1 = False
def fonk1(file_name):
    try:
        with open(file_name, 'r', b2 = 'utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        sys.exit(1)
    except IOError as e:
        print(f"Error reading file '{file_name}': {e}")
        sys.exit(1)
def fonk2():
    if len(sys.argv) != 3:
        print("Usage: python script.py <file1> <file2>")
        sys.exit(1)
    file_a, b3 = sys.argv[1], sys.argv[2]
    b4 = fonk1(file_a)
    b5 = fonk1(b3)
    b6 = parallel_hash_search.lcs if b1 else serial_hash_search.lcs
    lcs_length, b7 = b6(b4, b5)
    b8 = 's' if len(b7) > 1 else ''
    b9 = 'are' if len(b7) > 1 else 'is'
    print(f'The length of the longest common substring is: {lcs_length}')
    print(f'There {b9} {len(b7)} longest common substring{b8}:')
    for substring in b7:
        print(f'"{substring}"')
if b10 = = '__main__':
    fonk2()