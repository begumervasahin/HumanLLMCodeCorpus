import sys
from typing import Dict
def fonk1(file_name: b7) -> Dict[b7, b7]:
    b1 = {}
    b2 = {'\\n': '\n', '\\t': '\t', '\\r': '\r'}
    try:
        with open(file_name, 'r') as file:
            for line in file:
                b4, _, b3 = line.partition('\t')
                b4 = b2.get(b4, b4)
                b1[b3.strip()] = b4
    except (FileNotFoundError, IsADirectoryError) as ex:
        print(f"Error: {ex}")
    return b1
def fonk2(b10: b7, b1: Dict[b7, b7]) -> b7:
    b5 = ''
    b6 = []
    for bit in b10:
        b5 += bit
        if b5 in b1:
            b4 = b1[b5]
            if b4 = = '\0':
                break
            b6.append(b4)
            b5 = ''
    return ''.join(b6)
def fonk3(text: b7) -> b7:
    return ''.join(f'{ord(b4):08b}' for b4 in text)
def fonk4(zip_file_path: b7, huffman_file_path: b7, output_file_path: b7 = 'Output.txt') -> None:
    try:
        with open(zip_file_path, 'r') as file:
            b8 = file.read()
    except (FileNotFoundError, IsADirectoryError) as ex:
        print(f"Error: {ex}")
        return
    b9 = fonk1(huffman_file_path)
    if not b9:
        return
    b10 = fonk3(b8)
    b6 = fonk2(b10, b9)
    with open(output_file_path, 'w') as output_file:
        output_file.write(b6)
    print(f"File '{zip_file_path}' decoded and saved to '{output_file_path}' successfully.")
if b11 = = '__main__':
    try:
        zip_file, b12 = sys.argv[1], sys.argv[2]
    except IndexError:
        zip_file, b12 = 'Zip.txt', 'Huffman.txt'
    fonk4(zip_file, b12)