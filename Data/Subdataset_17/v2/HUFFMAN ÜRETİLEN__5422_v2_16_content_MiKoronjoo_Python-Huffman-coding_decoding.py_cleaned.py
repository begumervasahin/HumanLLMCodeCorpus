import sys
from typing import Dict
def load_huffman_codes(file_name: str) -> Dict[str, str]:
    code_dict = {}
    special_chars = {'\\n': '\n', '\\t': '\t', '\\r': '\r'}
    try:
        with open(file_name, 'r') as file:
            for line in file:
                char, _, code = line.partition('\t')
                char = special_chars.get(char, char)
                code_dict[code.strip()] = char
    except (FileNotFoundError, IsADirectoryError) as ex:
        print(f"Error: {ex}")
    return code_dict
def decode_binary_text(binary_text: str, code_dict: Dict[str, str]) -> str:
    temp_code = ''
    decoded_text = []
    for bit in binary_text:
        temp_code += bit
        if temp_code in code_dict:
            char = code_dict[temp_code]
            if char == '\0':
                break
            decoded_text.append(char)
            temp_code = ''
    return ''.join(decoded_text)
def convert_to_binary_string(text: str) -> str:
    return ''.join(f'{ord(char):08b}' for char in text)
def decode_huffman_file(zip_file_path: str, huffman_file_path: str, output_file_path: str = 'Output.txt') -> None:
    try:
        with open(zip_file_path, 'r') as file:
            encoded_text = file.read()
    except (FileNotFoundError, IsADirectoryError) as ex:
        print(f"Error: {ex}")
        return
    huffman_codes = load_huffman_codes(huffman_file_path)
    if not huffman_codes:
        return
    binary_text = convert_to_binary_string(encoded_text)
    decoded_text = decode_binary_text(binary_text, huffman_codes)
    with open(output_file_path, 'w') as output_file:
        output_file.write(decoded_text)
    print(f"File '{zip_file_path}' decoded and saved to '{output_file_path}' successfully.")
if __name__ == '__main__':
    try:
        zip_file, huffman_file = sys.argv[1], sys.argv[2]
    except IndexError:
        zip_file, huffman_file = 'Zip.txt', 'Huffman.txt'
    decode_huffman_file(zip_file, huffman_file)