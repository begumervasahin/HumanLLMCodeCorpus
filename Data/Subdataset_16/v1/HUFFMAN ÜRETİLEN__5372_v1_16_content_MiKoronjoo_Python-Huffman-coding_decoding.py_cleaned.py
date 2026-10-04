import sys
from typing import Dict
def fonk1(file_name: str) -> Dict[str, str]:
    b1 = {}
    try:
        with open(file_name, 'r') as file_stream:
            for line in file_stream:
                b3, _, b2 = line.partition('\t')
                if b3 = = '\\n':
                    b3 = '\n'
                elif b3 = = '\\t':
                    b3 = '\t'
                elif b3 = = '\\r':
                    b3 = '\r'
                b1[b2.strip()] = b3
    except FileNotFoundError as ex:
        print(f"No such file or directory: {ex.filename}")
    except IsADirectoryError as ex:
        print(f"Is a directory: {ex.filename}")
    return b1
def fonk2(b7: str, b1: Dict[str, str]) -> str:
    b4 = ''
    b5 = ''
    for bit in b7:
        b4 += bit
        if b4 in b1:
            b3 = b1[b4]
            if b3 = = '\0':
                break
            b5 += b3
            b4 = ''
    return b5
def fonk3(text: str) -> str:
    return ''.join(f'{ord(b3):08b}' for b3 in text)
def fonk4(zip_address: str, huffman_address: str) -> None:
    try:
        with open(zip_address, 'r') as file_stream:
            b6 = file_stream.read()
    except FileNotFoundError as ex:
        print(f"No such file or directory: {ex.filename}")
        return
    except IsADirectoryError as ex:
        print(f"Is a directory: {ex.filename}")
        return
    b1 = fonk1(huffman_address)
    if not b1:
        return
    b7 = fonk3(b6)
    b5 = fonk2(b7, b1)
    with open('Output.txt', 'w') as file_stream:
        file_stream.write(b5)
    print(f"File '{zip_address}' unzipped to 'Output.txt' successfully\n")
if b8 = = '__main__':
    try:
        zip_file_address, b9 = sys.argv[1], sys.argv[2]
    except IndexError:
        zip_file_address, b9 = 'Zip.txt', 'Huffman.txt'
    fonk4(zip_file_address, b9)