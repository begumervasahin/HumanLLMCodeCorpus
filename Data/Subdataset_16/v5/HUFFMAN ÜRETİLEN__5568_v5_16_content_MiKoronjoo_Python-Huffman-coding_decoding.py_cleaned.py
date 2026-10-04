import sys
def fonk1(file_name: str) -> dict:
    b1 = {}
    b2 = {'\\n': '\n', '\\t': '\t', '\\r': '\r'}
    try:
        with open(file_name, 'r') as file:
            for line in file:
                b4, _, b3 = line.strip().split('\t')
                b4 = b2.get(b4, b4)
                b1[b3] = b4
    except FileNotFoundError:
        print(f"Error: File not found - {file_name}")
    except IsADirectoryError:
        print(f"Error: Expected file but found directory - {file_name}")
    return b1
def fonk2(b7: str, b1: dict) -> str:
    b5 = []
    b6 = ''
    for bit in b7:
        b6 += bit
        if b6 in b1:
            b4 = b1[b6]
            if b4 = = '\0':
                break
            b5.append(b4)
            b6 = ''
    return ''.join(b5)
def fonk3(text: str) -> str:
    return ''.join(f'{ord(b4):08b}' for b4 in text)
def fonk4(zip_address: str, huffman_address: str) -> None:
    try:
        with open(zip_address, 'r') as file:
            b7 = file.read()
    except FileNotFoundError:
        print(f"Error: File not found - {zip_address}")
        return
    except IsADirectoryError:
        print(f"Error: Expected file but found directory - {zip_address}")
        return
    b1 = fonk1(huffman_address)
    if not b1:
        return
    b7 = fonk3(b7)
    b5 = fonk2(b7, b1)
    b8 = 'Output.txt'
    with open(b8, 'w') as output_file:
        output_file.write(b5)
    print(f"Decoding complete. Output saved to '{b8}'.")
if b9 = = '__main__':
    if len(sys.argv) >= 3:
        b10 = sys.argv[1]
        b11 = sys.argv[2]
    else:
        b10 = 'Zip.txt'
        b11 = 'Huffman.txt'
    fonk4(b10, b11)