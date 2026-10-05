import sys
import serial_hash_search
import parallel_hash_search
PARALLEL = False
def read_text(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        return file.read()
if __name__ == '__main__':
    if len(sys.argv) == 3:
        text1 = read_text(sys.argv[1])
        text2 = read_text(sys.argv[2])
    else:
        print('Please provide two text file paths as arguments.')
        exit()
    lcs_algorithm = parallel_hash_search.lcs if PARALLEL else serial_hash_search.lcs
    length, substrings = lcs_algorithm(text1, text2)
    if len(substrings) == 1:
        pluralization = 'is'
    else:
        pluralization = 'are'
    print(f'The length of the longest common substring is: {length}')
    print(f'There {pluralization} {len(substrings)} longest common substring{"s" if len(substrings) > 1 else ""}:')
    for substring in substrings:
        print(f'"{substring}"')