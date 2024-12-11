import sys
b1 = {}
def fonk1(file_name: str) -> None:
    with open(file_name, 'r') as file_stream:
        for line in file_stream:
            b3, _, b2 = line.split('\t')
            b3 = b3.replace('\\n', '\n').replace('\\t', '\t').replace('\\r', '\r')
            b1[b2.strip()] = b3
def fonk2(b7: str) -> str:
    b4 = ''
    b5 = ''
    for b in b7:
        b4 += b
        if b4 in b1:
            b3 = b1[b4]
            if b3 = = '\0':
                break
            b5 += b3
            b4 = ''
    return b5
def fonk3(zip_address: str, huffman_address: str) -> None:
    try:
        with open(zip_address, 'r') as file_stream:
            b6 = file_stream.read()
    except FileNotFoundError as ex:
        print('No such file or directory:', ex.filename)
        return
    except IsADirectoryError as ex:
        print('Is a directory:', ex.filename)
        return
    try:
        fonk1(huffman_address)
    except FileNotFoundError as ex:
        print('No such file or directory:', ex.filename)
        return
    except IsADirectoryError as ex:
        print('Is a directory:', ex.filename)
        return
    b7 = ''
    for b3 in b6:
        b4 = bin(ord(b3))[2:]
        if len(b4) < 8:
            b4 = (8 - len(b4)) * '0' + b4
        b7 += b4
    b5 = fonk2(b7)
    with open('Output.txt', 'w') as file_stream:
        file_stream.write(b5)
    print("File '%s' unzipped to 'Output.txt' successfully\n" % zip_address)
if b8 = = '__main__':
    try:
        zip_file_address, b9 = sys.argv[1], sys.argv[2]
    except IndexError:
        zip_file_address, b9 = 'Zip.txt', 'Huffman.txt'
    fonk3(zip_file_address, b9)