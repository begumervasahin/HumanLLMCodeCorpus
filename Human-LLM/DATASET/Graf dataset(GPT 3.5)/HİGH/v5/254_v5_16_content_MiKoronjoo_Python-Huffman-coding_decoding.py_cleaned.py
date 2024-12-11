import sys
b1 = {}
def fonk1(file_name: str) -> None:
    try:
        with open(file_name, 'r') as file_stream:
            for line in file_stream:
                b3, _, b2 = line.split('\t')
                b3 = fonk2(b3)
                b1[b2.strip()] = b3
    except FileNotFoundError as ex:
        fonk3(ex)
    except IsADirectoryError as ex:
        fonk3(ex)
def fonk2(b3: str) -> str:
    b4 = {'\\n': '\n', '\\t': '\t', '\\r': '\r'}
    return b4.get(b3.strip(), b3)
def fonk3(ex: Exception) -> None:
    print('Error:', ex)
def fonk4(b8: str) -> str:
    b5 = ''
    b6 = ''
    for bit in b8:
        b5 += bit
        if b5 in b1:
            b3 = b1[b5]
            if b3 = = '\0':
                break
            b6 += b3
            b5 = ''
    return b6
def fonk5(zip_address: str, huffman_address: str) -> None:
    try:
        with open(zip_address, 'r') as file_stream:
            b7 = file_stream.read()
    except FileNotFoundError as ex:
        fonk3(ex)
        return
    except IsADirectoryError as ex:
        fonk3(ex)
        return
    try:
        fonk1(huffman_address)
    except FileNotFoundError as ex:
        fonk3(ex)
        return
    except IsADirectoryError as ex:
        fonk3(ex)
        return
    b8 = ''.join(format(ord(b3), '08b') for b3 in b7)
    b6 = fonk4(b8)
    with open('Output.txt', 'w') as file_stream:
        file_stream.write(b6)
    print("File '%s' unzipped to 'Output.txt' successfully\n" % zip_address)
if b9 = = '__main__':
    try:
        zip_file_address, b10 = sys.argv[1], sys.argv[2]
    except IndexError:
        zip_file_address, b10 = 'Zip.txt', 'Huffman.txt'
    fonk5(zip_file_address, b10)