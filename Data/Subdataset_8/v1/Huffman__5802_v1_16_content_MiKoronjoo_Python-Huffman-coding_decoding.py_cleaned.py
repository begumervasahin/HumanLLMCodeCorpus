import sys
code_dic = {}
def generate_dic(file_name: str) -> None:
    with open(file_name, 'r') as file_stream:
        for line in file_stream:
            char, _, code = line.split('\t')
            char = char.replace('\\n', '\n').replace('\\t', '\t').replace('\\r', '\r')
            code_dic[code.strip()] = char
def decoding(bin_text: str) -> str:
    temp_code = ''
    decode_text = ''
    for b in bin_text:
        temp_code += b
        if temp_code in code_dic:
            char = code_dic[temp_code]
            if char == '\0':
                break
            decode_text += char
            temp_code = ''
    return decode_text
def main(zip_address: str, huffman_address: str) -> None:
    try:
        with open(zip_address, 'r') as file_stream:
            code_text = file_stream.read()
    except FileNotFoundError as ex:
        print('No such file or directory:', ex.filename)
        return
    except IsADirectoryError as ex:
        print('Is a directory:', ex.filename)
        return
    try:
        generate_dic(huffman_address)
    except FileNotFoundError as ex:
        print('No such file or directory:', ex.filename)
        return
    except IsADirectoryError as ex:
        print('Is a directory:', ex.filename)
        return
    bin_text = ''
    for char in code_text:
        temp_code = bin(ord(char))[2:]
        if len(temp_code) < 8:
            temp_code = (8 - len(temp_code)) * '0' + temp_code
        bin_text += temp_code
    decode_text = decoding(bin_text)
    with open('Output.txt', 'w') as file_stream:
        file_stream.write(decode_text)
    print("File '%s' unzipped to 'Output.txt' successfully\n" % zip_address)
if __name__ == '__main__':
    try:
        zip_file_address, huffman_file_address = sys.argv[1], sys.argv[2]
    except IndexError:
        zip_file_address, huffman_file_address = 'Zip.txt', 'Huffman.txt'
    main(zip_file_address, huffman_file_address)