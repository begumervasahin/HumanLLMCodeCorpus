import sys
b1 = {}
def fonk1(file_name: str) -> None:
    b2 = open(file_name, 'r')
    for line in b2.readlines():
        b4, _, b3 = line.split('\t')
        if b4 = = '\\n':
            b4 = '\n'
        elif b4 = = '\\t':
            b4 = '\t'
        elif b4 = = '\\r':
            b4 = '\r'
        b1.update({b3.strip(): b4})
def fonk2(b8: str) -> str:
    b5 = ''
    b6 = ''
    for b in b8:
        b5 += b
        if b5 in b1:
            b4 = b1[b5]
            if b4 = = '\0':
                break
            b6 += b4
            b5 = ''
    return b6
def fonk3(zip_address: str, huffman_address: str) -> None:
    try:
        b2 = open(zip_address, 'r')
        b7 = b2.read()
        b2.close()
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
    b8 = ''
    for b4 in b7:
        b5 = bin(ord(b4))[2:]
        if len(b5) < 8:
            b5 = (8 - len(b5)) * '0' + b5
        b8 += b5
    b6 = fonk2(b8)
    b2 = open('Output.txt', 'w')
    b2.write(b6)
    b2.close()
    print("File '%s' unzipped to 'Output.txt' successfully\n" % zip_address)
if b9 = = '__main__':
    try:
        zip_file_address, b10 = sys.argv[1], sys.argv[2]
    except IndexError:
        zip_file_address, b10 = 'Zip.txt', 'Huffman.txt'
    fonk3(zip_file_address, b10)