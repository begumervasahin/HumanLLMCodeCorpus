import collections
from typing import List, Dict, Tuple
def get_file_contents(file_name: str) -> str:
    with open(file_name, 'r') as file:
        return file.read()
def calculate_frequencies(contents: str) -> List[Tuple[int, str]]:
    frequency = collections.Counter(contents)
    return sorted(frequency.items(), key=lambda item: item[1], reverse=True)
def build_huffman_tree(frequencies: List[Tuple[int, str]]) -> List[Tuple[int, str]]:
    nodes = [[freq, char] for char, freq in frequencies]
    while len(nodes) > 1:
        nodes.sort(key=lambda x: x[0])
        left, right = nodes.pop(0), nodes.pop(0)
        combined_node = [left[0] + right[0], left[1] + right[1]]
        nodes.append(combined_node)
        left.append('0')
        right.append('1')
    return nodes
def generate_huffman_codes(tree: List[Tuple[int, str]], original_chars: List[str]) -> List[Tuple[str, str]]:
    if len(original_chars) == 1:
        return [(original_chars[0], '0')]
    codes = []
    for char in original_chars:
        code = ''.join(node[2] for node in tree if len(node) > 2 and char in node[1])
        codes.append((char, code))
    return codes
def encode_contents(contents: str, huffman_codes: List[Tuple[str, str]]) -> str:
    return ''.join(code for char in contents for item, code in huffman_codes if char == item)
def display_huffman_table(huffman_codes: List[Tuple[str, str]], frequencies: Dict[str, int]):
    print('Character\tBinary Huffman\tBinary ASCII')
    huffman_codes_sorted = sorted(huffman_codes, key=lambda item: frequencies[item[0]], reverse=True)
    for char, code in huffman_codes_sorted:
        ascii_binary = bin(ord(char))[2:]
        print(f"'{char}'\t\t{code}\t\t{ascii_binary}")
def main():
    print('Huffman Encoding Program')
    file_name = input('Enter the name of a text file to open (without extension): ') + '.txt'
    try:
        contents = get_file_contents(file_name)
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
        return
    frequencies = calculate_frequencies(contents)
    original_chars = [char for _, char in frequencies]
    huffman_tree = build_huffman_tree(frequencies)
    huffman_codes = generate_huffman_codes(huffman_tree, original_chars)
    bitstring = encode_contents(contents, huffman_codes)
    print("The contents of the file are:", repr(contents))
    print("The Huffman encoded contents are:", repr(bitstring))
    frequencies_dict = dict(frequencies)
    display_huffman_table(huffman_codes, frequencies_dict)
if __name__ == '__main__':
    main()