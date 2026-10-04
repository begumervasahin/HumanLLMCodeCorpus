import sys
from typing import Dict
def load_huffman_codes(file_name: str) -> Dict[str, str]:
    code_dic = {}
    try:
        with open(file_name, 'r') as file_stream:
            for line in file_stream:
                char, _, code = line.partition('\t')
                if char == '\\n':
                    char = '\n'
                elif char == '\\t':
                    char = '\t'
                elif char == '\\r':
                    char = '\r'
                code_dic[code.strip()] = char
    except FileNotFoundError as ex:
        print(f"No such file or directory: {ex.filename}")
    except IsADirectoryError as ex:
        print(f"Is a directory: {ex.filename}")
    return code_dic
def decode_binary_text(bin_text: str, code_dic: Dict[str, str]) -> str:
    temp_code = ''
    decoded_text = ''
    for bit in bin_text:
        temp_code += bit
        if temp_code in code_dic:
            char = code_dic[temp_code]
            if char == '\0':
                break
            decoded_text += char
            temp_code = ''
    return decoded_text
def convert_to_binary_string(text: str) -> str:
    return ''.join(f'{ord(char):08b}' for char in text)
def main(zip_address: str, huffman_address: str) -> None:
    try:
        with open(zip_address, 'r') as file_stream:
            code_text = file_stream.read()
    except FileNotFoundError as ex:
        print(f"No such file or directory: {ex.filename}")
        return
    except IsADirectoryError as ex:
        print(f"Is a directory: {ex.filename}")
        return
    code_dic = load_huffman_codes(huffman_address)
    if not code_dic:
        return
    bin_text = convert_to_binary_string(code_text)
    decoded_text = decode_binary_text(bin_text, code_dic)
    with open('Output.txt', 'w') as file_stream:
        file_stream.write(decoded_text)
    print(f"File '{zip_address}' unzipped to 'Output.txt' successfully\n")
if __name__ == '__main__':
    try:
        zip_file_address, huffman_file_address = sys.argv[1], sys.argv[2]
    except IndexError:
        zip_file_address, huffman_file_address = 'Zip.txt', 'Huffman.txt'
    main(zip_file_address, huffman_file_address)