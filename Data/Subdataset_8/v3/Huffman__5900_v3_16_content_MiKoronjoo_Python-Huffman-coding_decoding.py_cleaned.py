import sys
code_dictionary = {}
def generate_code_dictionary(file_name: str) -> None:
    try:
        with open(file_name, 'r') as file_stream:
            for line in file_stream:
                char, _, code = line.split('\t')
                char = char.replace('\\n', '\n').replace('\\t', '\t').replace('\\r', '\r')
                code_dictionary[code.strip()] = char
    except FileNotFoundError as ex:
        print(f"No such file or directory: {ex.filename}")
    except IsADirectoryError as ex:
        print(f"Is a directory: {ex.filename}")
def decode_binary_text(bin_text: str) -> str:
    temp_code = ''
    decoded_text = ''
    for bit in bin_text:
        temp_code += bit
        if temp_code in code_dictionary:
            char = code_dictionary[temp_code]
            if char == '\0':
                break
            decoded_text += char
            temp_code = ''
    return decoded_text
def main(zip_address: str, huffman_address: str) -> None:
    try:
        with open(zip_address, 'r') as file_stream:
            code_text = file_stream.read()
    except FileNotFoundError as ex:
        print(f'No such file or directory: {ex.filename}')
        return
    except IsADirectoryError as ex:
        print(f'Is a directory: {ex.filename}')
        return
    generate_code_dictionary(huffman_address)
    bin_text = ''
    for char in code_text:
        temp_code = bin(ord(char))[2:]
        temp_code = (8 - len(temp_code)) * '0' + temp_code
        bin_text += temp_code
    decoded_text = decode_binary_text(bin_text)
    with open('Output.txt', 'w') as file_stream:
        file_stream.write(decoded_text)
    print(f"File '{zip_address}' unzipped to 'Output.txt' successfully\n")
if __name__ == '__main__':
    try:
        zip_file_address, huffman_file_address = sys.argv[1], sys.argv[2]
    except IndexError:
        zip_file_address, huffman_file_address = 'Zip.txt', 'Huffman.txt'
    main(zip_file_address, huffman_file_address)