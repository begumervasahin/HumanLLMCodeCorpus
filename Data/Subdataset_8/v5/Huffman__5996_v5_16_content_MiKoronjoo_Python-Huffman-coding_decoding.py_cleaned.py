import sys
code_dict = {}
def generate_huffman_codes(file_name: str) -> None:
    try:
        with open(file_name, 'r') as file_stream:
            for line in file_stream:
                char, _, code = line.split('\t')
                char = convert_escape_characters(char)
                code_dict[code.strip()] = char
    except FileNotFoundError as ex:
        handle_file_error(ex)
    except IsADirectoryError as ex:
        handle_file_error(ex)
def convert_escape_characters(char: str) -> str:
    escape_map = {'\\n': '\n', '\\t': '\t', '\\r': '\r'}
    return escape_map.get(char.strip(), char)
def handle_file_error(ex: Exception) -> None:
    print('Error:', ex)
def decode_binary_text(bin_text: str) -> str:
    temp_code = ''
    decoded_text = ''
    for bit in bin_text:
        temp_code += bit
        if temp_code in code_dict:
            char = code_dict[temp_code]
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
        handle_file_error(ex)
        return
    except IsADirectoryError as ex:
        handle_file_error(ex)
        return
    try:
        generate_huffman_codes(huffman_address)
    except FileNotFoundError as ex:
        handle_file_error(ex)
        return
    except IsADirectoryError as ex:
        handle_file_error(ex)
        return
    bin_text = ''.join(format(ord(char), '08b') for char in code_text)
    decoded_text = decode_binary_text(bin_text)
    with open('Output.txt', 'w') as file_stream:
        file_stream.write(decoded_text)
    print("File '%s' unzipped to 'Output.txt' successfully\n" % zip_address)
if __name__ == '__main__':
    try:
        zip_file_address, huffman_file_address = sys.argv[1], sys.argv[2]
    except IndexError:
        zip_file_address, huffman_file_address = 'Zip.txt', 'Huffman.txt'
    main(zip_file_address, huffman_file_address)