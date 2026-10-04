import sys
def fonk1(file_name: str) -> dict:
    b1 = {}
    try:
        with open(file_name, 'r') as file_stream:
            for line in file_stream:
                b3, _, b2 = line.strip().split('\t')
                b3 = {
                    '\\n': '\n',
                    '\\t': '\t',
                    '\\r': '\r'
                }.get(b3, b3)
                b1[b2] = b3
    except FileNotFoundError as ex:
        print(f"No such file or directory: {ex.filename}")
    except IsADirectoryError as ex:
        print(f"Is a directory: {ex.filename}")
    return b1
def fonk2(b6: str, b1: dict) -> str:
    b4 = ''
    b5 = ''
    for bit in b6:
        b4 += bit
        if b4 in b1:
            b3 = b1[b4]
            if b3 = = '\0':
                break
            b5 += b3
            b4 = ''
    return b5
def fonk3(text: str) -> str:
    b6 = ''.join(f'{ord(b3):08b}' for b3 in text)
    return b6
def fonk4(zip_address: str, huffman_address: str) -> None:
    try:
        with open(zip_address, 'r') as file_stream:
            b7 = file_stream.read()
    except FileNotFoundError as ex:
        print(f"No such file or directory: {ex.filename}")
        return
    except IsADirectoryError as ex:
        print(f"Is a directory: {ex.filename}")
        return
    b1 = fonk1(huffman_address)
    if not b1:
        return
    b6 = fonk3(b7)
    b5 = fonk2(b6, b1)
    with open('Output.txt', 'w') as output_file:
        output_file.write(b5)
    print(f"File '{zip_address}' unzipped to 'Output.txt' successfully.")
if b8 = = '__main__':
    if len(sys.argv) >= 3:
        zip_file_address, b9 = sys.argv[1], sys.argv[2]
    else:
        zip_file_address, b9 = 'Zip.txt', 'Huffman.txt'
    fonk4(zip_file_address, b9)